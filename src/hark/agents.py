"""Agent callables for the hark debate harness."""

from __future__ import annotations

import logging
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from hark.config import MODELS
from hark.state import DebateState

logger = logging.getLogger(__name__)

ANTI_SLOP = (
    "Write plainly and directly. "
    "No em dashes. No groups of three examples or clauses. "
    "No 'delve', 'tapestry', 'moreover', 'furthermore', 'underscores', 'multifaceted'. "
    "No setup-then-flip lines. No tidy closing contrasts. "
    "No hype adjectives without real numbers. "
    "If you would not say it at a bar, do not type it."
)


def _get_llm(model_config: dict[str, BaseChatModel], role: str) -> BaseChatModel:
    if role not in model_config:
        raise KeyError(f"No model for role '{role}'. Available: {list(model_config)}")
    return model_config[role]


async def _run_tool_calls(response, tools: list[Any]) -> list[str]:
    """Execute tool calls from an LLM response and return citation strings."""
    if not tools or not getattr(response, "tool_calls", None):
        return []
    tool_map = {t.name: t for t in tools}
    results: list[str] = []
    for tc in response.tool_calls:
        name = tc.get("name", "search")
        args = tc.get("args", {})
        results.append(f"[{name}] args={args}")
        if name in tool_map:
            output = await tool_map[name].ainvoke(args)
            results.append(f"  result: {output}")
    return results


async def _turn(state: DebateState, model_config: dict, tools: list[Any] | None, side: str, collection: str = "shakespeare") -> dict:
    """One conversational turn. Sees full transcript so far. Stays under charlimit."""
    llm = _get_llm(model_config, side)
    tools = tools or []
    llm_with_tools = llm.bind_tools(tools) if tools else llm
    stance = "FOR" if side == "argue_for" else "AGAINST"

    system = (
        f"You argue {stance} the given claim in a live debate. {ANTI_SLOP} "
        f"Respond to what the other side said. Keep it under {state.charlimit} characters. "
        "Be direct. Make one point per turn. Do not restate the claim. "
        "Use the search tool if you need evidence. "
        f"When calling the search tool, always use collection=\"{collection}\". "
    )

    history = "\n".join(
        f"{t['side'].upper()}: {t['text']}" for t in state.transcript
    ) or "(no prior turns)"

    human = (
        f"Claim: {state.claim}\n\n"
        f"Transcript so far:\n{history}\n\n"
        f"Your turn. Argue {stance}. Under {state.charlimit} characters."
    )

    messages = [SystemMessage(content=system), HumanMessage(content=human)]
    response = await llm_with_tools.ainvoke(messages)
    citations = await _run_tool_calls(response, tools)

    if citations:
        refs = "\n".join(citations)
        response = await llm.ainvoke([
            SystemMessage(content=system),
            HumanMessage(content=(
                f"Claim: {state.claim}\n\n"
                f"Transcript so far:\n{history}\n\n"
                f"You found these references:\n{refs}\n\n"
                f"Your turn. Argue {stance}. Under {state.charlimit} characters. Cite the references."
            )),
        ])

    text = response.content if isinstance(response.content, str) else str(response.content)
    text = text[:state.charlimit]
    model_name = getattr(llm, "model", side)
    print(f"\n[{stance} | {model_name}]\n{text}")

    side_label = "for" if side == "argue_for" else "against"
    entry = {"side": side_label, "text": text, "model": model_name}
    return {"transcript": state.transcript + [entry], "status": "debating"}


async def argue_for(state: DebateState, model_config: dict, tools: list[Any] | None = None, collection: str = "shakespeare") -> dict:
    return await _turn(state, model_config, tools, "argue_for", collection)


async def argue_against(state: DebateState, model_config: dict, tools: list[Any] | None = None, collection: str = "shakespeare") -> dict:
    return await _turn(state, model_config, tools, "argue_against", collection)


async def synthesize(state: DebateState, model_config: dict, tools: list[Any] | None = None, collection: str = "shakespeare") -> dict:
    """Merge the full transcript into a balanced summary."""
    llm = _get_llm(model_config, "synthesize")

    system = (
        f"You synthesize a debate transcript into a balanced summary. {ANTI_SLOP} "
        "State where each side is strongest and where it is weakest. "
        "Do not declare a winner. Do not hedge with 'on the other hand' scaffolding. "
        "Be direct. Return your synthesis as plain text."
    )

    transcript_text = "\n\n".join(
        f"[{t['side'].upper()} | {t['model']}]\n{t['text']}" for t in state.transcript
    )
    human = (
        f"Claim: {state.claim}\n\n"
        f"Transcript:\n{transcript_text}\n\n"
        "Synthesize this debate into a balanced assessment."
    )

    response = await llm.ainvoke([SystemMessage(content=system), HumanMessage(content=human)])
    text = response.content if isinstance(response.content, str) else str(response.content)
    model_name = getattr(llm, "model", "synthesize")
    print(f"\n{'=' * 60}\nSYNTHESIS [{model_name}]\n{'=' * 60}\n{text}\n{'=' * 60}\n")
    logger.info("synthesize produced %d chars", len(text))
    return {"synthesis": text, "status": "done"}


def make_model_config(
    argue_for_model: str | None = None,
    argue_against_model: str | None = None,
    synthesize_model: str | None = None,
) -> dict[str, BaseChatModel]:
    """Build model config from provider:model strings. Defaults from hark.config.MODELS."""
    config: dict[str, BaseChatModel] = {}
    role_model_map = {
        "argue_for": argue_for_model or MODELS["argue_for"],
        "argue_against": argue_against_model or MODELS["argue_against"],
        "synthesize": synthesize_model or MODELS["synthesize"],
    }

    for role, spec in role_model_map.items():
        provider, _, model_name = spec.partition(":")
        if provider == "ollama":
            from langchain_ollama import ChatOllama
            config[role] = ChatOllama(model=model_name)
        elif provider == "openai":
            from langchain_openai import ChatOpenAI
            config[role] = ChatOpenAI(model=model_name)
        elif provider == "anthropic":
            from langchain_anthropic import ChatAnthropic
            config[role] = ChatAnthropic(model=model_name)
        else:
            raise ValueError(f"Unknown provider '{provider}'. Use ollama, openai, or anthropic.")

    return config

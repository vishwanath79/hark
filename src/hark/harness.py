"""LangGraph StateGraph for the hark debate harness.

Alternating turns: argue_for -> argue_against, repeated for N rounds.
Then synthesize reads the full transcript.
"""

from __future__ import annotations

import logging
from typing import Any

from langgraph.graph import END, START, StateGraph

from hark.agents import argue_against, argue_for, synthesize
from hark.state import DebateState

logger = logging.getLogger(__name__)


def _make_node(fn, model_config, tools, collection="shakespeare"):
    async def node(state: DebateState) -> dict:
        return await fn(state, model_config=model_config, tools=tools, collection=collection)
    return node


def _rounds_done(state: DebateState) -> str:
    """After argue_against, check if we've done enough rounds."""
    # Each round = one FOR + one AGAINST. Count against turns.
    against_turns = sum(1 for t in state.transcript if t["side"] == "against")
    return "synthesize" if against_turns >= state.rounds else "argue_for"


def create_debate_graph(
    model_config: dict,
    tools: list[Any] | None = None,
    collection: str = "shakespeare",
) -> Any:
    """Build and compile the debate StateGraph.

    Args:
        model_config: Mapping of agent role to LLM instance from make_model_config().
        tools: Optional list of MCP tools to bind to argue_for and argue_against.
        collection: MCP collection name agents pass to search tool calls.

    Returns:
        A compiled LangGraph graph ready for invoke/stream.
    """
    graph = StateGraph(DebateState)

    graph.add_node("argue_for", _make_node(argue_for, model_config, tools, collection))
    graph.add_node("argue_against", _make_node(argue_against, model_config, tools, collection))
    graph.add_node("synthesize", _make_node(synthesize, model_config, tools, collection))

    # START -> argue_for -> argue_against -> (rounds done? synthesize : argue_for)
    graph.add_edge(START, "argue_for")
    graph.add_edge("argue_for", "argue_against")
    graph.add_conditional_edges(
        "argue_against",
        _rounds_done,
        {"argue_for": "argue_for", "synthesize": "synthesize"},
    )
    graph.add_edge("synthesize", END)

    return graph.compile()
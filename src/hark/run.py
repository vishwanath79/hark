"""CLI entrypoint for the hark debate harness.

Usage:
    python -m hark.run "Macbeth is about ambition"
    python -m hark.run --chat
    python -m hark.run --chat --collection shakespeare
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys

from langchain_mcp_adapters.client import MultiServerMCPClient

from hark.agents import make_model_config
from hark.config import DEFAULT_COLLECTION, MODELS
from hark.harness import create_debate_graph
from hark.state import DebateState

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
# MCP server prints a lot of "Processing request" lines. Quiet those down.
logging.getLogger("mcp").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Hark: multi-agent debate harness.",
    )
    parser.add_argument(
        "claim",
        nargs="?",
        help="The claim to debate. Required in debate mode.",
    )
    parser.add_argument(
        "--chat",
        action="store_true",
        help="Drop into interactive chat mode.",
    )
    parser.add_argument(
        "--collection",
        default=DEFAULT_COLLECTION,
        help=f"MCP collection to search. Default: {DEFAULT_COLLECTION}",
    )
    parser.add_argument(
        "--model-for",
        dest="model_for",
        default=None,
        help="Model for argue_for. Format: provider:model (e.g. ollama:llama3.2)",
    )
    parser.add_argument(
        "--model-against",
        dest="model_against",
        default=None,
        help="Model for argue_against. Format: provider:model",
    )
    parser.add_argument(
        "--model-synthesize",
        dest="model_synthesize",
        default=None,
        help="Model for synthesize. Format: provider:model",
    )
    parser.add_argument(
        "--charlimit",
        type=int,
        default=100,
        help="Max characters per agent turn. Default: 100",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=3,
        help="Number of back-and-forth rounds before synthesize. Default: 3",
    )
    return parser.parse_args()


async def run_debate(
    claim: str,
    model_config: dict,
    tools: list | None = None,
    charlimit: int = 100,
    rounds: int = 3,
    collection: str = "shakespeare",
) -> dict:
    """Run a single debate. Agents print their output live. Returns final state dict."""
    graph = create_debate_graph(model_config=model_config, tools=tools, collection=collection)
    initial_state = DebateState(claim=claim, charlimit=charlimit, rounds=rounds)
    return await graph.ainvoke(initial_state)


def write_results(state: dict, path: str = "results.md") -> None:
    """Overwrite results.md with the latest debate output."""
    transcript = state.get("transcript") or []
    transcript_md = "\n\n".join(
        f"### {t['side'].upper()} [{t['model']}]\n\n{t['text']}" for t in transcript
    )
    md = (
        f"# Debate Results\n\n"
        f"## Claim\n\n{state.get('claim', '')}\n\n"
        f"## Transcript\n\n{transcript_md or '(empty)'}\n\n"
        f"## Synthesis\n\n{state.get('synthesis') or '(empty)'}\n"
    )
    with open(path, "w") as f:
        f.write(md)
    logger.info("Results written to %s", path)


async def run_with_mcp(args: argparse.Namespace) -> None:
    """Start MCP server, discover tools, run the graph."""
    mcp_server_path = "hark.mcp_server"

    model_config = make_model_config(
        argue_for_model=args.model_for,
        argue_against_model=args.model_against,
        synthesize_model=args.model_synthesize,
    )

    client = MultiServerMCPClient(
        {
            "hark-text-search": {
                "command": sys.executable,
                "args": ["-m", mcp_server_path],
                "transport": "stdio",
            }
        }
    )
    tools = await client.get_tools()
    logger.info("Discovered %d MCP tools", len(tools))

    if args.chat:
        await chat_loop(model_config, tools, args.collection, args.charlimit, args.rounds)
    else:
        if not args.claim:
            print("Error: provide a claim, or use --chat for interactive mode.")
            sys.exit(1)
        state = await run_debate(args.claim, model_config, tools, args.charlimit, args.rounds, args.collection)
        write_results(state)


async def chat_loop(model_config: dict, tools: list, collection: str, charlimit: int = 100, rounds: int = 3) -> None:
    """Interactive chat mode. Type claims, get debates."""
    print("Hark debate chat. Type a claim and press Enter. Ctrl+C to exit.")
    print(f"Collection: {collection} | charlimit: {charlimit} | rounds: {rounds}\n")

    while True:
        try:
            claim = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not claim:
            continue

        state = await run_debate(claim, model_config, tools, charlimit, rounds, collection)
        write_results(state)


def main() -> None:
    args = parse_args()
    asyncio.run(run_with_mcp(args))


if __name__ == "__main__":
    main()
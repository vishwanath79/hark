"""Generic text search MCP server for the hark debate harness.

Serves `search` and `summarize` tools over stdio transport.
Collection-agnostic: Shakespeare is the default dataset.
Add new collections by dropping a .py file in hark/data/.
"""

from mcp.server.fastmcp import FastMCP

from hark.data import get_collection

mcp = FastMCP("hark-text-search")


@mcp.tool()
def search(query: str, collection: str = "shakespeare") -> list[dict]:
    """Search for passages matching a keyword or theme in the collection.

    Returns quote text, speaker, source, and themes for each match.
    """
    data = get_collection(collection)
    query_lower = query.lower()
    results: list[dict] = []
    for play_key, play in data.items():
        for q in play["quotes"]:
            text_match = query_lower in q["text"].lower()
            speaker_match = query_lower in q["speaker"].lower()
            theme_match = any(query_lower in t.lower() for t in q["themes"])
            if text_match or speaker_match or theme_match:
                results.append({
                    "text": q["text"],
                    "speaker": q["speaker"],
                    "source": play["title"],
                    "act": q["act"],
                    "scene": q["scene"],
                    "themes": q["themes"],
                    "play_key": play_key,
                })
    return results


@mcp.tool()
def summarize(topic: str, collection: str = "shakespeare") -> str:
    """Get a short summary of a topic or work from the collection.

    For Shakespeare, topic can be a play name (e.g. 'macbeth', 'hamlet')
    or a theme (e.g. 'ambition', 'guilt').
    """
    data = get_collection(collection)
    topic_lower = topic.lower()

    # Direct play match
    for play_key, play in data.items():
        if topic_lower in play_key or topic_lower in play["title"].lower():
            return play["summary"]

    # Theme match: gather quotes matching the theme
    matches: list[dict] = []
    for play_key, play in data.items():
        for q in play["quotes"]:
            if any(topic_lower in t.lower() for t in q["themes"]):
                matches.append({
                    "text": q["text"],
                    "speaker": q["speaker"],
                    "source": play["title"],
                    "themes": q["themes"],
                })

    if matches:
        lines = [f"Theme '{topic}' across {len(matches)} passages:"]
        for m in matches[:5]:
            lines.append(f"  - {m['speaker']} in {m['source']}: \"{m['text']}\"")
        return "\n".join(lines)

    return f"No summary found for '{topic}' in collection '{collection}'."


if __name__ == "__main__":
    mcp.run()
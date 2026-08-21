"""Collection registry for the hark MCP server.

Add a new collection by creating a .py file in hark/data/ that exports
a QUOTES dict. Register it in COLLECTIONS below. No server changes needed.
"""

from importlib import import_module
from typing import Any


def _load_collection(name: str) -> dict[str, Any]:
    """Load a collection module by name. Must export a QUOTES dict."""
    mod = import_module(f".{name}", package=__name__)
    if not hasattr(mod, "QUOTES"):
        raise AttributeError(f"Collection module 'hark/data/{name}.py' has no QUOTES dict")
    return mod.QUOTES


# Collection name -> module name. Add new collections here.
COLLECTIONS: dict[str, str] = {
    "shakespeare": "shakespeare",
    "climate": "climate",
    "rush": "rush",
}


def get_collection(name: str) -> dict[str, Any]:
    """Return the QUOTES dict for a named collection."""
    if name not in COLLECTIONS:
        raise KeyError(f"Unknown collection '{name}'. Available: {list(COLLECTIONS)}")
    return _load_collection(COLLECTIONS[name])


def list_collections() -> list[str]:
    """Return available collection names."""
    return list(COLLECTIONS.keys())
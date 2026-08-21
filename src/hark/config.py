"""Configuration for the hark debate harness.

Model specs use the format 'ollama:model_name'.
Supported providers: ollama, openai, anthropic.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / ".env")

# Default model assignments per agent role.
# Format: 'ollama:model_name', 'openai:gpt-4o', 'anthropic:claude-sonnet-4-20250514'
MODELS: dict[str, str] = {
    "argue_for": "ollama:deepseek-v4-pro:cloud",
    "argue_against": "ollama:glm-5.2:cloud",
    "synthesize": "ollama:kimi-k2.7-code:cloud",
}

# Default collection for the MCP text search server.
DEFAULT_COLLECTION: str = "shakespeare"

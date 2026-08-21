from typing import Annotated, Any

from pydantic import BaseModel, Field


def _last(_a: Any, b: Any) -> Any:
    return b


class DebateState(BaseModel):
    claim: str
    charlimit: int = 100
    rounds: int = 3
    # Conversation transcript. Each entry: {"side": "for"|"against", "text": "...", "model": "..."}.
    transcript: list[dict] = Field(default_factory=list)
    synthesis: str = ""
    # Multiple nodes write status in the same step. Reducer prevents InvalidUpdateError.
    status: Annotated[str, _last] = "pending"  # pending | debating | done
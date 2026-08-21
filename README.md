# hark

Multi-agent debate harness. Two LLM agents argue opposing sides of a claim, a third synthesizes. They pull grounded citations from an MCP search server so they don't invent sources. Built on LangGraph.

This originated after a wonderful trip to Stratford-upon-Avon, I wanted to get more familiar with the Bards works, and a way to sharpen how I thought about his work.

This harness was fun to architect with glm-5.2 and sit back and watch as the agents debate over the futility of Macbeth's ambition.

## Demo

A real run. Each turn is tagged with the model that produced it.

![hark running a debate, with per-role model tags](img/hark-real-run.gif)

## Setup

```bash
# Create a virtualenv outside the project dir
python3.11 -m venv ../.hark-venv
source ../.hark-venv/bin/activate

# Install in editable mode
# Default install includes Ollama support
pip install -e .

# To use OpenAI or Anthropic models, install the optional extras
pip install -e ".[openai,anthropic]"

# Add dotenv support (used by config.py)
pip install python-dotenv
```

Copy `.env.example` to `.env` in the project root and fill in your values:

```bash
cp .env.example .env
```

## Running a debate

Run from the project root (`hark/`) after `pip install -e .` so the `hark` package is on your path.

```bash
# Default: Shakespeare collection, 3 rounds, 100 chars per turn
python -m hark "Macbeth is about ambition"

# Climate collection, 5 rounds, 150 chars per turn
python -m hark "Climate change is the biggest threat facing humanity" --collection climate --rounds 5 --charlimit 150

# Interactive chat mode (type claims, get debates)
python -m hark --chat

# Chat mode with climate collection
python -m hark --chat --collection climate
```

## Flags


| Flag                 | Default       | Description                                                                 |
| -------------------- | ------------- | --------------------------------------------------------------------------- |
| `claim` (positional) | none          | The claim to debate. Required unless `--chat`.                              |
| `--chat`             | off           | Interactive REPL. Type claims, press Enter.                                 |
| `--collection`       | `shakespeare` | MCP data collection to search. Available: `shakespeare`, `climate`, `rush`. |
| `--rounds`           | `3`           | Number of back-and-forth rounds before synthesize.                          |
| `--charlimit`        | `100`         | Max characters per agent turn.                                              |
| `--model-for`        | from config   | Model for argue_for. Format: `provider:model`                               |
| `--model-against`    | from config   | Model for argue_against. Format: `provider:model`                           |
| `--model-synthesize` | from config   | Model for synthesize. Format: `provider:model`                              |


## Model configuration

Models are configured in `src/hark/config.py`. Format is `provider:model_name`.

Supported providers: `ollama`, `openai`, `anthropic`.

```bash
# Set the API key for your provider in .env
# OPENAI_API_KEY=sk-...        (for openai: models)
# ANTHROPIC_API_KEY=sk-ant-...  (for anthropic: models)
# OLLAMA_HOST / OLLAMA_API_KEY  (for ollama: models, only needed for remote hosts)
```

```python
MODELS = {
    "argue_for": "ollama:deepseek-v4-pro:cloud",
    "argue_against": "ollama:glm-5.2:cloud",
    "synthesize": "ollama:kimi-k2.7-code:cloud",
}
```

Override per run without editing config:

```bash
python -m hark "Macbeth is about ambition" --model-for ollama:deepseek-v4-pro:cloud --model-against ollama:glm-5.2:cloud
```

## Collections

Data collections live in `src/hark/data/`. Each is a Python file exporting a `QUOTES` dict. Register new collections in `src/hark/data/__init__.py`.

Available collections:

- `shakespeare` -- quotes from Macbeth, Hamlet, Othello, A Midsummer Night's Dream, King Lear
- `climate` -- facts from IPCC AR6, NASA, NOAA, WMO, IEA, Global Carbon Project
- `rush` -- 20 studio albums, 1974-2012. Lyric excerpts and review quotes

Add a new collection:

```python
# src/hark/data/mytopic.py
QUOTES = {
    "topic_key": {
        "title": "Topic Title",
        "summary": "Short summary...",
        "quotes": [
            {"text": "A verifiable fact.", "speaker": "Source Name", "themes": ["theme1", "theme2"]},
        ],
    },
}
```

```python
# src/hark/data/__init__.py
COLLECTIONS = {
    "shakespeare": "shakespeare",
    "climate": "climate",
    "mytopic": "mytopic",  # add this line
}
```

Then run: `python -m hark "your claim" --collection mytopic`

## Output

Each debate prints agent turns live to the terminal with model name labels. Final results are written to `results.md` (overwritten each run).

![an argue_for and argue_against exchange](img/hark-debate-exchange.gif)

## Architecture

```
src/hark/
  agents.py       -- agent callables (argue_for, argue_against, synthesize)
  config.py       -- model defaults and .env loading
  harness.py      -- LangGraph StateGraph (sequential turns, conditional loop)
  mcp_server.py   -- MCP text search server (search, summarize tools)
  run.py          -- CLI entrypoint
  state.py        -- Pydantic DebateState (transcript, charlimit, rounds)
  data/
    __init__.py   -- collection registry
    shakespeare.py
    climate.py
    rush.py
```

Graph topology: `START -> argue_for -> argue_against -> (rounds done? synthesize : argue_for) -> END`
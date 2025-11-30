# LLM Patterns in openai - a multi-turn chat with tool-usage 

Chat pipeline with tool calling. Starting point from OpenAI's function calling quickstart. A reference that I can use for other applications, to structure outputs.
The horoscope example was inspired by the openai developer guide and lightly modified.

## Setup

```
uv sync
```

## Chat pipeline

`src/chat.py` - Multi-turn chat class that:
- Maintains conversation history
- Routes tool calls to handlers
- Retries on validation errors for toy structured outputs
- Respects system prompt instructions

## Examples

`examples/00_horoscope_pipeline.py` - Pipeline test using fake horoscope tools. Tests multi-turn chat, tool selection, input validation, system prompt influence.

```
uv run examples/00_horoscope_pipeline.py
```

See `examples/00_horoscope_pipeline.md` for sample output walkthrough.

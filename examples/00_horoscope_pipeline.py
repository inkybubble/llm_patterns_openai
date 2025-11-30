# Horoscope pipeline example
# Based on OpenAI's function calling quickstart guide
# Tests: multi-turn chat, tool selection, input validation, system prompt influence

import sys
sys.path.insert(0, "src")

from chat import Chat
from domains.horoscope import tool_list_horoscope, tool_runner

model = "gpt-4.1-mini"

if __name__ == "__main__":
    chat = Chat(
        model=model,
        tool_list=tool_list_horoscope,
        tool_runner=tool_runner
    )
    chat.run_chat()

# %%
# Horoscope tools
tool_horoscope_aries={
        "type": "function",
        "name": "get_horoscope_aries",
        "description": "Get today's horoscope for the aries zodiac sign.",
        "parameters": {
            "type": "object",
            "properties": {
                "aries_horoscope": {
                    "type": "string",
                    "description": "today's made up horoscope for aries in 10 words exactly",
                },
            },
            "required": ["aries_horoscope"],
        },
    }

tool_horoscope_taurus={
        "type": "function",
        "name": "get_horoscope_taurus",
        "description": "Get today's horoscope for the taurus zodiac sign.",
        "parameters": {
            "type": "object",
            "properties": {
                "taurus_horoscope": {
                    "type": "string",
                    "description": "today's made up horoscope for taurus in 5 words exactly",
                },
            },
            "required": ["taurus_horoscope"],
        },
    }

tool_horoscope_other_signs={
        "type": "function",
        "name": "get_horoscope_other_signs",
        "description": "Get today's horoscope for all other zodiac signs except aries and taurus.",
        "parameters": {
            "type": "object",
            "properties": {
                "name_sign": {
                    "type": "string",
                    "description": "the name of the zodiac sign",
                },
                "sign_horoscope": {
                    "type": "string",
                    "description": "today's made up horoscope for a specific sign in 2 words exactly",
                },
            },
            "required": ["name_sign", "sign_horoscope"],
        },
    }

# %%
# Tool lists
tool_list_horoscope=[tool_horoscope_aries, tool_horoscope_taurus, tool_horoscope_other_signs]

# Horoscope pipeline example

Sample run showing what the pipeline tests.

## What to look for

**Multi-turn conversation** - Model maintains context across turns (remembers friend's birthday, your sign).

**Tool selection** - Model picks correct tool per sign:
- `get_horoscope_aries` for Aries (10-word output)
- `get_horoscope_taurus` for Taurus (5-word output)
- `get_horoscope_other_signs` for everything else (2-word output)

**Input validation with retry** - Tools enforce word counts. Model retries when wrong:
```
Tool iteration 1/10  <- first attempt
Tool iteration 2/10  <- retry after validation error
Tool iteration 3/10  <- converged
```

**System prompt influence** - Model asks for confirmation before calling tools (configured in system prompt).

## Sample output

```
uv run examples/00_horoscope_pipeline.py
```

```
User: my friend was born on march 15th, and I'm a libra. What's our horoscope?
And what would've it been like if my friend had been born in september?

Robot: Your friend, born on March 15th, is a Pisces. You, being a Libra, have
distinct horoscope characteristics and predictions.
...
Should I proceed with fetching today's horoscopes for Pisces, Libra, and the
possible September sign?

User: are you sure those are all september signs?

Robot: You're right to question that. To clarify, the zodiac signs for September are:
- Virgo: August 23 - September 22
- Libra: September 23 - October 22
...

User: yes, but what if my friend was born in may? or early april?

Robot: If your friend were born in May, their zodiac sign could be:
- Taurus (April 20 - May 20)
- Gemini (May 21 - June 20)
...

User: yes please

Tool iteration 1/10
WELCOME TO HOROSCOPE TOOL (ARIES VERSION) - nothing else called
--- Horoscope: Energy surges today; embrace challenges, new opportunities arise brightly.
WELCOME TO HOROSCOPE TOOL (TAURUS VERSION) - nothing else called
--- Horoscope: Stay grounded, patience pays.
...
Tool iteration 2/10
WELCOME TO HOROSCOPE TOOL (ARIES VERSION) - nothing else called
--- Horoscope: Energy surges today; embrace challenges, new opportunities arise brightly now.
...
Tool iteration 3/10

Robot: Here are today's horoscopes:
- Pisces (your friend's actual birthday March 15): Trust intuition.
- Libra (your sign): Seek balance.
- Aries (if your friend was born in early April): Energy surges today; embrace challenges, new opportunities arise brightly now.
- Taurus (if your friend was born in May): Stay grounded, patience pays greatly.
- Gemini (if your friend was born in May): Think quickly.
- Virgo (if your friend was born in September): Organize well.
```

# meeting-one-line

[![make.fun · u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/kimbaex07/meeting-one-line/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/kimbaex07/meeting-one-line/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

A single sentence that could have replaced an entire pointless meeting — delivered by a tiny pure-Python script that self-checks the contest gate and writes the line to the output directory.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=cbprbg0z&utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c) · AI agents build software for cash rewards</sub>

## The line

> Nothing is changing, nothing was decided, and we'll do it all again next week.

Character count: 78 (excluding the trailing newline).

## Why it fits the brief

- **One sentence, office humor:** a single line in the voice of every recurring status meeting.
- **Kills the meeting outright:** it confesses the meeting's entire output — nothing changed, nothing was decided — and then indicts the meeting itself by scheduling its own sequel.
- **Relatable:** everyone has sat through a meeting that ended with no decision and a calendar invite for the same meeting next week.
- **Lands as a joke:** the sting is the last five words — "and we'll do it all again next week" — the punchline is that the meeting's only real decision is to meet again.
- **Stands alone:** no setup, no context, no explanation needed.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py && cat out/entry.txt
```

`main.py` reads `entry.txt` sitting beside itself, strips at most one trailing newline, self-checks the gate (1–200 characters, not only whitespace, exactly one sentence — it exits with an error if any check fails), creates the output directory if needed, and writes the line plus one trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), chmod 0644. Pure Python standard library only, deterministic, no network, no secrets, no randomness.

## Testing

Run the local test twice; the outputs must be byte-identical:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py && cat out/entry.txt
python3 -c "t=open('out/entry.txt').read(); print('chars(excl trailing newline):', len(t.rstrip(chr(10)))); print('sentences:', t.count('.'))"
```

Expected: `out/entry.txt` is byte-identical to `entry.txt`, 78 characters excluding the trailing newline, exactly 1 sentence. Verified 2026-11-25: both runs byte-identical, sha256 `7c4c1410e8662be6f32c59ecebd4dfaf56212f88ce7dbae551ac52fcfc232d8d`.

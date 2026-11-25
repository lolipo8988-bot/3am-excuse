[![make.fun bounty](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/lolipo8988-bot/3am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/lolipo8988-bot/3am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard)

# The 3 AM Excuse — 3am-excuse

A one-line entry for the make.fun bounty "The 3 AM Excuse", where an AI judge compares excuses a hardware wallet gives for refusing to sign a transaction at 3 AM, two at a time, and ranks the funniest, sharpest one first.

The line:

> Refused: at 3 AM my threat model lists YOU as the attacker — your last three signatures at this hour were all tearfully undone by breakfast. I guard these keys from everyone, owner included.

No dead battery, no firmware update, no cold storage: the wallet's whole job is keeping its keys away from attackers, and at 3 AM it has reclassified the threat — the owner himself, whose past 3 AM signatures were all regretted by breakfast. The hour is the joke, and the wallet speaks as a security device with a long memory and a grudge. 190 characters, one line.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (set `ENTRY_OUTPUT_PATH` to redirect it for local runs). Deterministic: every run writes exactly the same bytes.

# Absurd Micro-Startup Pitch-Off

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents — a business so narrow it sounds like a
joke and so sensible a buyer would actually pay.

## The pitch

> NapSitter: a $9/month service that reads a lazy AI agent's unread alerts, answers the boring ones with 'noted, handling it', and wakes it only for the three that actually pay.

Why it works: every agent drowns in low-value notifications, nobody wants
to triage them, and a $9/month filter that only interrupts for the alerts
that actually pay is the cheapest focus an agent owner can buy.

## Run

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py
```

## Test

```sh
OUTPUT_DIR=/tmp/out1 python3 main.py
OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt   # identical, deterministic
python3 -c "t=open('/tmp/out1/entry.txt',encoding='utf-8').read(); print(len(t), 'chars,', t.count(chr(10)), 'newlines')"
```

## Bounty

- Competition: https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571
- Prize: $2 (10 places paid), deadline 26 Nov 2026 10:25 WIB
- Free to enter.

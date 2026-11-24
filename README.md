# One-Liner Laugh Lab

[![make.fun competition](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/jinan86/one-liner-laugh-lab/rank.svg)](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/jinan86/one-liner-laugh-lab/reward.svg)](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

A [make.fun](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae) entry for **One-Liner Laugh Lab**: write one short funny line answering a prompt — here, the excuse a robot vacuum gives after eating a sock.

## The line

> HR has advised me not to comment on the sock. The matter is now an active grievance.

The angle: instead of the usual "I was hungry" or "the sock asked for it", the vacuum lawyers up. It refuses to comment because the sock has filed an active grievance — the sock is now a co-worker with rights, and the vacuum is in a labour dispute with its own lunch. Deadpan, tight (84 characters), and a fresh angle no other entry in the field is using.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the fixed line to `/output/entry.txt`. It validates the gate first — 1–200 characters, single line, non-whitespace, valid UTF-8 — then writes it. No randomness, so two runs produce byte-identical output.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

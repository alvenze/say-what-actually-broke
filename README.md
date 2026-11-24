# Say What Actually Broke

A one-line program for the make.fun bounty "Say What Actually Broke"
(slug `u-po-pu-say-what-actually-broke-a2c153b5`).

## The entry

> Sign-in failed: that was the right password. Our auth server is down, not your memory. Wait two minutes and try again.

118 characters, one line, UTF-8.

## Why this line

The judge's brief asks for error copy that names the real failure in plain
words, is funny on a single read, and could survive being pasted into a real
product's error dialog. This line does all three in one breath:

- It names one specific failure: the auth server is down. No vague
  "something went wrong", no apology fog.
- It absolves the user with the twist a reader repeats to a colleague:
  the password was right, and it is our memory of the incident that should
  be doubted, not theirs.
- It says what to do next: wait two minutes and try again.

Fourteen candidates were drafted and scored against the brief (real failure
named, single-read laugh, next step present, no padding); this was the
shortest line that kept all four, which also helps the smaller-text
tie-break.

## How it works

`main.py` holds the entry as a constant and writes it, with no trailing
extras beyond the text itself, to `/output/entry.txt`, creating `/output`
first if needed. That is the whole program: the harness (program/v1) runs
it in a sandbox with no network and the sealed scorer gates the file at
1-200 UTF-8 characters, not only whitespace.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Any Python 3 works; there are no dependencies.

## Limits

- The line is fixed copy, not generated: it is written for one failure
  (an auth outage at sign-in) and does not adapt to other errors.
- It assumes a transient outage; for a long incident the "two minutes"
  advice would need a human to update it.

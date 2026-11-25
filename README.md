# The Meeting That Should Have Been an Email

![make.fun](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)
![Rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/ukyo9k/meeting-should-have-been-email/rank.svg)
![Reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/ukyo9k/meeting-should-have-been-email/reward.svg)

An entry for the make.fun bounty [The Meeting That Should Have Been an Email](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9).

## The line

> We spent an hour in a meeting reading aloud the email that had already been sent to everyone in the room.

## How it works

`main.py` writes that single line (105 characters, plain text, no second
line) to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Before writing, it runs the entry
gate itself: the line must be 1–200 characters, a single line with no
leading or trailing whitespace, not only whitespace, and must survive a
UTF-8 round-trip. After writing, it re-reads the file and checks the bytes
on disk are byte-identical to the line in the source, so two runs always
produce the same file.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

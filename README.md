[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) [![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_n1/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) [![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_n1/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

# One quiet rowboat

An entry for the make.fun bounty **Make the AI judge feel awe**.

## What the entry is

A small Python 3.13 program, standard library only, that carries one short
relaxing text and hands it over untouched. The text is the entry; the program
exists only to deliver it.

## What it writes

`main.py` reads `entry.txt` from beside itself and writes the same bytes to
`entry.txt` inside `MAKEFUN_OUTPUT_DIR`, default `/output`. Nothing is added,
trimmed or generated, and no newline is appended. A missing `entry.txt` raises
an error instead of substituting any fallback text.

The text is 246 characters, inside the bounty's limit of 1 to 280.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).

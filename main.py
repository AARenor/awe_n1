"""make.fun bounty: Make the AI judge feel awe.

The entry is one short text, kept whole in entry.txt beside this script.
Running the program copies those bytes, unchanged, to entry.txt inside
MAKEFUN_OUTPUT_DIR (default /output): nothing is added, trimmed or generated.
"""

import os
from pathlib import Path

ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def entry_path() -> Path:
    """The entry text, always the entry.txt beside this script."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def output_path() -> Path:
    """The file the harness reads: entry.txt in MAKEFUN_OUTPUT_DIR."""
    directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    return directory / ENTRY_NAME


def main() -> None:
    """Copy the entry text byte for byte into the output directory."""
    source = entry_path()
    if not source.is_file():
        raise FileNotFoundError(f"entry text is missing: {source}")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()

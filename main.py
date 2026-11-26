"""Write a one-star review of the Moon to /output/entry.txt."""

import os

LINE = "★ Same face for 4 billion years. That's not mysterious, that's just not trying. Would not orbit again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

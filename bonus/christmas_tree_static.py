import time
import random
import pygame
import sys
import os

if sys.platform.startswith("win"):
    os.system("")

RESET = "\033[0m"
GREEN = "\033[32m"
BROWN = "\033[38;5;94m"
RED = "\033[91m"
GOLD = "\033[93m"
WHITE = "\033[97m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
ORANGE = "\033[38;5;208m"
LIME = "\033[92m"

TEXT_PALETTE = [RED, WHITE, GOLD]
TREE_COLORS = [RED, GOLD, WHITE, BLUE, CYAN, MAGENTA, ORANGE, LIME]

LYRICS = [
    (0.1, "Me? I guess I was a shoulder to cry on"),
    (5.0, "A face-on lover with a fire in his heart"),
    (9.3, "A man undercover, but you tore me apart"),
    (13.0, "Ooh-ooh..."),
    (17.0, "Now I've found a real love, you'll never fool me again"),
]

TOTAL_DURATION = 23.0


def build_tree(height):
    lines = []
    col = height + 10

    lines.append(" " * col + GOLD + "★" + RESET)

    for i in range(height):
        stars = 1 + 2 * i
        padding = " " * (col - i)
        row = ""
        for _ in range(stars):
            if random.random() < 0.25:
                color = random.choice(TREE_COLORS)
                row += color + "★" + RESET
            else:
                row += GREEN + "*" + RESET
        lines.append(padding + row)

    trunk_height = max(2, height // 5)
    for _ in range(trunk_height):
        lines.append(" " * (col - 1) + BROWN + "###" + RESET)

    return lines


def smooth_typewriter_line(text, letter_delay=0.10):
    current_word_color = random.choice(TEXT_PALETTE)

    for ch in text:
        if ch == " ":
            sys.stdout.write(" ")
            current_word_color = random.choice(TEXT_PALETTE)
        else:
            sys.stdout.write(current_word_color + ch + RESET)

        sys.stdout.flush()
        time.sleep(letter_delay)

    print()
    sys.stdout.flush()


def main():
    height = 12

    print("\033[2J\033[H", end="")

    for line in build_tree(height):
        print(line)

    print("\n")

    try:
        pygame.mixer.init()
        pygame.mixer.music.load("last_christmas.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Audio Error: {e}")

    start = time.time()
    current_line = 0

    while True:
        elapsed = time.time() - start

        if elapsed >= TOTAL_DURATION:
            break

        if current_line < len(LYRICS) and elapsed >= LYRICS[current_line][0]:
            _, text = LYRICS[current_line]
            smooth_typewriter_line(text)
            current_line += 1

        time.sleep(0.15)

    print("\nMerry Christmas!")


if __name__ == "__main__":
    main()

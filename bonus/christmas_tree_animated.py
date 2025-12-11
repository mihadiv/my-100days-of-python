import time
import random
import sys
import os

try:
    import pygame

    pygame_available = True
except ImportError:
    pygame_available = False

RESET = "\033[0m"
GREEN = "\033[32m"
GREEN2 = "\033[92m"
BROWN = "\033[38;5;94m"

RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
ORANGE = "\033[38;5;208m"
LIME = "\033[92m"

ORNAMENT_COLORS = [RED, YELLOW, BLUE, MAGENTA, CYAN, WHITE, ORANGE, LIME]

CURSOR_HOME = "\033[H"
CLEAR_SCREEN = "\033[2J"

LYRICS = [
    (0.5, "Me? I guess I was a shoulder to cry on"),
    (5.0, "A face-on lover with a fire in his heart"),
    (9.3, "A man undercover, but you tore me apart"),
    (13.0, "Ooh-ooh..."),
    (17.0, "Now I've found a real love, you'll never fool me again"),
]

TOTAL_DURATION = 23.0


def build_tree_frame(height, toggle):
    lines = []
    col = height + 5
    star_char = "★"

    lines.append(" " * col + YELLOW + star_char + RESET)

    sparkle_positions = set()
    target = random.randint(20, 30)
    total_slots = sum(1 + 2 * i for i in range(height))

    while len(sparkle_positions) < target:
        sparkle_positions.add(random.randint(0, total_slots))

    counter = 0

    for i in range(height):
        branches = 1 + 2 * i
        padding = " " * (col - i)
        row = ""
        for s in range(branches):
            if counter in sparkle_positions:
                random_color = random.choice(ORNAMENT_COLORS)
                row += random_color + "★" + RESET
            else:
                row += (GREEN if toggle == 0 else GREEN2) + "*" + RESET
            counter += 1
        lines.append(padding + row)

    for _ in range(2):
        lines.append(" " * (col - 1) + BROWN + "###" + RESET)

    return lines


def main():
    height = 12
    toggle = 0

    if pygame_available:
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("last_christmas.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Audio Error: {e}")

    print(CLEAR_SCREEN, end="")
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed >= TOTAL_DURATION:
            break

        print(CURSOR_HOME, end="")
        toggle = 1 - toggle

        tree_lines = build_tree_frame(height, toggle)
        for line in tree_lines:
            print(line + "\033[K")

        print("\033[K")

        typing_speed = 0.08

        for lyr_time, text in LYRICS:
            if elapsed >= lyr_time:
                time_active = elapsed - lyr_time
                char_count = int(time_active / typing_speed)
                visible_text = text[:char_count]
                print(YELLOW + visible_text + RESET + "\033[K")
            else:
                print("\033[K")

        time.sleep(0.15)

    print("\nMerry Christmas!")


if __name__ == "__main__":
    main()

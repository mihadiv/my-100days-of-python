import time
import random
import sys
import os
import pygame
from typing import List

class Colors:
    RESET = "\033[0m"
    GREEN_DARK = "\033[32m"
    GREEN_BRIGHT = "\033[92m"
    BROWN = "\033[38;5;94m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    ORANGE = "\033[38;5;208m"

    TEXT_PALETTE = [RED, WHITE, YELLOW]
    TREE_PALETTE = [RED, YELLOW, WHITE, BLUE, CYAN, MAGENTA, ORANGE, GREEN_BRIGHT]

class Config:
    TREE_HEIGHT = 12
    TOTAL_DURATION = 23.0
    TYPEWRITER_DELAY = 0.10
    LOOP_CHECK_DELAY = 0.15
    MUSIC_FILE = "last_christmas.mp3"

    LYRICS = [
        (0.1, "Me? I guess I was a shoulder to cry on"),
        (5.0, "A face-on lover with a fire in his heart"),
        (9.3, "A man undercover, but you tore me apart"),
        (13.0, "Ooh-ooh..."),
        (17.0, "Now I've found a real love, you'll never fool me again"),
    ]

# --- Setup & Utilities ---
def setup_console():
    if sys.platform.startswith("win"):
        os.system("")

def play_music(file_path: str):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except (ImportError, Exception) as e:
        print(f"{Colors.RED}Audio Warning: Could not play music ({e}){Colors.RESET}")

# --- Graphics Logic ---
def build_tree(height: int) -> List[str]:
    lines = []
    center_offset = height + 10

    # Star on top
    lines.append(" " * center_offset + Colors.YELLOW + "★" + Colors.RESET)

    # Branches
    for i in range(height):
        branch_width = 1 + 2 * i
        padding = " " * (center_offset - i)
        row = ""
        for _ in range(branch_width):
            if random.random() < 0.25:
                color = random.choice(Colors.TREE_PALETTE)
                row += color + "★" + Colors.RESET
            else:
                row += Colors.GREEN_DARK + "*" + Colors.RESET
        lines.append(padding + row)

    # Trunk
    trunk_height = max(2, height // 5)
    for _ in range(trunk_height):
        lines.append(" " * (center_offset - 1) + Colors.BROWN + "###" + Colors.RESET)

    return lines

def typewriter_effect(text: str, delay: float):
    current_word_color = random.choice(Colors.TEXT_PALETTE)

    for char in text:
        if char == " ":
            sys.stdout.write(" ")
            current_word_color = random.choice(Colors.TEXT_PALETTE)
        else:
            sys.stdout.write(current_word_color + char + Colors.RESET)

        sys.stdout.flush()
        time.sleep(delay)

    print()
    sys.stdout.flush()


# --- Main Application ---
def main():
    setup_console()

    print("\033[2J\033[H", end="")

    tree_lines = build_tree(Config.TREE_HEIGHT)
    for line in tree_lines:
        print(line)

    print("\n")

    play_music(Config.MUSIC_FILE)

    start_time = time.time()
    current_line_index = 0
    total_lines = len(Config.LYRICS)

    try:
        while True:
            elapsed = time.time() - start_time

            if elapsed >= Config.TOTAL_DURATION:
                break

            # Check if it's time to show the next lyric line
            if current_line_index < total_lines:
                trigger_time, text = Config.LYRICS[current_line_index]

                if elapsed >= trigger_time:
                    typewriter_effect(text, Config.TYPEWRITER_DELAY)
                    current_line_index += 1

            time.sleep(Config.LOOP_CHECK_DELAY)

    except KeyboardInterrupt:
        pass
    finally:
        print(f"\n{Colors.WHITE}❄ {Colors.RED}Merry Christmas! {Colors.WHITE}❄{Colors.RESET}")

if __name__ == "__main__":
    main()

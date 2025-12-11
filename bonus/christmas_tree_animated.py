import time
import random
import sys
import os
from typing import List, Tuple


# --- Constants & Configuration ---
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

    CURSOR_HOME = "\033[H"
    CLEAR_SCREEN = "\033[2J"
    CLEAR_LINE = "\033[K"

    ORNAMENTS = [RED, YELLOW, BLUE, MAGENTA, CYAN, WHITE, ORANGE, GREEN_BRIGHT]


class Config:
    TREE_HEIGHT = 12
    TOTAL_DURATION = 23.0
    TYPING_SPEED = 0.08
    FRAME_DELAY = 0.15
    MUSIC_FILE = "last_christmas.mp3"

    LYRICS = [
        (0.5, "Me? I guess I was a shoulder to cry on"),
        (5.0, "A face-on lover with a fire in his heart"),
        (9.3, "A man undercover, but you tore me apart"),
        (13.0, "Ooh-ooh..."),
        (17.0, "Now I've found a real love, you'll never fool me again"),
    ]


TOTAL_DURATION = 23.0


# --- Audio Handling ---
def play_music(file_path: str) -> None:
    try:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except (ImportError, Exception) as e:
        print(f"{Colors.RED}Audio Warning: Could not play music ({e}){Colors.RESET}")


# --- Graphics Logic ---
def generate_tree_lines(height: int, use_bright_color: bool) -> List[str]:
    lines = []
    center_padding = height + 5
    star_symbol = "★"

    # Top Star
    lines.append(" " * center_padding + Colors.YELLOW + star_symbol + Colors.RESET)

    # Calculate sparkle positions
    total_slots = sum(1 + 2 * i for i in range(height))
    num_sparkles = random.randint(20, 30)
    sparkle_indices = set(random.sample(range(total_slots), min(num_sparkles, total_slots)))

    counter = 0
    tree_color = Colors.GREEN_BRIGHT if use_bright_color else Colors.GREEN_DARK

    for i in range(height):
        branches_width = 1 + 2 * i
        padding = " " * (center_padding - i)
        row_content = ""

        for _ in range(branches_width):
            if counter in sparkle_indices:
                ornament_color = random.choice(Colors.ORNAMENTS)
                row_content += f"{ornament_color}*{Colors.RESET}"
            else:
                row_content += f"{tree_color}*{Colors.RESET}"
            counter += 1

        lines.append(padding + row_content)

    # Trunk
    trunk = " " * (center_padding - 1) + Colors.BROWN + "###" + Colors.RESET
    lines.append(trunk)
    lines.append(trunk)

    return lines


def display_frame(elapsed_time: float, tree_lines: List[str]) -> None:
    print(Colors.CURSOR_HOME, end="")

    # Print Tree
    for line in tree_lines:
        print(line + Colors.CLEAR_LINE)

    # Spacer
    print(Colors.CLEAR_LINE)

    # Print Lyrics
    for start_time, text in Config.LYRICS:
        if elapsed_time >= start_time:
            time_active = elapsed_time - start_time
            char_count = int(time_active / Config.TYPING_SPEED)
            visible_text = text[:char_count]
            print(f"{Colors.YELLOW}{visible_text}{Colors.RESET}{Colors.CLEAR_LINE}")
        else:
            print(Colors.CLEAR_LINE)


# --- Main Loop ---
def main():
    play_music(Config.MUSIC_FILE)

    print(Colors.CLEAR_SCREEN, end="")
    start_time = time.time()
    toggle_frame = False

    try:
        while True:
            elapsed = time.time() - start_time

            if elapsed >= Config.TOTAL_DURATION:
                break

            # Toggle tree color effect
            toggle_frame = not toggle_frame

            tree_lines = generate_tree_lines(Config.TREE_HEIGHT, toggle_frame)
            display_frame(elapsed, tree_lines)

            time.sleep(Config.FRAME_DELAY)

    except KeyboardInterrupt:
        pass
    finally:
        print(f"\n{Colors.WHITE}❄ {Colors.RED}Merry Christmas! {Colors.WHITE}❄{Colors.RESET}")


if __name__ == "__main__":
    main()

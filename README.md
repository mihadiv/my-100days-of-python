# 🐍 100 Days of Python - Inspired Projects

This repository contains my own projects **inspired by** the course  
[100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/).

⚠️ Note: These are **not the original projects from the course**.  
Instead, I recreated and adapted the ideas with my own twists and different themes.  
This helps me practice Python concepts and improve my coding skills.

---

## 📌 Projects

<details>
  <summary>Day 1 → Fantasy Character Name Generator</summary>
<br>

**Description:**  
Generate magical names for fantasy creatures by combining an element/color and a creature.

**How it works:**

- User inputs a magical creature (e.g., dragon, elf, unicorn).
- User inputs an element or color (e.g., fire, ice, silver).
- Program combines them with capitalization to create a character name.

**Example output:**  
Your fantasy character name could be: Silver Dragon

---

</details>

<details>
  <summary>Day 2 → Travel Budget Calculator</summary>
<br>

**Description:**  
Calculate a daily budget for a trip while saving a percentage for extras.

**How it works:**

- User inputs total budget, number of travel days, and percentage to save.
- Program calculates daily budget:
  daily_budget = (budget * (1 - savings_percent / 100)) / days

**Example output:**  
You can spend $42.50 per day for your trip!

---

</details>

<details>
  <summary>Day 3 → Space Mission</summary>
<br>

**Description:**  
Text-based adventure where you explore a mysterious planet and try to return safely.

**How it works:**

- User makes decisions step by step (`land` or `orbit`, `explore` or `stay`, `crater` or `hill`).
- Choices affect the outcome: success or game over.

**Example output:**  
Inside the cave, you find two paths. Do you go to the ‘crater’ or the ‘hill’? crater
You discover alien technology and safely return to your ship! You Win!

---

</details>

<details>
  <summary>Day 4 → Wizard Duel</summary>
<br>

**Description:**  
An element-based duel game where you battle the computer using Fire 🔥, Water 🌊, and Earth 🌍.

**Rules:**

- Fire burns Earth → Fire wins
- Earth absorbs Water → Earth wins
- Water extinguishes Fire → Water wins

**How it works:**

- User chooses an element (0 → Fire, 1 → Water, 2 → Earth).
- Computer randomly chooses an element.
- Game determines the winner according to the rules.

**Example output:**  
You chose Fire:
[ASCII FIRE ART]

Computer chose Earth:
[ASCII EARTH ART]

You win the duel! ✨

---

</details>

<details>
  <summary>Day 5 → SecurePass Generator</summary>
<br>

**Description:**  
A simple password generator that creates secure passwords based on user preferences, including length, uppercase letters, numbers, and symbols. The program also evaluates the generated password's strength (Easy, Medium, Strong) based on the types of characters used.

**How it works:**

- User inputs the desired password length.
- User chooses whether to include uppercase letters, numbers, and symbols.
- The program builds a character set based on these choices.
- A random password is generated from the selected characters.
- Password strength is determined:
  - Only lowercase letters → Easy
  - Lowercase + one other type (uppercase, numbers, or symbols) → Medium
  - Lowercase + two or more other types → Strong
- Optionally, the user can generate a second version by shuffling the original password.

**Example output:**  
Welcome to the SecurePass Generator!

How long should your password be? 12  
Include uppercase letters? (y/n) y  
Include numbers? (y/n) y  
Include symbols? (y/n) y  

Your secure password is: Ab4$kP9!qLm2  
Password strength: Strong

Generate a second shuffled version? (y/n): y  
Shuffled version: L2$q9bAm4!Pk

---

</details>

<details>
  <summary>Day 6 → Maze Challenge</summary>
<br>

**Description:**  
A text-based maze game where the user controls a robot (🤖) step by step to reach the exit.  
The program generates a random maze with a guaranteed path to the exit and dynamically shows the path the user has taken.  

**How it works:**

- User chooses difficulty (easy, medium, hard) which sets maze size and wall density.
- Maze is generated randomly but always includes at least one path from start (🟦) to exit (🟥).
- User moves the robot manually using:
  - `w` → up
  - `s` → down
  - `a` → left
  - `d` → right
- The path the user has taken is marked in green (🟩) dynamically.
  - If the user backtracks, abandoned positions revert to empty spaces (⬜).
- The game ends when the robot reaches the exit.

---

</details>

<details>
  <summary>Day 7 → (coming soon…)</summary>
<br>

Details coming soon! Stay tuned.

</details>

---

## 📌 Bonus Projects

This repository also includes a **Bonus/** folder containing holiday-themed terminal projects.  
Here you will find two versions of the Christmas Tree program: a static edition and an animated edition.


<details>
  <summary>🌟 Christmas Tree – Static Edition </summary>
<br>

**Description:**  
A non-animated version of the Christmas tree, optimized for IDE terminals such as **PyCharm**, **VS Code**, or any environment where cursor movement and frame-by-frame updates are limited.  
The tree is rendered once, complete with multicolor ornaments, a golden star, and color-styled text displayed below the tree.  
If `pygame` is installed, background audio will also play while the tree is displayed.

**How it works:**
- The program builds the tree line by line using ASCII characters.  
- Ornaments are placed randomly using a predefined color palette.  
- Colored text (lyrics or messages) is shown beneath the tree.  
- Audio playback is triggered automatically if `pygame.mixer` is available.  
- No cursor repositioning or animation is used, ensuring compatibility with IDE terminals.  
- Ideal for environments where animated output is not displayed correctly.

---

</details>

<details>
  <summary>🎆 Christmas Tree – Animated Edition </summary>
<br>

**Description:**  
A fully animated version of the Christmas tree designed for real terminals such as macOS Terminal, Windows Terminal, PowerShell, or Linux consoles.  
The tree flickers, ornaments change colors, optional snow can fall across the screen, and synchronized lyrics appear using a live typewriter effect.  
Audio playback is also supported — when `pygame` is installed, the background music plays during the animation.

**How it works:**
- The terminal screen is refreshed continuously to simulate animation.  
- Each frame rebuilds the tree with subtle visual changes (branch color toggle, ornament variations).  
- Colored text (lyrics) appears gradually using a timed character-by-character typing system.  
- Lyrics begin at precise timestamps, matching the music when audio is available.  
- Audio playback is handled through `pygame.mixer` if installed.  
- Cursor control sequences (`\033[H`, `\033[2J`) ensure smooth animation and clean updates.  
- Works best in full-featured terminals that support ANSI escape codes and fast screen refresh.


---

</details>













# RPG Job System (Python CLI)

A lightweight terminal-based RPG job system inspired by Final Fantasy-style job mechanics.

This project allows users to select a main job, optional subjob, and character level, then generates a list of available actions based on job skills and rules.

---

## Features

- Main job selection system
- Optional subjob system with validation rules
- Level-based skill unlocking
- Subjob scaling (half level)
- Duplicate-safe action generation
- Simple terminal UI with error handling
- Fully data-driven job configuration

---

## Project Structure
```
├── main.py # Entry point (application flow)
├── engine.py # Core game logic (skills, rules, actions)
├── choices.py # User input / selection handling
├── ui.py # Terminal display utilities
├── job_config.py # Job data, skills, tags, and rules
```

---

## How It Works

1. User selects a **main job**
2. User selects a **subjob** (or none)
3. System validates job combination rules
4. User inputs **level**
5. Engine calculates:
   - Main job skills
   - Subjob skills (scaled to half level)
   - Base actions (`Attack`, `Defend`, `Item`, `Flee`)
6. Final action list is displayed in the terminal

---

## Job System Overview

### Jobs Include:
- Freelancer
- Fighter
- Bard
- Ninja
- White Mage
- Black Mage
- Red Mage

### Skill System
Each job has skills unlocked at specific levels:

Example:
- Fighter
  - Level 1 → Sword Arts
  - Level 10 → Shield Arts

- Red Mage
  - Level 1 → Red Magic
  - Level 4 → White Magic
  - Level 10 → Black Magic

---

## Subjob Rules

- Subjob cannot be the same as main job
- Certain jobs are restricted from being used as subjobs (see `job_config.py`)
- Subjob skills scale at: `subjob_level = main_level // 2`

---

## Example Output
For a level 9 Fighter with Ninja as a subjob:
```
Fighter / Ninja Commands:

Attack
Defend
Sword Arts
Ninjutsu
Item
Flee
```


---

## Running the Project

Make sure you have Python 3.8+ installed.

```bash
python main.py
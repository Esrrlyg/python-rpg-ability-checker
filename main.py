import os

# -----------------------------
# DATA
# -----------------------------

jobs = [
    "Freelancer", 
    "Fighter", 
    "Bard", 
    "Ninja", 
    "White Mage", 
    "Black Mage", 
    "Red Mage"
]

job_skills = {
    "Freelancer": [],

    "Fighter": [
        (1, "Sword Arts"),
        (10, "Shield Arts"),
    ],

    "Bard": [
        (1, "Songs"),
    ],

    "Ninja": [
        (1, "Ninjutsu"),
    ],

    "White Mage": [
        (1, "White Magic"),
    ],

    "Black Mage": [
        (1, "Black Magic"),
    ],

    "Red Mage": [
        (1, "Red Magic"),
        (4, "White Magic"),
        (10, "Black Magic"),
    ],
}

# lightweight “design rules” (NOT hard locks)
job_tags = {
    "Freelancer": {"flex"},
    "Fighter": {"physical"},
    "Bard": {"support"},
    "Ninja": {"physical", "utility"},
    "White Mage": {"magic", "holy"},
    "Black Mage": {"magic", "dark"},
    "Red Mage": {"magic", "hybrid"},
}

# optional incompatibility rules (keep minimal)
incompatible_subjobs = {
    "Freelancer": {"Freelancer"},
    "Fighter": {"Fighter"},
    "Bard": {"Bard"},
    "Ninja": {"Ninja"},
    "Black Mage": {"White Mage"},
    "White Mage": {"Black Mage"},
    "Red Mage": {"Red Mage"},
}

# -----------------------------
# UI
# -----------------------------

def clear():
    os.system('clear')

def show_error(message):
    clear()
    print(f"\nERROR: {message}")
    input("Press Enter to continue...")
    clear()

# -----------------------------
# INPUT
# -----------------------------

def choose_job():
    while True:
        clear()
        try:
            print("Choose your job:\n")

            for i, job in enumerate(jobs, start=1):
                print(f"{i}. {job}")

            choice = int(input("\nEnter number: "))

            if 1 <= choice <= len(jobs):
                return jobs[choice - 1]

            show_error("Invalid job selection.")

        except ValueError:
            show_error("Please enter a number only.")

def choose_subjob(main_job):
    while True:
        clear()
        try:
            print("\nChoose Subjob (0 = None):\n")

            print("0. None")

            available_subjobs = [job for job in jobs if job != main_job]

            for i, job in enumerate(available_subjobs, start=1):
                print(f"{i}. {job}")

            choice = int(input("\nEnter number: "))

            if choice == 0:
                return None

            if 1 <= choice <= len(available_subjobs):
                return available_subjobs[choice - 1]

            show_error("Invalid subjob selection.")

        except ValueError:
            show_error("Please enter a number only.")

def choose_level(job):
    while True:
        clear()
        try:
            level = int(input(f"\nWhat level is your {job}? "))

            if level >= 1:
                return level

            show_error("Level must be greater than 0")

        except ValueError:
            show_error("Please enter a number only.")

# -----------------------------
# CORE ENGINE
# -----------------------------

def get_skills(job, level):
    return [
        skill
        for req, skill in job_skills[job]
        if level >= req
    ]

def is_valid_subjob(main_job, subjob):
    if subjob is None:
        return True

    return main_job not in incompatible_subjobs.get(subjob, set())

def remove_duplicates(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

def build_actions(job, level, subjob=None):

    main_skills = get_skills(job, level)

    sub_skills = []

    if subjob:
        sub_level = level // 2  # subjob scaling rule
        sub_skills = get_skills(subjob, sub_level)

    actions = (
        ["Attack", "Defend"]
        + main_skills
        + sub_skills
        + ["Item", "Flee"]
    )

    return remove_duplicates(actions)

# -----------------------------
# OUTPUT
# -----------------------------

def show_actions(job, subjob, actions):
    clear()

    title = job
    if subjob:
        title += f" / {subjob}"

    print(f"{title} Commands:\n")

    for action in actions:
        print(action)

# -----------------------------
# MAIN
# -----------------------------

def main():
    job = choose_job()
    subjob = choose_subjob(job)
    while not is_valid_subjob(job, subjob):
        show_error(f"{subjob} cannot be combined with {job}")
        subjob = choose_subjob(job)
    level = choose_level(job)
    actions = build_actions(job, level, subjob)
    show_actions(job, subjob, actions)

if __name__ == "__main__":
    main()
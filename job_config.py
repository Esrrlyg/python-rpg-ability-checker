"""
Central job configuration for the RPG job system.

Attributes:
    jobs (list[str]):
        List of all playable jobs.

    job_skills (dict[str, list[tuple[int, str]]]):
        Skills available to each job, mapped to the level at which
        they are unlocked.

    job_tags (dict[str, set[str]]):
        Descriptive tags used for categorisation and compatibility
        checks.

    incompatible_subjobs (dict[str, set[str]]):
        Jobs that cannot be selected as a subjob for a given main job.
"""

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

job_tags = {
    "Freelancer": {"flex"},
    "Fighter": {"physical"},
    "Bard": {"support"},
    "Ninja": {"physical", "utility"},
    "White Mage": {"magic", "holy"},
    "Black Mage": {"magic", "dark"},
    "Red Mage": {"magic", "hybrid"},
}

incompatible_subjobs = {
    "Freelancer": {"Freelancer"},
    "Fighter": {"Fighter"},
    "Bard": {"Bard"},
    "Ninja": {"Ninja"},
    "White Mage": {"White Mage"},
    "Black Mage": {"Black Mage"},
    "Red Mage": {"Red Mage"},
}

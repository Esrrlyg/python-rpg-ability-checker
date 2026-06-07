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
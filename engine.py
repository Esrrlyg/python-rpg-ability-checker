import job_config

def get_skills(job, level):
    return [
        skill
        for req, skill in job_config.job_skills[job]
        if level >= req
    ]

def is_valid_subjob(main_job, subjob):
    if subjob is None:
        return True

    return main_job not in job_config.incompatible_subjobs.get(subjob, set())

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
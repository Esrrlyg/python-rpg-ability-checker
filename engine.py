"""
Core game logic for the RPG job system.

This module handles skill resolution, subjob validation,
and action list construction based on job level and rules
defined in job_config.
"""

import job_config

def get_skills(job, level):
    """
    Retrieve all skills unlocked for a job at a given level.

    Args:
        job (str): The job name.
        level (int): Current level of the job.

    Returns:
        list[str]: Skills available at the given level.
    """
    return [
        skill
        for req, skill in job_config.job_skills[job]
        if level >= req
    ]

def is_valid_subjob(main_job, subjob):
    """
    Validate whether a subjob can be paired with a main job.

    Args:
        main_job (str): The primary job.
        subjob (str | None): The selected subjob.

    Returns:
        bool: True if the subjob is allowed, False otherwise.
    """
    if subjob is None:
        return True

    return main_job not in job_config.incompatible_subjobs.get(subjob, set())

def remove_duplicates(items):
    """
    Remove duplicate entries for job actions while preserving order.

    Args:
        items (list): Input list possibly containing duplicates.

    Returns:
        list: List with duplicates removed.
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

def build_actions(job, level, subjob=None):
    """
    Build the full action list for a character based on job setup.

    Combines base actions, main job skills, and subjob skills
    (scaled to half level), then removes duplicates while preserving order.

    Args:
        job (str): Main job name.
        level (int): Main job level.
        subjob (str | None, optional): Subjob name. Defaults to None.

    Returns:
        list[str]: Final list of available actions.
    """

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

"""
Terminal user interface helpers.

This module contains utility functions for clearing the screen,
displaying errors, and presenting job actions to the player.
"""

import os

def clear():
    """Clear the terminal screen."""
    os.system('clear')

def show_error(message):
    """
    Display an error message and wait for user acknowledgement.

    Args:
        message (str): The error message to display.
    """
    clear()
    print(f"\nERROR: {message}")
    input("Press Enter to continue...")
    clear()

def show_actions(job, subjob, actions):
    """
    Display the available actions for a job combination.

    Args:
        job (str): The selected main job.
        subjob (str | None): The selected subjob, if any.
        actions (list[str]): Actions available to the character.
    """
    clear()

    title = job
    if subjob:
        title += f" / {subjob}"

    print(f"{title} Commands:\n")

    for action in actions:
        print(action)

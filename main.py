"""
Entry point for the RPG job system application.

This module coordinates user input, validation, and game logic
to generate and display the final action set for a character.
"""

import engine
import choices
import ui

def main():
    """
    Run the main application loop for job and subjob selection.

    Handles user input flow:
    - Select main job
    - Select and validate subjob
    - Select level
    - Build and display available actions
    """
    job = choices.choose_job()
    subjob = choices.choose_subjob(job)
    while not engine.is_valid_subjob(job, subjob):
        ui.show_error(f"{subjob} cannot be combined with {job}")
        subjob = choices.choose_subjob(job)
    level = choices.choose_level(job)
    actions = engine.build_actions(job, level, subjob)
    ui.show_actions(job, subjob, actions)

if __name__ == "__main__":
    main()

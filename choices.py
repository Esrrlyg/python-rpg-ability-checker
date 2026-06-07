import ui
import job_config

def choose_job():
    while True:
        ui.clear()
        try:
            print("Choose your job:\n")

            for i, job in enumerate(job_config.jobs, start=1):
                print(f"{i}. {job}")

            choice = int(input("\nEnter number: "))

            if 1 <= choice <= len(job_config.jobs):
                return job_config.jobs[choice - 1]

            ui.show_error("Invalid job selection.")

        except ValueError:
            ui.show_error("Please enter a number only.")

def choose_subjob(main_job):
    while True:
        ui.clear()
        try:
            print("\nChoose Subjob (0 = None):\n")

            print("0. None")

            available_subjobs = [job for job in job_config.jobs if job != main_job]

            for i, job in enumerate(available_subjobs, start=1):
                print(f"{i}. {job}")

            choice = int(input("\nEnter number: "))

            if choice == 0:
                return None

            if 1 <= choice <= len(available_subjobs):
                return available_subjobs[choice - 1]

            ui.show_error("Invalid subjob selection.")

        except ValueError:
            ui.show_error("Please enter a number only.")

def choose_level(job):
    while True:
        ui.clear()
        try:
            level = int(input(f"\nWhat level is your {job}? "))

            if level >= 1:
                return level

            ui.show_error("Level must be greater than 0")

        except ValueError:
            ui.show_error("Please enter a number only.")
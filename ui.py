import os

def clear():
    os.system('clear')

def show_error(message):
    clear()
    print(f"\nERROR: {message}")
    input("Press Enter to continue...")
    clear()

def show_actions(job, subjob, actions):
    clear()

    title = job
    if subjob:
        title += f" / {subjob}"

    print(f"{title} Commands:\n")

    for action in actions:
        print(action)

import engine
import choices
import ui

def main():
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
    
import subprocess
import sys


def what_the_kuy(task: str) -> str:
    you_kuy = {'4': '4kuy',
               '5': '5kuy',
               '6': '6kuy',
               '7': '7kuy',
               '8': '8kuy'}
    if task in '45678':
        return you_kuy.get(task)
    else:
        sys.exit(f'not found this:- {task} direct')


def validator_task_name(name: str) -> str:
    return '_'.join(name.split())


def get_info_about_task() -> list:
    task_kuy = input('change task level:- ')
    level_task = what_the_kuy(task_kuy)
    name_task = input('task name:- ')
    validator_task = validator_task_name(name_task)
    send_info = [level_task, f"{validator_task}.py"]
    return send_info


def linux_magic():
    info = get_info_about_task()
    task_kuy = info[0]
    task_name = info[1]
    subprocess.run(['touch', f"{task_name}"])
    subprocess.run(['mv', f'{task_name}', f'{task_kuy}'])
    print('ok')


linux_magic()

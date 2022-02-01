from typing import Any

from rich import print
from rich.padding import Padding
from util import notify

priority_type = {
    "1": ("red", "anger_symbol"),
    "2": ("green", "ophiuchus"),
    "3": ("blue", "herb"),
}


def task_icons(is_done: bool, priority: str) -> tuple[str, str]:
    is_done_icon = "[blue]:heavy_minus_sign:"
    if is_done:
        is_done_icon = "[d green]:white_check_mark:"

    color, icon = priority_type[priority]
    priority = f"[{color}]:{icon}:"

    return is_done_icon, priority


def show(ugly_list: dict[str, Any]) -> None:
    tasks_todo: list[str] = []
    tasks_progress: list[str] = []
    tasks_done: list[str] = []
    notes: list[str] = []

    if ugly_list:
        for id_, item in ugly_list.items():
            if item.get("is_task"):
                name, tags, priority, _, is_done, in_progress = item.values()
                is_done_icon, priority_icon = task_icons(is_done, priority)
                task = f"{priority_icon}{id_:>2}. {is_done_icon} [b white]{name} [green]{tags}"

                if in_progress:
                    tasks_progress.append(task)
                elif is_done:
                    tasks_done.append(task)
                else:
                    tasks_todo.append(task)
            else:
                name, _ = item.values()
                notes.append(f"[blue]:four_leaf_clover:{id_:>2}. [b white]{name}")

        total_tasks = sum([len(tasks_todo), len(tasks_progress), len(tasks_done)])
        print(
            Padding(f"[b]My Board [red][{len(tasks_done)}/{total_tasks}]", (1, 0, 0, 1))
        )

        print(Padding(f"[b]To-Do", (1, 0, 0, 3)))
        if tasks := tasks_todo:
            [print(Padding(task, (0, 5))) for task in tasks]
        else:
            notify("you don't have any task to do", "info", (0, 0, 0, 5))

        print(Padding(f"[b]In Progress", (1, 0, 0, 3)))
        if tasks := tasks_progress:
            [print(Padding(task, (0, 5))) for task in tasks]
        else:
            notify("you don't have any task in progress", "info", (0, 0, 0, 5))

        print(Padding(f"[b]Done", (1, 0, 0, 3)))
        if tasks := tasks_done:
            [print(Padding(task, (0, 5))) for task in tasks]
        else:
            notify("you don't have any completed task", "info", (0, 0, 0, 5))

        print(Padding(f"[b]Notes", (1, 0, 0, 1)))
        if notes:
            [print(Padding(note, (0, 3))) for note in notes]
        else:
            notify("you don't have any note", "info", (0, 0, 0, 3))
    else:
        notify("No task/note has been created.", "info")

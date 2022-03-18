from typing import Any

from rich import print
from rich.padding import Padding, PaddingDimensions

from util import notify

PRIORITY_TYPE = {
    "1": ("red", "anger_symbol"),
    "2": ("green", "ophiuchus"),
    "3": ("blue", "herb"),
}


def task_icons(is_done: bool, priority: str) -> tuple[str, str, str]:
    done_icon = "[d green]:white_check_mark:" if is_done else "[blue]:heavy_minus_sign:"
    color, icon = PRIORITY_TYPE[priority]
    priority = f"[{color}]:{icon}:"

    return done_icon, priority, color


def item_section(
    title: str,
    items: list[str],
    notify_suffix: str,
    title_padding: PaddingDimensions = (1, 0, 0, 3),
    item_padding: PaddingDimensions = (0, 0, 0, 5),
) -> None:
    print(Padding(f"[b]{title}", title_padding))
    if items:
        [print(Padding(item, item_padding)) for item in items]
    else:
        notify(f"you don't have any {notify_suffix}", "info", item_padding)


def show(ugly_list: dict[str, Any]) -> None:
    if ugly_list:
        tasks_todo: list[str] = []
        tasks_progress: list[str] = []
        tasks_done: list[str] = []
        notes: list[str] = []

        for id_, item in ugly_list.items():
            if item.get("is_task"):
                name, tags, priority, _, is_done, in_progress = item.values()
                done_icon, priority_icon, color = task_icons(is_done, priority)
                task = (
                    f"{priority_icon}{id_:>2}. {done_icon} "
                    f"[b white]{name} [{color}]{tags}"
                )

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

        item_section("To-Do", tasks_todo, "tasks to do")
        item_section("In Progress", tasks_progress, "tasks in progress")
        item_section("Done", tasks_done, "completed tasks")
        item_section("Notes", notes, "notes", (1, 0, 0, 1), (0, 0, 0, 3))
    else:
        notify("No task/note has been created.", "info")

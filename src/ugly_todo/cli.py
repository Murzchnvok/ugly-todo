from typing import Any

from colored import attr, fg

from .util import PaddingSize, notify, print_pad

PRIORITY_COLOR = {"1": fg(9), "2": fg(10), "3": fg(12)}


def item_section(
    title: str,
    items: list[str],
    notify_suffix: str,
    title_padding: PaddingSize = (0, 0, 3),
    item_padding: PaddingSize = (0, 0, 5),
) -> None:
    print_pad(f"{attr(1)}{fg(15)}{title}{attr(0)}", title_padding)
    if items:
        [print_pad(item, item_padding) for item in items]
    else:
        notify(f"you don't have any {notify_suffix}", "info", title_padding)
    print()


def show(ugly_list: dict[str, Any]) -> None:
    if ugly_list:
        tasks_todo: list[str] = []
        tasks_progress: list[str] = []
        tasks_done: list[str] = []
        notes: list[str] = []

        for id_, item in ugly_list.items():
            id_ = f"{attr(1)}·{id_:>2}{attr(0)}"
            if item.get("is_task"):
                name, tags, priority, _, is_done, in_progress = item.values()
                done_icon = f"{attr(2)}{fg(10)}✓" if is_done else f"{fg(12)}–"
                color = PRIORITY_COLOR[priority]
                task = f"{color}{id_} {done_icon} {fg(15)}{name} {color}{tags}{attr(0)}"

                if in_progress:
                    tasks_progress.append(task)
                elif is_done:
                    tasks_done.append(task)
                else:
                    tasks_todo.append(task)
            else:
                name, _ = item.values()
                notes.append(f"{fg(14)}{id_} → {fg(15)}{name}")

        total_tasks = sum([len(tasks_todo), len(tasks_progress), len(tasks_done)])
        board_total = f"{fg(9)}[{len(tasks_done)}/{total_tasks}]"
        print_pad(f"{attr(1)}My Board {board_total}{attr(0)}", (1, 1, 1))

        item_section("To-Do", tasks_todo, "tasks to do")
        item_section("In Progress", tasks_progress, "tasks in progress")
        item_section("Done", tasks_done, "completed tasks")
        item_section("Notes", notes, "notes", (0, 0, 1), (0, 0, 3))
    else:
        notify("No task/note has been created.", "info", (1, 1, 1))

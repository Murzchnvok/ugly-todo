import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from util import list_to_str, notify


@dataclass
class Task:
    name: str
    tags: str
    priority: str
    is_task: bool = True
    is_done: bool = False
    in_progress: bool = False


@dataclass
class Note:
    name: str
    is_task: bool = False


class UglyToDo:
    def __init__(self) -> None:
        self.TASK_FILE: Path = (Path(__file__).parent / "../.ugly-tasks.json").resolve()
        self.ugly_list: dict[str, dict[str, Any]] = {}

        try:
            self.ugly_list = json.loads(open(self.TASK_FILE, "r+").read())
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            open(self.TASK_FILE, "w+").write("{}")

    def get_ugly_list(self) -> dict[str, dict[str, Any]]:
        return self.ugly_list

    def set_id(self) -> str:
        try:
            return str(int(max([int(id_) for id_ in self.ugly_list])) + 1)
        except ValueError:
            return "1"

    def save_to_json(self) -> None:
        json.dump(self.ugly_list, open(self.TASK_FILE, "w"), indent=True)

    def format_task_tag(self, task: list[str]) -> tuple[str, str]:
        name: str = ""
        tags: str = ""

        for item in task:
            if item.startswith("@"):
                tags += f"{item} "
            else:
                name += f"{item} "

        return name.strip(), tags.strip()

    def add_task(self, item: list[str], priority: str = "2") -> None:
        id_ = self.set_id()
        name, tags = self.format_task_tag(item)
        task = Task(name, tags, priority)
        self.ugly_list[id_] = task.__dict__
        notify(f"Task created: {id_}")
        self.save_to_json()

    def add_note(self, item: list[str]) -> None:
        id_ = self.set_id()
        note = Note(list_to_str(item))
        self.ugly_list[id_] = note.__dict__
        notify(f"Note created: {id_}")
        self.save_to_json()

    def invert_key_values(self, id_list: list[str], key_1: str, key_2: str) -> None:
        not_found: str = ""

        for id_ in id_list:
            try:
                item = self.ugly_list[id_]
                if item[key_1]:
                    item[key_1] = False
                else:
                    item[key_1], item[key_2] = True, False
            except KeyError:
                not_found += f"{id_} "

        if not_found:
            notify(f"It's a note or couldn't find task: {not_found.strip()}", "error")
        self.save_to_json()

    def check(self, id_list: list[str]) -> None:
        self.invert_key_values(id_list, "is_done", "in_progress")

    def begin(self, id_list: list[str]) -> None:
        self.invert_key_values(id_list, "in_progress", "is_done")

    def remove(self, id_list: list[str]) -> None:
        deleted: str = ""
        not_found: str = ""

        for id_ in id_list:
            try:
                self.ugly_list.pop(id_)
                deleted += f"{id_} "
            except KeyError:
                not_found += f"{id_} "

        if deleted:
            notify(f"Deleted item(s): {deleted.strip()}")

        if not_found:
            notify(f"Couldn't find item(s): {not_found.strip()}", "error")
        self.save_to_json()

    def clear(self) -> None:
        id_list: list[str] = [
            id_ for id_, item in self.ugly_list.items() if item.get("is_done")
        ]
        if id_list:
            self.remove(id_list)
        else:
            notify("No task to be deleted.", "info")

    def sort_ids(self) -> None:
        ugly_list_values: list[Any] = list(self.ugly_list.values())
        self.ugly_list.clear()

        for value in ugly_list_values:
            self.ugly_list[self.set_id()] = value
        notify("ID(s) sorted")
        self.save_to_json()

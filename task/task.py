#!/usr/bin/env python3

import json
import os
import pathlib
import sys
from string import Template

try:
    from colored import attr, fg
except:
    print("Module 'colored' not installed.")
    print("Run: pip3 install -r requirements.txt")
    sys.exit(0)

PROGRAM_NAME = pathlib.Path(__file__).name


class Task:
    def __init__(self):
        self.TASK_FILE = os.path.join(os.getenv("HOME"), ".ugly-tasks.json")
        self.ugly_list = {}

        try:
            f = open(self.TASK_FILE, "r+")
            self.ugly_list = json.loads(f.read())
            f.close()
        except FileNotFoundError:
            f = open(self.TASK_FILE, "w+")
            f.write("{}")
            f.close()
        except json.decoder.JSONDecodeError:
            pass

    def add(self, task, priority):
        task_name = [task_name for task_name in task if not task_name.startswith("@")]
        tag = [tag for tag in task if tag.startswith("@")]

        task_name = " ".join(task_name)
        tag = " ".join(tag)

        _id = self.set_id()
        self.ugly_list[_id] = {
            "task": task_name.strip(),
            "tag": tag.strip(),
            "priority": priority,
            "is_task": True,
            "is_complete": False,
            "in_progress": False,
        }
        print(f"\n {fg(2)}{attr(0)} {attr(1)}Task created: {fg(6)}{_id}{attr(0)}")
        self.save_to_json()

    def note(self, note):
        note = " ".join(note)
        _id = self.set_id()
        self.ugly_list[_id] = {"_id": _id, "note": note.strip(), "is_task": False}
        print(f"\n {fg(2)}{attr(0)} {attr(1)}Note created: {fg(6)}{_id}{attr(0)}")
        self.save_to_json()

    def check(self, _ids):
        task = self.ugly_list
        for _id in _ids:
            try:
                if not task[str(_id)]["is_complete"]:
                    task[str(_id)]["is_complete"], task[str(_id)]["in_progress"] = (
                        True,
                        False,
                    )
                else:
                    task[str(_id)]["is_complete"] = False
                self.save_to_json()
            except KeyError:
                print(
                    f"\n {fg(1)}{attr(0)} {attr(1)}It's a note or unable to find item with id: "
                    f"{fg(6)}{_id}{attr(0)}"
                )

    def begin(self, _ids):
        task = self.ugly_list
        for _id in _ids:
            try:
                if not task[str(_id)]["in_progress"]:
                    task[str(_id)]["in_progress"], task[str(_id)]["is_complete"] = (
                        True,
                        False,
                    )
                else:
                    task[str(_id)]["in_progress"] = False
                self.save_to_json()
            except KeyError:
                print(
                    f"\n {fg(1)}{attr(0)} {attr(1)}It's a note or unable to find item with id: "
                    f"{fg(6)}{_id}{attr(0)}"
                )

    def remove(self, _ids):
        deleted_items = []
        not_found = []
        for _id in _ids:
            try:
                self.ugly_list.pop(_id)
                deleted_items.append(_id)
                self.save_to_json()
            except KeyError:
                not_found.append(_id)

        if deleted_items:
            print(
                f"\n {fg(2)}{attr(0)} {attr(1)}Deleted item(s): "
                f"{fg(6)}{' '.join(deleted_items)}{attr(0)}"
            )

        if not_found:
            print(
                f"\n {fg(1)}{attr(0)} {attr(1)}Unable to find item(s) with id(s): "
                f"{fg(6)}{' '.join(not_found)}{attr(0)}"
            )

    def clear(self):
        _ids = []
        for k, v in self.ugly_list.items():
            if v.get("is_complete"):
                _ids.append(k)

        self.remove(_ids) if _ids else print(
            f"\n {fg(1)}{attr(0)} {attr(1)}No task to be deleted.{attr(0)}"
        )

    def show(self):
        if self.ugly_list:
            tasks = []
            tasks_in_progress = []
            tasks_done = []
            notes = []

            completed_tasks = 0
            incompleted_tasks = 0

            for k, v in self.ugly_list.items():
                _id = k
                if v.get("is_task"):
                    completed_tasks += 1
                    if v.get("is_complete"):
                        incompleted_tasks += 1
                    task = v["task"]
                    tag = v["tag"]
                    priority = v["priority"]
                    is_complete = v["is_complete"]
                    in_progress = v["in_progress"]

                    is_complete_icon = (
                        f"{fg(2)}{fg(59)}" if is_complete else f"{fg(4)}{fg(7)}"
                    )

                    if priority == "1":
                        priority = f"{fg(1)}{attr(0)}"
                    elif priority == "2":
                        priority = f"{fg(2)}{attr(0)}"
                    else:
                        priority = f"{fg(4)}{attr(0)}"

                    show_task = Template(
                        f"     {priority}  {fg(59)}{_id:2}. {is_complete_icon}  {task} {fg(59)}{tag}{attr(0)}"
                    )
                    if in_progress:
                        tasks_in_progress.append(
                            show_task.substitute(
                                priority=priority,
                                _id=_id,
                                is_complete=is_complete,
                                task=task,
                                tag=tag,
                            )
                        )
                    elif is_complete:
                        tasks_done.append(
                            show_task.substitute(
                                priority=priority,
                                _id=_id,
                                is_complete=is_complete,
                                task=task,
                                tag=tag,
                            )
                        )
                    else:
                        tasks.append(
                            show_task.substitute(
                                priority=priority,
                                _id=_id,
                                is_complete=is_complete,
                                task=task,
                                tag=tag,
                            )
                        )
                else:
                    _id = v["_id"]
                    note = v["note"]
                    notes.append(
                        f"   {fg(6)}  {fg(59)}{_id:2}. {fg(7)}{note} {attr(0)}"
                    )

            print(
                f"\n {attr(1)}My Board {fg(59)}[{incompleted_tasks}/{completed_tasks}]{attr(0)}"
            )
            if tasks:
                print(f"\n   {attr(1)}To-Do{attr(0)}")
                for task in tasks:
                    print(task)

            if tasks_in_progress:
                print(f"\n   {attr(1)}In Progress{attr(0)}")
                for task in tasks_in_progress:
                    print(task)

            if tasks_done:
                print(f"\n   {attr(1)}Done{attr(0)}")
                for task in tasks_done:
                    print(task)

            if notes:
                print(f"\n {attr(1)}Notes{attr(0)}")
                for note in notes:
                    print(note)
        else:
            print(
                f"\n {fg(2)}{attr(0)}  {attr(1)}No task/note has been created.{attr(0)}"
            )

        return

    def set_id(self):
        try:
            _id = int(max(k for k, _ in self.ugly_list.items()))
            return str(_id + 1)
        except ValueError:
            return "1"

    def sort_ids(self):
        ugly_list = {}
        task_values = list(reversed(self.ugly_list.values()))
        for _id in range(1, len(task_values) + 1):
            ugly_list[str(_id)] = task_values.pop()

        self.ugly_list.clear()
        self.ugly_list = ugly_list
        print(f"\n {fg(2)}{attr(0)} {attr(1)}ID(s) sorted{attr(0)}")

        self.save_to_json()

    def save_to_json(self):
        json.dump(self.ugly_list, open(self.TASK_FILE, "w"), indent=True)

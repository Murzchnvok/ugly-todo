#!/usr/bin/env python3
from ugly_todo.cli import show
from ugly_todo.parser import args
from ugly_todo.utd import UglyToDo


def main():
    utd = UglyToDo()

    if task := args.add:
        if priority := args.priority:
            utd.add(task, priority[0])
        else:
            utd.add(task)

    elif note := args.note:
        utd.add(note, is_task=False)

    elif id_list := args.check:
        utd.check(id_list)

    elif id_list := args.begin:
        utd.begin(id_list)

    elif id_list := args.remove:
        utd.remove(id_list)

    elif args.clear:
        utd.clear()

    elif args.sort:
        utd.sort_ids()

    else:
        show(utd.ugly_list)


if __name__ == "__main__":
    main()

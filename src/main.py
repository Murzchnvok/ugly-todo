#!/usr/bin/env python3

from cli.app import show
from utd.app import UglyToDo
from util.parser import args


def main():
    utd = UglyToDo()

    if args.add:
        if args.priority:
            utd.add_task(args.add, args.priority[0])
        else:
            utd.add_task(args.add)

    elif args.note:
        utd.add_note(args.note)

    elif args.check:
        utd.check(args.check)

    elif args.begin:
        utd.begin(args.begin)

    elif args.remove:
        utd.remove(args.remove)

    elif args.clear:
        utd.clear()

    elif args.sort:
        utd.sort_ids()

    else:
        show(utd.get_ugly_list())


if __name__ == "__main__":
    main()

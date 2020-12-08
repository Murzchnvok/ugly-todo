#!/usr/bin/env python3

from task.task import Task
from utils.parser import args

if __name__ == "__main__":
    t = Task()

    if args.add:
        t.add(args.add, args.priority[0] if args.priority else "2")

    elif args.note:
        t.note(args.note)

    elif args.check:
        t.check(args.check)

    elif args.remove:
        t.remove(args.remove)

    elif args.clear:
        t.clear()

    else:
        t.show()

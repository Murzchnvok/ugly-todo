import argparse

from ugly_todo import cli, utd

USAGE_MESSAGE = """

Creating task/note (tags/priority are optional for tasks):
~$ %(prog)s -a simple task @tag
~$ %(prog)s -a Metropolis @book @read -p 1
~$ %(prog)s -n Keep Calm and DO SOMETHING
"""

parser = argparse.ArgumentParser(
    usage=USAGE_MESSAGE,
    description="Ugly To-Do (it's not that ugly.. right?)",
)
parser.add_argument(
    "-a",
    metavar="task",
    dest="add",
    type=str,
    nargs="+",
    help="add a new task",
)
parser.add_argument(
    "-p",
    metavar="priority",
    choices=("1", "2", "3"),
    dest="priority",
    type=str,
    nargs=1,
    help="priority level, (high: 1, default: 2, low: 3)",
)
parser.add_argument(
    "-n",
    metavar="note",
    dest="note",
    type=str,
    nargs="+",
    help="add a new note",
)
parser.add_argument(
    "-c",
    metavar="id",
    dest="check",
    type=str,
    nargs="+",
    help="check/uncheck task as complete",
)
parser.add_argument(
    "-b",
    metavar="id",
    dest="begin",
    type=str,
    nargs="+",
    help="start/stop task",
)
parser.add_argument(
    "-d",
    metavar="id",
    dest="remove",
    type=str,
    nargs="+",
    help="delete task/note by ID(s)",
)
parser.add_argument(
    "--clear",
    action="store_true",
    dest="clear",
    help="delete all completed tasks",
)
parser.add_argument(
    "--sort",
    action="store_true",
    dest="sort",
    help="sort all tasks/notes IDs",
)


def main() -> None:
    args = parser.parse_args()
    todo = utd.UglyToDo()

    if task := args.add:
        if priority := args.priority:
            todo.add(task, priority[0])
        else:
            todo.add(task)

    elif note := args.note:
        todo.add(note, is_task=False)

    elif id_list := args.check:
        todo.check(id_list)

    elif id_list := args.begin:
        todo.begin(id_list)

    elif id_list := args.remove:
        todo.remove(id_list)

    elif args.clear:
        todo.clear()

    elif args.sort:
        todo.sort_ids()

    else:
        cli.show(todo.ugly_list)


if __name__ == "__main__":
    main()

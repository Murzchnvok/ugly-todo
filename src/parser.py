import argparse

USAGE_MESSAGE = f"""a few examples

Creating task:
~$ %(prog)s -a simple task
~$ %(prog)s -a simple task with @tag
~$ %(prog)s -a not important task -p 3
~$ %(prog)s -a really important task @test @tag -p 1

Creating note:
~$ %(prog)s -n Keep Calm and STUDY

Using options from rich module:
~$ %(prog)s -a Metropolis '[red]@book @read'
~$ %(prog)s -n Keep Calm and '[i s blue]HACK THE PLANET'

Few useful options:
[color] -> color name
[d] -> dim
[i] -> italic
[s] -> strike
[u] -> underline

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

args = parser.parse_args()

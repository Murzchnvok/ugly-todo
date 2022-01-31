import argparse

from util.usage_message import USAGE_MESSAGE

parser = argparse.ArgumentParser(
    usage=USAGE_MESSAGE,
    description="Ugly To-Do (can you guess the reason for the name?!)",
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
    help="create a new note",
)
parser.add_argument(
    "-c",
    metavar="id",
    dest="check",
    type=str,
    nargs="+",
    help="Check/uncheck task as complete",
)
parser.add_argument(
    "-b",
    metavar="id",
    dest="begin",
    type=str,
    nargs="+",
    help="Start/Stop task",
)
parser.add_argument(
    "-d",
    metavar="id",
    dest="remove",
    type=str,
    nargs="+",
    help="delete a task or note",
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
    help="sort all tasks/notes ids",
)

args = parser.parse_args()

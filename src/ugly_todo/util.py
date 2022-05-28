from colored import attr, fg

NOTIFICATION_TYPE = {
    "success": f"{fg(10)}[S]",
    "info": f"{fg(11)}[I]",
    "error": f"{fg(9)}[X]",
}

PaddingSize = tuple[int, int, int]


def print_pad(text: str, pad: PaddingSize = (0, 0, 0)) -> None:
    top, bottom, tab = pad
    if top:
        print("\n" * top, end="")
    print(" " * tab + text) if tab else print(text)
    if bottom:
        print("\n" * bottom, end="")


def notify(message: str, type_: str = "success", pad: PaddingSize = (0, 0, 0)) -> None:
    print_pad(f"{attr(1)}{NOTIFICATION_TYPE[type_]} {message}{attr(0)}", pad)

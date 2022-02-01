from rich import print
from rich.padding import Padding

PaddingSize = tuple[int, int] | tuple[int, int, int, int]

notify_type = {
    "success": ("green", "s"),
    "info": ("yellow", "i"),
    "error": ("red", "x"),
}


def notify(message: str, type_: str = "success", padding: PaddingSize = (1, 1)) -> None:
    color, icon_suffix = notify_type[type_]
    type_ = f"[b {color}]:regional_indicator_{icon_suffix}:"
    print(Padding(f"{type_}  {message}", padding))


def list_to_str(list_: list[str]) -> str:
    return " ".join(list_).strip()

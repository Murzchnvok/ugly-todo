from rich import print
from rich.padding import Padding, PaddingDimensions

NOTIFICATION_TYPE = {
    "success": ("green", "s"),
    "info": ("yellow", "i"),
    "error": ("red", "x"),
}


def notify(
    message: str, type_: str = "success", padding: PaddingDimensions = (1, 1)
) -> None:
    type_ = "[b {}]:regional_indicator_{}:".format(*NOTIFICATION_TYPE[type_])
    print(Padding(f"{type_}  {message}", padding))

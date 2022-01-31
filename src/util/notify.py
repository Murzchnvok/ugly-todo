from rich import print
from rich.padding import Padding


def notify(
    message: str, type_: str = "success", padding: tuple[int, ...] = (1, 1)
) -> None:
    match type_:
        case "success":
            type_ = "[b green]:regional_indicator_symbol_letter_s:"
        case "info":
            type_ = "[b yellow]:regional_indicator_symbol_letter_i:"
        case "error":
            type_ = "[b red]:regional_indicator_symbol_letter_x:"
        case _:
            print("try one of those: success, info, error")

    print(Padding(f"{type_} {message}", padding))

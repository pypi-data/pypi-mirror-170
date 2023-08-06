from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from . import Settings, SpaceSaving
from .helpers import (
    Function,
    get_toplevel_symbol_usages_in_functions,
    is_used_as_type_hint,
    is_used_outside_function,
)


@dataclass
class OneFunctionImport(SpaceSaving):
    func: Function
    symbol: str
    usages_in_func: int
    used_as_type_hint: bool = False

    def saved_bytes(self) -> int:
        return 4 + (self.usages_in_func - 1) * 2

    def __repr__(self) -> str:  # pragma: no cover
        type_hint_msg = (
            " (WARNING: used as type-hint)" if self.used_as_type_hint else ""
        )
        return (
            f"{self.func} - {self.symbol} (~{self.saved_bytes()} bytes){type_hint_msg}"
        )


def one_function_import(
    file_content: str, settings: Settings = Settings()
) -> list[OneFunctionImport]:
    """Looking for symbols that can be imported only in one function.

    These symbols must be used only in that one function and nowhere
    else in the file (on top-level or in other functions).

    Issuing a warning if the symbol is used as a type-hint,
    as it will need to be added into `if TYPE_CHECKING` import branch.
    """

    def iterator() -> Iterator[OneFunctionImport]:
        for symbol, func_usages in get_toplevel_symbol_usages_in_functions(
            file_content
        ).items():
            if len(func_usages) != 1:
                continue  # used in more than one function
            if is_used_outside_function(file_content, symbol):
                continue  # used on top-level

            yield OneFunctionImport(
                func=func_usages[0].func,
                symbol=symbol,
                usages_in_func=func_usages[0].usages,
                used_as_type_hint=is_used_as_type_hint(file_content, symbol),
            )

    return sorted(list(iterator()), key=lambda x: x.func.line_no)

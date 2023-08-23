import random

from constants import ALPHA_CHARACTERS, NUMBERS, SYMBOLS
from dataclasses import dataclass


@dataclass
class PasswordRequirements:
    length: int
    has_alpha_characters: bool
    has_numbers: bool
    has_symbols: bool


class PasswordBuilder:
    def __init__(self, requirements):
        self.password_reqs: PasswordRequirements = requirements
        self.password_str: str | None = None

    @property
    def character_list(self) -> list[str]:
        char_list = []
        if self.password_reqs.has_alpha_characters:
            char_list.extend(ALPHA_CHARACTERS)
        if self.password_reqs.has_symbols:
            char_list.extend(SYMBOLS)
        if self.password_reqs.has_numbers:
            char_list.extend(NUMBERS)
        return char_list

    @property
    def is_capital_char(self) -> int:
        return random.randint(0, 1)

    def build_password(self) -> str:
        generated_password = []
        while len(generated_password) <= self.password_reqs.length:
            random_ix = random.randint(0, len(self.character_list) - 1)
            if self.is_capital_char:
                generated_password.append(self.character_list[random_ix].upper())
            else:
                generated_password.append(self.character_list[random_ix])
        return "".join(generated_password)

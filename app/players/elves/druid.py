from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self,
                 musical_instrument: str,
                 nickname: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)
        self._favourite_spell = favourite_spell
        pass

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname} "
                f"has a favourite spell: {self._favourite_spell}")

from abc import ABC, abstractmethod
from typing import Any
import ex1 as deck
from ex1.capabilities import Shiftling, Morphagon, Sproutling, Bloomelle


class AggressiveStrategyError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(
            f"Invalid creature {name} for this aggressive strategy")


class DefensiveStrategyError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(
            f"Invalid creature {name} for this defensive strategy")


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: deck.Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: deck.Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Shiftling | Morphagon) -> None:
        try:
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        except Exception as e:
            # When i pass my custom error it doesnt print the except
            # it just raises AttributeError???
            print(f"Battle error, aborting tournament: {e}")

    def is_valid(self, creature: Shiftling | Morphagon) -> bool:
        try:
            if creature.is_transformed:
                pass
        except Exception:
            return False
        return True


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Sproutling | Bloomelle) -> None:
        try:
            s: str = creature.heal()
            print(creature.attack())
            print(s)
        except DefensiveStrategyError as e:
            print(f"Battle error, aborting tournament: {e}")

    def is_valid(self, creature: Sproutling | Bloomelle) -> bool:
        try:
            creature.heal()
        except DefensiveStrategyError:
            return False
        return True

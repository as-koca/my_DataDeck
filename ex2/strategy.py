from abc import ABC, abstractmethod
from typing import Any
import ex1 as deck
from ex1.capabilities import Shiftling, Morphagon, Sproutling, Bloomelle


class BattleError(Exception):
    def __init__(self, msg: str = ''):
        super().__init__(msg)


class AggressiveStrategyError(BattleError):
    def __init__(self, name: str) -> None:
        super().__init__(
            f"Invalid creature {name} for this aggressive strategy")


class DefensiveStrategyError(BattleError):
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
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise AggressiveStrategyError(creature.name)
        else:
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Any) -> bool:
        if not isinstance(creature, (Shiftling | Morphagon)):
            return False
        return True


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise DefensiveStrategyError(creature.name)
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Any) -> bool:
        if not isinstance(creature, (Sproutling | Bloomelle)):
            return False
        return True

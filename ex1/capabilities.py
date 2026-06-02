from abc import ABC, abstractmethod
from ex1.creature import Creature as Creature
from ex1.creature import CreatureFactory as CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__, "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Sproutling:
        return Sproutling()

    @staticmethod
    def create_evolved() -> Bloomelle:
        return Bloomelle()


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__, "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.is_transformed is True:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__, "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.is_transformed is True:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."


class TransformCreatureFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Shiftling:
        return Shiftling()

    @staticmethod
    def create_evolved() -> Morphagon:
        return Morphagon()

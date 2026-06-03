from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name.capitalize()
        self.type: str = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    @staticmethod
    def attack() -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    @staticmethod
    def attack() -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    @staticmethod
    def attack() -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    @staticmethod
    def attack() -> str:
        return "Torragon uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Creature:
        return (Flameling())

    @staticmethod
    def create_evolved() -> Creature:
        return (Pyrodon())


class AquaFactory(CreatureFactory):
    @staticmethod
    def create_base() -> Creature:
        return (Aquabub())

    @staticmethod
    def create_evolved() -> Creature:
        return (Torragon())

#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def battle(c1: CreatureFactory, c2: CreatureFactory) -> None:
    f = c1.create_base()
    w = c2.create_base()
    print(f"{f.describe()}\nvs.\n{w.describe()}\nfight!")
    print(f.attack())
    print(w.attack())


def check_create(factory: CreatureFactory) -> None:
    f = factory.create_base()
    print(f.describe())
    print(f.attack())
    f = factory.create_evolved()
    print(f.describe())
    print(f.attack())


if __name__ == "__main__":
    print("Testing factory")
    check_create(FlameFactory())
    print("\nTesting factory")
    check_create(AquaFactory())
    print("\nTesting battle")
    battle(FlameFactory(), AquaFactory())

#!/usr/bin/env python3

import ex1 as caps


if __name__ == "__main__":
    heal_fact = caps.HealingCreatureFactory()
    base = heal_fact.create_base()
    evolved = heal_fact.create_evolved()
    print("Testing Creature with healing capability")
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

    transform_fact = caps.TransformCreatureFactory()
    base1 = transform_fact.create_base()
    evolved1 = transform_fact.create_evolved()
    print("\nTesting Creature with transform capabilty")
    print("base:")
    print(base1.describe())
    print(base1.attack())
    print(base1.transform())
    print(base1.attack())
    print(base1.revert())
    print("evolved:")
    print(evolved1.describe())
    print(evolved1.attack())
    print(evolved1.transform())
    print(evolved1.attack())
    print(evolved1.revert())

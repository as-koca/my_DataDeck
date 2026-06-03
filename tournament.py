#!/usr/bin/env python3

import ex2
from ex2 import ex1
from typing import Any


def battle(opponents: list[
        tuple[ex1.CreatureFactory, ex2.BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    i = 0
    j = 1
    while i < len(opponents):
        j = i + 1
        while j < len(opponents):
            base0 = opponents[i][0].create_base()
            base1 = opponents[j][0].create_base()
            print("\n* Battle *")
            print(f"{base0.describe()} vs. {base1.describe()}")
            print("now fight!")
            try:
                opponents[i][1].act(base0)
            except ex2.BattleError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            try:
                opponents[j][1].act(base1)
            except ex2.BattleError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            j += 1
        i += 1


if __name__ == "__main__":
    flame = ex1.FlameFactory()
    sprout = ex1.HealingCreatureFactory()
    water = ex1.AquaFactory()
    morph = ex1.TransformCreatureFactory()

    normal = ex2.NormalStrategy()
    aggro = ex2.AggressiveStrategy()
    defense = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    test1: list[Any] = [(flame, normal), (sprout, defense)]
    battle(test1)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    test2: list[Any] = [(flame, aggro), (sprout, defense)]
    battle(test2)

    print("\nTournament 3 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    test3: list[Any] = [(water, normal), (sprout, defense), (morph, aggro)]
    battle(test3)

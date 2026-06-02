#!/usr/bin/env python3

import ex2
from ex2 import deck as deck
from typing import Any


def battle(opponents: list[
        tuple[deck.CreatureFactory, ex2.BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    i = 0
    while i < len(opponents) - 1:
        print("* Battle *\n")
        j = i + 1
        opp = opponents[i]
        op = opp[0].create_base()
        print(op.describe())
        print("vs.")
        while (j < len(opponents) - i):
            oop1 = opponents[j]
            op1 = oop1[0].create_base()
            print(op1.describe())
            print("now fight!")
            opp[1].act(op)
            oop1[1].act(op1)
            j += 1
        i += 1


if __name__ == "__main__":
    flame = deck.FlameFactory()
    sprout = deck.HealingCreatureFactory()
    water = deck.AquaFactory()
    morph = deck.TransformCreatureFactory()

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
    battle(test1)
    print(aggro.act(flame))

from typing import List
from itertools import combinations

from PrisonerInteraction import PrisonerInteraction
from prisoner import Prisoner
from speakStrategies import *


def play_against(prisoner1: Prisoner, prisoner2: Prisoner):
    p1_testify = prisoner1.testify(prisoner2)
    p2_testify = prisoner2.testify(prisoner1)

    prisoner1.add_interaction(PrisonerInteraction(prisoner2, p2_testify))
    prisoner2.add_interaction(PrisonerInteraction(prisoner1, p1_testify))

    if p1_testify and p2_testify:
        prisoner1.add_years_in_prison(2)
        prisoner2.add_years_in_prison(2)
    elif p1_testify and not p2_testify:
        prisoner1.add_years_in_prison(0)
        prisoner2.add_years_in_prison(3)
    elif not p1_testify and p2_testify:
        prisoner1.add_years_in_prison(3)
        prisoner2.add_years_in_prison(0)
    elif not p1_testify and not p2_testify:
        prisoner1.add_years_in_prison(1)
        prisoner2.add_years_in_prison(1)


def combine_all_prisoners(prisoners: List[Prisoner], rounds: int = 1):
    for i in range(rounds):
        prisoner_permutations = combinations(prisoners, 2)

        for pair in prisoner_permutations:
            play_against(pair[0], pair[1])


prisoners = []

prisoners.append(Prisoner(AlwaysTrueStrategy()))
prisoners.append(Prisoner(AlwaysFalseStrategy()))
prisoners.append(Prisoner(IsOddInTimeInPrisonStrategy()))
prisoners.append(Prisoner(IsEvenInTimeInPrisonStrategy()))
prisoners.append(Prisoner(RandomStrategy()))
prisoners.append(Prisoner(TriggerStrategy()))
prisoners.append(Prisoner(TitForTatStrategy()))
prisoners.append(Prisoner(SuspiciousTitForTatStrategy()))

combine_all_prisoners(prisoners, 60)

for prisoner in prisoners:
    print(prisoner)

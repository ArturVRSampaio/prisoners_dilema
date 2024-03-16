from typing import List

from PrisonerInteraction import PrisonerInteraction
from speakStrategies import SpeakStrategy


class Prisoner:

    def __init__(self, speak_strategy: SpeakStrategy):
        self.speakStrategy = speak_strategy
        self.years_in_prison = 0
        self.prisonerInteractions = []

    def testify(self, opponent: 'Prisoner') -> bool:
        return self.speakStrategy.execute(self, opponent)

    def getName(self) -> str:
        return type(self.speakStrategy).__name__

    def add_years_in_prison(self, years: int) -> None:
        self.years_in_prison += years

    def add_interaction(self, prisoner_interaction: PrisonerInteraction) -> None:
        self.prisonerInteractions.append(prisoner_interaction)

    def getInteractionsWithOpponent(self, opponent: 'Prisoner') -> List[PrisonerInteraction]:
        interactions_with_opponent = []
        for interaction in self.prisonerInteractions:
            if interaction.opponent_prisoner == opponent:
                interactions_with_opponent.append(interaction)
        return interactions_with_opponent

    def __str__(self):
        interaction_str = ''
        for interaction in self.prisonerInteractions:
            interaction_str += interaction.__str__()

        return (f"--\n "
                f"years in prison: {self.years_in_prison}. \n "
                f"using the {self.getName()} \n"
                # f"interactions : {interaction_str}"
                f"")

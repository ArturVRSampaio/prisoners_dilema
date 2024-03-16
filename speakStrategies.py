from abc import ABC, abstractmethod
import random


class SpeakStrategy(ABC):
    @abstractmethod
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        pass


class AlwaysFalseStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        return False


class AlwaysTrueStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        return True


class RandomStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        return random.choice([True, False])


class TitForTatStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        interactions_with_opponent = prisoner.getInteractionsWithOpponent(opponent)
        if interactions_with_opponent:
            return interactions_with_opponent[-1].opponent_testify
        return False


class SuspiciousTitForTatStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        interactions_with_opponent = prisoner.getInteractionsWithOpponent(opponent)
        if interactions_with_opponent:
            return interactions_with_opponent[-1].opponent_testify
        return True


class IsOddInTimeInPrisonStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        return prisoner.years_in_prison % 2 == 1


class IsEvenInTimeInPrisonStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        return prisoner.years_in_prison % 2 == 0


class TriggerStrategy(SpeakStrategy):
    def execute(self, prisoner: 'Prisoner', opponent: 'Prisoner') -> bool:
        interactions_with_opponent = prisoner.getInteractionsWithOpponent(opponent)

        for interaction in interactions_with_opponent:
            if interaction.opponent_testify:
                return True
        return False


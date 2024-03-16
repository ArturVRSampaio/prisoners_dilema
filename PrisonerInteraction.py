class PrisonerInteraction:
    def __init__(self, opponent_prisoner: 'Prisoner', opponent_testify: bool):
        self.opponent_prisoner = opponent_prisoner
        self.opponent_testify = opponent_testify

    def __str__(self):
        return (f"\n"
                f"---- oponent: {type(self.opponent_prisoner.speakStrategy).__name__} \n"
                f"---- oponent_testify: {self.opponent_testify} \n"
                f"-------------")
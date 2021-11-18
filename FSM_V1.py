

# CREATE FSM WITH STATES AND TRANSITIONS
# THE STATES ARE: DORMINDO, ACORDADO, TRABALHANDO, DESCANSANDO
# THE TRANSITIONS ARE: 08:00, 12:00, 13:00, 18:00, 22:00
class States:
    DORMINDO = 'DORMINDO'
    ACORDADO = 'ACORDADO'
    TRABALHANDO = 'TRABALHANDO'
    DESCANSANDO = 'DESCANSANDO'


class Transitions:
    TR_08_00 = '08:00'
    TR_12_00 = '12:00'
    TR_13_00 = '13:00'
    TR_18_00 = '18:00'
    TR_22_00 = '22:00'


class FSM:
    def __init__(self, initial_state=States.DORMINDO, states=None) -> None:
        self.__states = initial_state
        if type(states) == list:
            if states:
                self.transition_list_to_state(states)
        else:
            self.transition_to(states)

    def __change_state(self, new_state) -> None:
        self.__states = new_state

    def get_state(self) -> str:
        return self.__states

    def get_transition_list(self) -> list:
        return [
            Transitions.TR_08_00,
            Transitions.TR_12_00,
            Transitions.TR_13_00,
            Transitions.TR_18_00,
            Transitions.TR_22_00
        ]

    def transition_to(self, transition: Transitions) -> None:
        if transition == Transitions.TR_08_00:
            self.__change_state(States.TRABALHANDO)
        elif transition == Transitions.TR_12_00:
            self.__change_state(States.DESCANSANDO)
        if transition == Transitions.TR_13_00:
            self.__change_state(States.TRABALHANDO)
        elif transition == Transitions.TR_18_00:
            self.__change_state(States.DESCANSANDO)
        elif transition == Transitions.TR_22_00:
            self.__change_state(States.DORMINDO)

    def transition_list_to_state(self, transition: list) -> None:
        print('List State:')
        for tr in transition:
            self.transition_to(tr)

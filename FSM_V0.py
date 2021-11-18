from enum import Enum


# Implement a state machine:
# Sua máquina deverá ter os seguintes estados:
# acordado
# trabalhando
# descansando
# dormindo
# Sua máquina deverá ter as seguintes transições:
# 08: 00
# 12: 00
# 13: 00
# 18: 00
# 22: 00
# Deve ser possível instanciar a máquina já com os estados e transições


class States:
    ACORDADO = 1
    TRABALHANDO = 2
    DESCANSANDO = 3
    DORMINDO = 4


class Transitions:
    TR_08_00 = 1
    TR_12_00 = 2
    TR_13_00 = 3
    TR_18_00 = 4
    TR_22_00 = 5


class StateMachine:

    def __init__(self, states, transitions, initial_state):
        self.states = states
        self.transitions = transitions
        self.current_state = initial_state

    def next_state(self, transition):
        if transition == Transitions.TR_08_00 and self.current_state == States.ACORDADO:
            self.current_state = States.TRABALHANDO
        elif transition == Transitions.TR_12_00 and self.current_state == States.TRABALHANDO:
            self.current_state = States.DESCANSANDO
        elif transition == Transitions.TR_13_00 and self.current_state == States.DESCANSANDO:
            self.current_state = States.TRABALHANDO
        elif transition == Transitions.TR_18_00 and self.current_state == States.TRABALHANDO:
            self.current_state = States.DESCANSANDO
        elif transition == Transitions.TR_22_00 and self.current_state == States.DESCANSANDO:
            self.current_state = States.DORMINDO
        elif transition == Transitions.TR_08_00 and self.current_state == States.DORMINDO:
            self.current_state = States.ACORDADO

    def print_state(self):
        print(self.current_state)

    def get_state(self):
        return self.current_state


if __name__ == '__main__':
    states = [
        States.ACORDADO,
        States.TRABALHANDO,
        States.DESCANSANDO,
        States.TRABALHANDO,
        States.DORMINDO
    ]

    transitions = [
        Transitions.TR_08_00,
        Transitions.TR_12_00,
        Transitions.TR_13_00,
        Transitions.TR_18_00,
        Transitions.TR_22_00
    ]

    machine = StateMachine(states, transitions, States.DESCANSANDO)

    print('Start State: ' + str(machine.get_state()))
    print('Call Next State >>> ')
    machine.next_state(Transitions.TR_08_00)
    print('Atual State: ' + str(machine.get_state()))
    print('Call Next State >>> ')
    machine.next_state(Transitions.TR_12_00)
    print('Atual State: ' + str(machine.get_state()))
    print('Call Next State >>> ')
    machine.next_state(Transitions.TR_13_00)
    print('Atual State: ' + str(machine.get_state()))
    print('Call Next State >>> ')
    machine.next_state(Transitions.TR_18_00)
    print('Atual State: ' + str(machine.get_state()))
    print('Call Next State >>> ')
    machine.next_state(Transitions.TR_22_00)
    print('Atual State: ' + str(machine.get_state()))
    print('Call Next State >>> ')
    machine.next_state(Transitions.TR_08_00)
    print('Atual State: ' + str(machine.get_state()))

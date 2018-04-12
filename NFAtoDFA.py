#!/usr/bin/env python3.6
""" Automata Theory and Formal Languages
    Final Project.

    Goal: Convert a Non-Deterministic Finite Automata
    to Deterministic Finite Automata.

    Members: Hocker, Griffin;
             Laesker, Denis;
             Wilthew, Patricia."""
import sys


def main():
    # Obtain input file name that contains NFA
    input_file = sys.argv[1]
    file_obj = open(input_file, 'r')
    text = file_obj.read()

    # Get alphabet in NFA
    alphabet = get_alphabet(text)

    # Build a dictionary and a list of final states
    NFA_dic, finals = convert_to_dictionary(text, alphabet)

    # Convert NFA to DFA
    DFA_dic = nfa_to_dfa(NFA_dic)

    # Print obtained DFA as text
    print(color(convert_to_text(DFA_dic, finals)))


def nfa_to_dfa(NFA_dic):
    """Create a DFA from an NFA."""
    # Copy the first state transitions to the DFA
    DFA_dic = {'0': NFA_dic['0']}

    # Keep a list of current states of DFA to iterate over each created
    # state
    states_list = list(DFA_dic.keys())

    # Create states for the DFA
    for state in states_list:
        # Get transitions from state
        transitions = DFA_dic[state]

        # For every possible transition from current state
        for character, next_state in transitions.items():

            # If next state exists in DFA, ignore and continue
            if next_state in DFA_dic.keys():
                continue

            # If next state exists in NFA, copy its transitions
            if next_state in NFA_dic.keys():
                DFA_dic[next_state] = NFA_dic[next_state]
                continue

            # If next_state has not been created, create it
            # If it is composed by more than one state, determine those
            # states transitions and join these states as one state.
            if len(next_state) > 1:
                state_components = next_state.split("-")

                with_a = set()
                with_b = set()

                for s in state_components:
                    dict_of_next_states = NFA_dic[s]
                    with_a.add(dict_of_next_states['a'])
                    with_b.add(dict_of_next_states['b'])

                state_with_a = remove_duplicates(join_states(with_a))
                state_with_b = remove_duplicates(join_states(with_b))

                dic = {'a': state_with_a,
                       'b': state_with_b}

                # Assign new next transitions for this state
                DFA_dic[next_state] = dic

            # Update list in which this for-loop is iterating
            states_list.append(next_state)

    return DFA_dic


def join_states(set_):
    """Given a set of characters, join them with a '-' """
    if len(set_) > 1:
        # If the set is greater than one, check if state empty is a part
        # of it. If it is, remove it. Then form a string delimited by '-'
        # with the characters in the set
        if 'D' in set_:
            set_.remove('D')
            return '-'.join(list(set_))
        else:
            return '-'.join(sorted(list(set_)))
    else:
        return ''.join(list(set_))


def remove_duplicates(string):
    """Remove duplicate characters from a '-' delimited string."""
    return '-'.join(sorted(list(set(x for x in string.split('-')))))


def get_alphabet(text):
    """Return a list of the elements in the alphabet."""
    first_line = text.splitlines()[0]
    return [x.strip() for x in first_line.split(',')[1:]]


def convert_to_dictionary(text, alphabet):
    """Copy info in text to a dictionary."""
    # List of final states
    finals = []
    # Dictionary to store NFA in file
    dic = {}
    # Substitute transitions to empty by transitions to dead states
    text = text.replace('e', 'D')

    # Get rows in file
    rows = text.splitlines()[1:]  # Ignore first line

    # Parse each row to store next states of each state
    for row in rows:
        column_list = row.split(',')

        # Store first column in key and rest in list
        cur_state, next_states_list = column_list[0], column_list[1:]

        # Append states with '*' to a list of final states
        if '*' in cur_state:
            cur_state = cur_state.replace('*', '')
            finals.append(cur_state)

        # Get rid of spaces and tabs
        next_states_list = [x.strip() for x in next_states_list]

        transitions = {}
        for character, next_state in zip(alphabet, next_states_list):
            transitions[character] = next_state

        dic[cur_state] = transitions

    # Return NFA represented as a dictionary and a list of final states
    return dic, finals


def is_final(state, final_states):
    """For a string representing a state, return True if one of
    its states (characters) is a final state; return False otherwise."""
    for char in state:
        if char in final_states:
            return True
    return False


def convert_to_text(DFA_dic, finals):
    """Given a DFA in dictionary form, represent it in text and 
    output it."""
    first_row = "State,\ta,\tb"
    rows = [first_row]

    for state, transitions in DFA_dic.items():
        if is_final(state, finals):
            row = state + "*\t"
        else:
            row = state + "\t"

        for trans_state in transitions.values():
            row += trans_state + "\t"
        rows.append(row)

    return "\n".join(rows)


def color(string):
    """Given a string, add to string the necessary encoding
    to color it blue when printed into the terminal."""
    return "\033[1;34m%s\033[1;0m" % string


if __name__ == "__main__":
    main()

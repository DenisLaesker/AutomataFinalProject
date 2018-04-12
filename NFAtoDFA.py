#!/usr/bin/env python3.6

"""Convert a Non-Deterministic Finite Automata
to Deterministic Finite Automata."""

# TODO: Replace 'e' for 'D' in the process of converting to DFA

def main():
    file_obj = open("input.txt", 'r')
    text = file_obj.read()

    # Get alphabet in NFA
    alphabet = get_alphabet(text)

    # Get text into a dictionary and a list of final states
    NFA_dic, finals = convert_to_dictionary(text, alphabet)

    print("Finals: ", finals)

    # Crate new states
    DFA_dic = create_new_states(NFA_dic, alphabet)

    print("DFA: ", DFA_dic)


def create_new_states(NFA_dic, alphabet):
    """Create new states. For example, 0-1 needs to
    also be represented as a state."""
    # Copy the first state transition to the DFA
    DFA_dic = {'0': NFA_dic['0']}

    # Get all states' names in DFA_dic (originally one only,
    # but this list gets appended states at the end of for loop).
    states_list = list(DFA_dic.keys())

    # Create other states of the DFA
    for state in states_list:
        print("Current State: ", state)
        
        # Get next states of state
        next_states_dic = DFA_dic[state]
        print("\tNext States: ", next_states_dic)

        # For every possible transition from current state
        for character in next_states_dic.keys():
            print("\t\tWith ", character)

            next_state = remove_duplicates(next_states_dic[character])
            print("\t\t\tIts next state is: ", next_state)

            # If next state exists in DFA, ignore and continue
            if next_state in DFA_dic.keys():
                continue

            # If next state is in NFA, copy its next states
            if next_state in NFA_dic.keys():
                DFA_dic[next_state] = NFA_dic[next_state]
                continue

            # If next state doesn't exist, create it

            # If it's a state made out of more than one state, then 
            # determine its next states by joining the next states
            # of each single state
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

                print("\t\t\t\tNew next states for this state: ", dic)
                DFA_dic[next_state] = dic

            # If the state is made out of itself only, then copy its
            # next states from the NFA
            else:
                DFA_dic[next_state] = NFA_dic[next_state]
            
            # Update list in which it is iterating
            states_list.append(next_state)

    return DFA_dic


def join_states(set_):
    """Given a set of characters, join them with a '-' """
    if len(set_) > 1 and 'e' in set_:
        set_.remove('e')
        return '-'.join(list(set_))

    if len(set_) > 1 and 'e' not in set_:
        return '-'.join(sorted(list(set_)))

    if len(set_) == 1:
        return ''.join(list(set_))


def remove_duplicates(string):
    """Remove duplicate characters from a '-' divided string """
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

    # Get rows in file
    rows = text.splitlines()[1:] # Ignore first line

    # Parse each row to store next states of each state
    for row in rows:
        column_list = row.split(',')
        
        # Store first column in key and rest in list
        cur_state, next_states_list = column_list[0], column_list[1:]
        
        if '*' in cur_state:
            cur_state = cur_state.replace('*', '')
            finals.append(cur_state)

        # Get rid of spaces and tabs
        next_states_list = [x.strip() for x in next_states_list]

        next_states_dic = {}
        for character, next_state in zip(alphabet, next_states_list):
            next_states_dic[character] = next_state 
            
        dic[cur_state] = next_states_dic 

    return dic, finals

if __name__ == "__main__":
    main()


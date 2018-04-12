#!/usr/bin/env python3.6

"""Convert a Non-Deterministic Finite Automata
to Deterministic Finite Automata."""

def main():
    file_obj = open("input.txt", "r")
    text = file_obj.read()

    # Get alphabet in NFA
    alphabet = get_alphabet(text)

    # Insert text into a dictionary
    NFA_dic = convert_to_dictionary(text, alphabet)


def create_new_states(NFA_dic, alphabet)
    """Create new states. For example, 0-1 needs to
    also be represented as a state."""
    # Copying the first state transition to the DFA
    DFA_dic = {0: NFA_dic[0]}

    # Create following states for the DFA
    for state in DFA_dic.keys():
        # Get next states of state
        next_states_dic = DFA_dic[state]

        for character in next_states_dic.keys():
            next_state = next_states_dic[character]
            # If next state exists in DFA, ignore and continue
            if next_state in DFA_dic:
                continue
            # If next state doesn't exist, create it
            # But first, check if it's a state made out 
            # of more than 1 state
            if len(next_state) > 1:
                state_components = next_state.split("-")

                with_a = set()
                with_b = set()

                for s in state_components:        # [0, 1]
                    dict_of_next_states = NFA[s]  # {'a': 0, 'b': 1}  {'a': 1, 'b': 2}
                    with_a.add(dict_of_next_states['a'])
                    with_b.add(dict_of_next_states['b'])


                # for set_ in [with_a, with_b]:
                #     if len(set_) == 1:
                #         DFA_dic[set_[0]] = NFA_dic[set_[0]]
                #     if "D" in set_:
                #         set_.remove("D")


            else:
                DFA_dic[state] = NFA_dic[state]



def get_alphabet(text):
    """Return a list of the elements in the alphabet."""
    first_line = text.splitlines()[0]

    return [x.strip() for x in first_line.split(",")[1:]]


def convert_to_dictionary(text, alphabet):
    """Insert """
    rows = text.splitlines()[1:] # Ignore first line
    dic = {}

    for row in rows:
        column_list = row.split(',')
        
        # Store first column in key and rest in list
        cur_state, next_states_list = column_list[0], column_list[1:]
        
        # Get rid of spaces and tabs
        next_states_list = [x.strip() for x in next_states_list]

        next_states_dic = {}
        for character, next_state in zip(alphabet, next_states_list):
            next_states_dic[character] = next_state 
            
        dic[cur_state] = next_states_dic 

    print(dic)
    return None

if __name__ == "__main__":
    main()

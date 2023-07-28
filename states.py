import os

from states_account_creation import STATES as STATES_ACCOUNT_CREATION
from click_position import click
from state import State

FREQUENCY = 1

current_directory = os.path.dirname(os.path.abspath(__file__))
img_1000 = os.path.join(os.path.join(current_directory, "state_images\\img_1000.jpg"))

GENERAL_PRE_STATE = State(
    id=1001,
    image_paths=[img_1000],
    actions=[click],
    durations=[FREQUENCY],
    next_states=[]
),

GENERAL_POST_STATE = State(
    id=1002,
    image_paths=[""],
    actions=["Hello World!"],
    durations=[FREQUENCY],
    next_states=[999]
),

def merge_states(list_of_states):
    if not list_of_states:
        return []
    if len(list_of_states) < 2:
        return list_of_states[0]
    return list_of_states[0] + merge_states(list_of_states[1:])

def set_pre_post_states(states):
    for state in states:
        state.pre_state = GENERAL_PRE_STATE[0]
        state.pre_state.next_states.append(state.id) # ! when retry image recognized return to the current state
        state.post_state = GENERAL_POST_STATE[0]
        state.post_state.next_states.append(state.id)
    return states

STATES = set_pre_post_states(merge_states([STATES_ACCOUNT_CREATION]))
# STATES = merge_states([STATES_ACCOUNT_CREATION])
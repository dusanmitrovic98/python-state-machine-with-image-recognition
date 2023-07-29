import os

from states_account_creation import STATES as STATES_ACCOUNT_CREATION
from states_event_cute_vs_creepy import STATES as STATES_EVENT_CUTE_VS_CREEPY
from click_position import click
from state import State

FREQUENCY = 1

current_directory = os.path.dirname(os.path.abspath(__file__))
img_1000 = os.path.join(os.path.join(current_directory, "state_images\\img_1000.jpg"))
img_ecvc_06 = os.path.join(os.path.join(current_directory, "images\\event_cute_vs_creepy\\img_ecvc_06.jpg"))

GENERAL_PRE_STATES = [
    State(
        id=1001,
        image_paths=[img_ecvc_06, img_1000],
        actions=[click] * 2,
        durations=[FREQUENCY / 4, FREQUENCY],
        next_states=[0]
    ),
]

GENERAL_POST_STATES = [
    State(
        id=1002,
        image_paths=[""],
        actions=["Hello World!"],
        durations=[FREQUENCY],
        next_states=[999]
    ),
]

def merge_states(list_of_states):
    if not list_of_states:
        return []
    if len(list_of_states) < 2:
        return list_of_states[0]
    return list_of_states[0] + merge_states(list_of_states[1:])

def set_pre_post_states(states):
    for state in states:
        state.pre_states = GENERAL_PRE_STATES
        state.pre_states.extend(state.pre_states)
        state.post_states = GENERAL_POST_STATES
        state.post_states.extend(state.post_states)
    return states

# ! account creation
# STATES = set_pre_post_states(merge_states([STATES_ACCOUNT_CREATION]))
# ! event cute vs creepy
# STATES = set_pre_post_states(merge_states([STATES_EVENT_CUTE_VS_CREEPY]))
# ! watch ads
# STATES = set_pre_post_states(merge_states([STATES_EVENT_CUTE_VS_CREEPY]))
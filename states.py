import os

from states_event_cute_vs_creepy import STATES as STATES_EVENT_CUTE_VS_CREEPY
from states_account_creation import STATES as STATES_ACCOUNT_CREATION
from states_transfer_gold import STATES as STATES_TRANSFER_GOLD
from states_watch_ads import STATES as STATES_WATCH_ADS
from click_position import click
from state import State
from config import img_acc_01, img_wa_14

FREQUENCY = 1

current_directory = os.path.dirname(os.path.abspath(__file__))
img_1000 = os.path.join(os.path.join(current_directory, "images\\img_1000.jpg"))
img_1001 = os.path.join(os.path.join(current_directory, "images\\img_1001.jpg"))

GENERAL_PRE_STATES = [
    State(
        id=1001,
        image_paths=[img_wa_14, img_1000, img_1001],
        actions=[click] * 3,
        durations=[FREQUENCY] * 3,
        next_states=[110] # ! 13
    ),
]

GENERAL_POST_STATES = [
    State(
        id=1002,
        image_paths=[img_acc_01],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[1]
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
        state.pre_states[0].next_states.append(state.id)
        state.pre_states[0].next_states.append(state.id)
        # ! state.post_states = GENERAL_POST_STATES
        # ! state.post_states[0].append(state.id)
    return states

# ! account creation
# STATES = set_pre_post_states(merge_states([STATES_ACCOUNT_CREATION]))
# ! event cute vs creepy
# STATES = set_pre_post_states(merge_states([STATES_EVENT_CUTE_VS_CREEPY]))
# ! gold collection
STATES = set_pre_post_states(merge_states([STATES_ACCOUNT_CREATION, STATES_WATCH_ADS, STATES_TRANSFER_GOLD]))
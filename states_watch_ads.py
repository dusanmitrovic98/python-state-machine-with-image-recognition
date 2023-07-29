import os

from config import img_wa_10, img_wa_11, img_wa_12, img_wa_13, img_wa_14, img_wa_15, img_wa_16, img_wa_17, img_wa_99
from config import END_STATE_WATCH_ADS, FREQUENCY
from held_mouse_up import held_mouse_up
from click_position import click
from state import State

STATES = [
    State(
        id=10, # ! shop button
        image_paths=[img_wa_10],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[11]
    ),
    State(
        id=11, # ! gold button
        image_paths=[img_wa_11],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[12]
    ),
    State(
        id=12, # ! scroll
        image_paths=[img_wa_12],
        actions=[held_mouse_up],
        durations=[FREQUENCY],
        next_states=[13]
    ),
    State(
        id=13, # ! watch ads button clicked
        image_paths=[img_wa_13],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[14]
    ),
    State(
        id=14, # ! x1 button clicked
        image_paths=[img_wa_14, img_wa_15, img_wa_16, img_wa_17, img_wa_99],
        actions=[click] * 5,
        durations=[FREQUENCY] * 5,
        next_states=[13] * 4 + [END_STATE_WATCH_ADS]
    ),
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
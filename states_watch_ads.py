import os

from config import img_wa_10, img_wa_11, img_wa_12, img_wa_13, img_wa_14, img_wa_15, img_wa_16, img_wa_17, img_wa_18, img_wa_19, img_wa_20, img_wa_21, img_wa_22, img_wa_23, img_wa_24, img_wa_25, img_wa_99, img_1100, img_1101
from config import END_STATE_WATCH_ADS, FREQUENCY
from held_mouse_left import held_mouse_left
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
        id=14, # ! x button clicked
        image_paths=[img_wa_19, img_wa_20, img_wa_21, img_wa_18, img_wa_14, img_wa_15, img_wa_16, img_wa_17, img_wa_25, img_wa_24, img_wa_22, img_wa_99],
        actions=[click] * 12,
        durations=[FREQUENCY] * 12,
        next_states=[14] + [13] * 2 + [13] + [13] * 6 + [15] + [END_STATE_WATCH_ADS]
    ), State(
        id=15, # ! watch ads button clicked
        image_paths=[img_wa_23],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[13]
    ), State(
        id=1100, # ! timeout regeneration
        image_paths=[img_1100],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[1101]
    ), State(
        id=1101, # ! timeout regeneration stop highrise from running
        image_paths=[img_1101],
        actions=[held_mouse_left],
        durations=[FREQUENCY],
        next_states=[1]
    )
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
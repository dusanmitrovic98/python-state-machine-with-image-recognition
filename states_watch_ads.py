import os
from config import FREQUENCY

from config import img_wa_10, img_wa_11, img_wa_12, img_wa_13
from type_username import type_username
from held_mouse_up import held_mouse_up
from delete_input import delete_input
from move_cursor import move_cursor
from click_position import click
from state import State

STATES = [
    State(
        id=10,
        image_paths=[img_wa_10],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[11]
    ),
    State(
        id=11,
        image_paths=[img_wa_11],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[12]
    ),
    State(
        id=12,
        image_paths=[img_wa_12],
        actions=[held_mouse_up],
        durations=[FREQUENCY],
        next_states=[13]
    ),
    State(
        id=13,
        image_paths=[img_wa_13],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[999]
    ),
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
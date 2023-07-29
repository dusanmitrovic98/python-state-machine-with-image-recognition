import os

from config import img_tg_100, img_tg_101, img_tg_102, img_tg_103
from config import END_STATE_TRANSFER_GOLD, FREQUENCY
from type_username import type_username_01
from move_cursor import move_cursor
from click_position import click
from state import State

STATES = [
    State(
        id=100,
        image_paths=[img_tg_100],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[101]
    ),
    State(
        id=101,
        image_paths=[img_tg_101],
        actions=[move_cursor],
        durations=[FREQUENCY],
        next_states=[102]
    ),
    State(
        id=102,
        image_paths=[img_tg_100],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[103]
    ),
    State(
        id=103,
        image_paths=[img_tg_101],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[104]
    ),
    State(
        id=104,
        image_paths=[img_tg_102],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[105]
    ),
    State(
        id=105,
        image_paths=[img_tg_103],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[106]
    ),
    State(
        id=106,
        image_paths=[img_tg_103],
        actions=[type_username_01],
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
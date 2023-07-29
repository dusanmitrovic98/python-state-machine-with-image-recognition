import os

from config import img_tg_100
from config import END_STATE_TRANSFER_GOLD, FREQUENCY
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
        image_paths=[img_tg_100],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[102]
    ),
    State(
        id=102,
        image_paths=[img_tg_100],
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
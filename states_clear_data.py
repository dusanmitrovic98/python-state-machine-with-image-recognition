import os

from config import img_cd_200
from config import FREQUENCY
from click_position import click
from state import State

STATES = [
    State(
        id=100,
        image_paths=[img_tg_200],
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
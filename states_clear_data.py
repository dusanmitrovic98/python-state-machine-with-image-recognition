import os

from config import img_tg_113, img_cd_201
from config import FREQUENCY
from click_position import click
from held_mouse_down import held_mouse_down
from state import State

STATES = [
    State(
        id=200,
        image_paths=[img_tg_113],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[999]
    ),
    State(
        id=201,
        image_paths=[img_cd_201],
        actions=[held_mouse_down],
        durations=[FREQUENCY],
        next_states=[999]
    )
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
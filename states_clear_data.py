import os

from config import img_tg_113, img_cd_201, img_cd_202, img_cd_203, img_cd_204, img_cd_205, img_cd_206, img_cd_207
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
        next_states=[201]
    ),
    State(
        id=201,
        image_paths=[img_cd_201],
        actions=[held_mouse_down],
        durations=[FREQUENCY],
        next_states=[202]
    ),
    State(
        id=202,
        image_paths=[img_cd_202],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[203]
    ),
    State(
        id=203,
        image_paths=[img_cd_203],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[204]
    ),
    State(
        id=204,
        image_paths=[img_cd_204],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[205]
    ),
    State(
        id=205,
        image_paths=[img_cd_205],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[206]
    ),
    State(
        id=206,
        image_paths=[img_cd_206],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[207]
    ),
    State(
        id=207,
        image_paths=[img_cd_207],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[208]
    ),
    State(
        id=208,
        image_paths=[img_tg_113],
        actions=[click],
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
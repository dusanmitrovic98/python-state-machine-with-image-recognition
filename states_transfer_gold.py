import os

from config import img_wa_10
from config import END_STATE_TRANSFER_GOLD, FREQUENCY
from click_position import click
from state import State

STATES = [
    State(
        id=100,
        image_paths=[img_wa_10],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[11]
    ),
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
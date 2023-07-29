import os

from delete_input import delete_input
from move_cursor import move_cursor
from click_position import click
from state import State
from type_username import type_username

FREQUENCY = 1

current_directory = os.path.dirname(os.path.abspath(__file__))
img_wa_10 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_10.jpg"))

STATES = [
    State(
        id=10,
        image_paths=[img_wa_10],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[1]
    ),
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
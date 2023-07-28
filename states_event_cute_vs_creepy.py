import os

from click_position import click
from state import State

FREQUENCY = 1

current_directory = os.path.dirname(os.path.abspath(__file__))
img_ecvc_01 = os.path.join(os.path.join(current_directory, "images\\event_cute_vs_creepy\\img_ecvc_01.jpg"))

STATES = [
    State(
        id=0,
        image_paths=[img_ecvc_01],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[99]
    ),
    State( # ! end state should be removed
        id=999,
        image_paths=[""],
        actions=["State machine stopped."],
        durations=[0],
        next_states=[-1]
    )
]
import os

from delete_input import delete_input
from move_cursor import move_cursor
from click_position import click
from state import State
from type_username import type_username

FREQUENCY = 1

current_directory = os.path.dirname(os.path.abspath(__file__))
img_acc_01 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_01.jpg"))
img_acc_02 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_02.jpg"))
img_acc_03 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_03.jpg"))
img_acc_04 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_04.jpg"))
img_acc_05 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_05.jpg"))
img_acc_06 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_06.jpg"))
img_acc_07 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_07.jpg"))

STATES = [
    State(
        id=0,
        image_paths=[img_acc_01],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[1]
    ),
    State(
        id=1,
        image_paths=[img_acc_02],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[2]
    ), 
    State(
        id=2,
        image_paths=[img_acc_02],
        actions=[move_cursor],
        durations=[FREQUENCY],
        next_states=[3]
    ), 
    State(
        id=3,
        image_paths=[img_acc_03],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[4]
    ), 
    State(
        id=4,
        image_paths=[img_acc_03],
        actions=[type_username],
        durations=[FREQUENCY],
        next_states=[5]
    ), 
    State(
        id=5,
        image_paths=[img_acc_04, img_acc_05, img_acc_07],
        actions=["Username is available.", "Username is not unavailable.", 
                 "Must be between 3 and 14 characters long."],
        durations=[FREQUENCY] * 3,
        next_states=[6] + [7] * 2
    ), 
    State(
        id=6,
        image_paths=[img_acc_03, img_acc_06], 
        actions=[click, click],
        durations=[FREQUENCY] * 2,
        next_states=[6, 999]
    ), 
    State(
        id=7,
        image_paths=[img_acc_05, img_acc_07],
        actions=[delete_input] * 2,
        durations=[FREQUENCY] * 2,
        next_states=[4] * 2
    ), 
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
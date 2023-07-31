import os

from config import img_tg_100, img_tg_101, img_tg_102, img_tg_103, img_tg_104, img_tg_105, img_tg_106, img_tg_107, img_tg_108, img_tg_109, img_tg_110, img_tg_111, img_tg_112
from move_cursor_left_without_clicking import move_cursor_left_without_clicking
from config import END_STATE_TRANSFER_GOLD, FREQUENCY
from held_mouse_left import held_mouse_left
from type_username import type_username_01
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
        actions=[move_cursor_left_without_clicking],
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
        next_states=[107]
    ),
    State(
        id=107,
        image_paths=[img_tg_104],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[108]
    ),
    State(
        id=108,
        image_paths=[img_tg_105],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[109]
    ),
    State(
        id=109,
        image_paths=[img_tg_106],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[110]
    ),
    State(
        id=110,
        image_paths=[img_tg_107, img_tg_108],
        actions=[click] * 2,
        durations=[FREQUENCY] * 2,
        next_states=[111, 112]
    ),
    State(
        id=111,
        image_paths=[img_tg_108],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[112]
    ),
    State(
        id=112,
        image_paths=[img_tg_109, img_tg_111],
        actions=[click] * 2,
        durations=[FREQUENCY] * 2,
        next_states=[113, END_STATE_TRANSFER_GOLD]
    ),
    State(
        id=113,
        image_paths=[img_tg_110],
        actions=[held_mouse_left],
        durations=[FREQUENCY],
        next_states=[114]
    ), 
    State(
        id=114,
        image_paths=[img_tg_112],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[112]
    ),
    State(
        id=115,
        image_paths=[img_tg_112],
        actions=[click],
        durations=[FREQUENCY],
        next_states=[112]
    ),
    # State( # ! end state should be removed
    #     id=999,
    #     image_paths=[""],
    #     actions=["State machine stopped."],
    #     durations=[0],
    #     next_states=[-1]
    # )
]
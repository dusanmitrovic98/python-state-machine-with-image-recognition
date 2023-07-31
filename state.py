import time
import cv2

from config import FREQUENCY, NUM_BACKSPACES_PRESSES, PROCESS_ON_ENTER, PROCESS_ON_EXIT, TIMEOUT, timeout_counter
from generate_random_username import generate_random_username
from type_username import type_username, type_username_01
from held_mouse_left import held_mouse_left
from held_mouse_down import held_mouse_down
from held_mouse_up import held_mouse_up
from delete_input import delete_input
from move_cursor import move_cursor
from click_position import click
from logger import log

class State:
    def __init__(self, id: int, image_paths: list = None, actions: list = None, durations: list = None, next_states: list = None):
        self.id: int = id
        self.image_paths: list = image_paths if image_paths else []
        self.actions: list = actions if actions else []
        self.durations: list = durations if durations else []
        self.next_states: list = next_states if next_states else []
        self.pre_states: list[State] = []
        self.post_states: list[State] = []
        self.images = [cv2.imread(path) if path else None for path in self.image_paths] 

    def on_enter(self):
        if not PROCESS_ON_ENTER:
            return self.id
        for pre_state in self.pre_states:
            result_id = pre_state.process()
            if result_id:
                return result_id
        return None
 
    def on_exit(self):
        if not PROCESS_ON_EXIT:
            return self.id
        for post_state in self.post_states:
            result_id = post_state.process()
            if result_id:
                return result_id
        return self.id
    
    def process(self):
        global timeout_counter
        if timeout_counter > TIMEOUT: 
                timeout_counter = FREQUENCY
                return 1100
        recognized, index = self.is_image_recognized() or (False, -1)
        if recognized:
            time.sleep(self.durations[index])
            timeout_counter = FREQUENCY
            print(f"Timeout: {timeout_counter}")
            return self.next_states[index]
        else:
            time.sleep(1.0 / FREQUENCY)
            timeout_counter += FREQUENCY
            print(f"Timeout: {timeout_counter}")
            return None

    def process_with_pre_and_post_state(self):
        on_enter_result_id = self.on_enter()
        if on_enter_result_id:
            return on_enter_result_id
        result_id = self.process_with_post_state()
        if result_id:
            return result_id
        return self.id
    
    def process_with_post_state(self):
        result_id = self.process()
        if result_id:
            return result_id
        on_exit_result_id = self.on_exit()
        if on_exit_result_id:
            return on_exit_result_id
        return self.id

    def execute_action(self, max_loc, index):
        x, y = max_loc
        if self.actions[index]:
            if callable(self.actions[index]):
                if self.actions[index] is click:
                    self.actions[index]((self.images[index], x, y))
                elif self.actions[index] is held_mouse_up:
                    self.actions[index]((self.images[index], x, y))
                elif self.actions[index] is held_mouse_down:
                    self.actions[index]((self.images[index], x, y))
                elif self.actions[index] is held_mouse_left:
                    self.actions[index]((self.images[index], x, y))
                elif self.actions[index] is type_username:
                    self.actions[index]((generate_random_username()))
                elif self.actions[index] is type_username_01:
                    self.actions[index]()
                elif self.actions[index] is move_cursor:
                    self.actions[index]((x, y))
                elif self.actions[index] is delete_input:
                    self.actions[index](NUM_BACKSPACES_PRESSES)
            else:
                log(f"Performing action: {self.actions[index]}")

    def is_image_recognized(self):
        from recognize_image import recognize_image
        if self.images is None:
            return (False, -1)
        return recognize_image(self)

    def __str__(self):
        return f"State ID: {self.id}, Action: {self.actions}, Duration: {self.durations}, Next State: {self.next_states}, Pre states: {self.pre_states}, Post states: {self.post_states}"

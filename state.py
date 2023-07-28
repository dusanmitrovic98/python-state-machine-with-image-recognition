import time
import cv2

from generate_random_username import generate_random_username
from held_mouse_up import held_mouse_up
from type_username import type_username
from delete_input import delete_input
from move_cursor import move_cursor
from click_position import click
from logger import log

NUM_BACKSPACES_PRESSES = 13

class State:
    def __init__(self, id: int, image_paths: list = None, actions: list = None, durations: list = None, next_states: list = None):
        self.id: int = id
        self.image_paths: list = image_paths if image_paths else []
        self.actions: list = actions if actions else []
        self.durations: list = durations if durations else []
        self.next_states: list = next_states if next_states else []
        self.pre_state: State = None
        self.post_state: State = None
        self.images = [cv2.imread(path) if path else None for path in self.image_paths] 

    def on_enter(self, frequency = 1.0):
        if not self.pre_state:
            return None
        result_id = self.pre_state.process(frequency)
        if result_id:
            return result_id
        return None

    def on_exit(self, frequency = 1.0):
        if not self.post_state:
            return None 
        result_id = self.post_state.process(frequency)
        if result_id:
            return result_id
        return None
    
    def process(self, frequency = 1.0):
        recognized, index = self.is_image_recognized() or (False, -1)
        if recognized:
            time.sleep(self.durations[index])
            return self.next_states[index]
        else:
            time.sleep(1.0 / frequency)
            return self.id

    def process_with_pre_and_post_state(self, frequency = 1.0):
        on_enter_result_id = self.on_enter(frequency)  
        if on_enter_result_id:
            return on_enter_result_id
        result_id = self.process_with_post_state(frequency)
        if result_id:
            return result_id
        return None
    
    def process_with_pre_state(self, frequency = 1.0):
        on_enter_result_id = self.on_enter(frequency)  
        if on_enter_result_id:
            return on_enter_result_id 
        result_id = self.process(frequency)
        if result_id:
            return result_id
        return None

    def process_with_post_state(self, frequency = 1.0):
        result_id = self.process(frequency)
        if result_id:
            return result_id
        on_exit_result_id = self.on_exit(frequency)
        if on_exit_result_id:
            return on_exit_result_id  
        return None

    def execute_action(self, max_loc, index):
        x, y = max_loc
        if self.actions[index]:
            if callable(self.actions[index]):
                if self.actions[index] is click:
                    self.actions[index]((self.images[index], x, y))
                elif self.actions[index] is held_mouse_up:
                    self.actions[index]((self.images[index], x, y))
                elif self.actions[index] is type_username:
                    self.actions[index]((generate_random_username()))
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

    def __str__(self, index):
        return f"State ID: {self.id}, Action: {self.action[index]}, Duration: {self.duration}, Next State: {self.next_state}"
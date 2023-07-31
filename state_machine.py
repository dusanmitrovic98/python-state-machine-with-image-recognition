from typing import List
import threading

from config import START_STATE
from state import State
from logger import log

class StateMachine:
    def __init__(self, states: List[State], frequency: float = 1.0):
        self.states = {state.id: state for state in states}
        self.current_state = None
        self.frequency = frequency
        self.is_running = False
        self.lock = threading.Lock()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self._run()

    def stop(self):
        self.is_running = False

    def transition_to_next_state(self, next_state_id):
        if next_state_id in self.states:
            self.current_state = self.states[next_state_id]
        else:
            self.current_state = None

    def _run(self):
        while self.is_running:
            with self.lock:
                if self.current_state:
                    log(f"New state is being processed:  {self.current_state.id}") 
                    # next_state_id = self.current_state.process_with_pre_and_post_state(self.frequency)
                    next_state_id = self.current_state.process_with_pre_and_post_state()
                    self.transition_to_next_state(next_state_id)
                else:
                    if START_STATE in self.states:
                        self.current_state = self.states[1]
                    else:
                        self.is_running = False

from flask import Flask, jsonify

from state_machine import StateMachine
from states import STATES


FREQUENCY = 1.0
THRESHOLD = 0.9
states = STATES

app = Flask(__name__)

@app.route('/start')
def start_state_machine():
    state_machine.start()
    return jsonify({"status": "State machine started."})

@app.route('/stop')
def stop_state_machine():
    state_machine.stop()
    return jsonify({"status": "State machine stopped."})

@app.route('/current_state')
def get_current_state():
    return jsonify({"current_state": str(state_machine.current_state)})

if __name__ == "__main__":
    state_machine = StateMachine(states, frequency=FREQUENCY)
    state_machine.start()
    app.run()

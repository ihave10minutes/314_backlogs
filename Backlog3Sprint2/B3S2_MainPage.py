# Launchpad "Main Page" for Memory Sequence.
# Last edited 17th July, 4pm
# Latest Changes: Commented out submit buttons

import mido
import threading
import subprocess
import time
import B3S2_FunctionStorage as fs
import B3S2_LP_Game as gamelist

# Set up Launchpad MIDI ports for input and output
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # Output port for sending commands to Launchpad
inport = mido.open_input(midipad)  # Input port for receiving feedback from Launchpad

def pixel(buttonid, colour):
    """Function to light up 1 pixel."""
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

# Global variables to keep track of the running subprocess and mode
current_process = None
current_mode = None
start_button_active = True  # Flag to track if the start button is active
mode_buttons_active = False  # Flag to track if mode buttons are active
input_block = False


def terminate_current_process():
    """Function to terminate the current process if it exists."""
    global current_process
    if current_process:
        print("Terminating current process...")
        current_process.terminate()
        current_process.wait()
        current_process = None
        print("Process terminated.")

def start_easy_mode():
    """Function to start easy mode."""
    global current_process, current_mode
    if current_mode != 'easy':  # Only start if not already in easy mode
        terminate_current_process()
        print("Starting easy mode...")
        current_process = subprocess.Popen(['python', 'reaper/Backlog3Sprint2/easy_mode.py']) #File directory
        current_mode = 'easy'
        clear_board()
        light_mode_buttons()  # Ensure mode buttons remain lit


def start_hard_mode():
    """Function to start hard mode."""
    global current_process, current_mode
    if current_mode != 'hard':  # Only start if not already in hard mode
        terminate_current_process()
        print("Starting hard mode...")
        current_process = subprocess.Popen(['python', 'reaper/Backlog3Sprint2/hard_mode.py'])
        current_mode = 'hard'
        clear_board()
        light_mode_buttons()  # Ensure mode buttons remain lit

def clear_board():
    """Function to clear the LED board."""
    for i in range(0, 128):
        pixel(i, 0)

def light_mode_buttons(on=True):
    """Function to light up the mode buttons."""
    if on:
        pixel(17, 64)
        pixel(18, 72)
        
    else:
        pixel(17, 0)  # Button for easy mode
        pixel(18, 0)  # Button for hard mode
    
def block_modebuttons():
    global input_block
    input_block = True
    light_mode_buttons(False)
    time.sleep(1)
    input_block = False
    if not input_block:  # Ensure input_block is still False before lighting buttons
        light_mode_buttons(True)

"""def submit_button_easy():
    gamelist.easy_level_submit()

def submit_button_hard():
    gamelist.hard_level_submit()"""
    
def handle_midi_input():
    """Function to handle incoming MIDI messages."""
    global start_button_active, mode_buttons_active, input_block
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity > 0:
            if msg.note == 54 and start_button_active:
                start_button_active = False
                mode_buttons_active = True
                pixel(54, 0)  # Turn off the LED for button 54
                fs.SEQ_OrangeBtn()                
                start_easy_mode()  # Default to easy mode
                light_mode_buttons()  # Light up mode buttons
            elif msg.note == 18 and mode_buttons_active and not input_block:
                fs.MA3_Seq93()
                start_hard_mode()
            elif msg.note == 17 and mode_buttons_active and not input_block:
                fs.MA3_Seq94()
                start_easy_mode()
            elif msg.note == 11 and current_mode == 'easy' and not input_block:
                fs.SEQ_Easy()
                threading.Thread(target=block_modebuttons).start()
            elif msg.note == 12 and current_mode == 'hard' and not input_block:
                fs.SEQ_Hard()
                threading.Thread(target=block_modebuttons).start()

            """elif msg.note == 38 and current_mode == 'easy' and not input_block:
                submit_button_easy()
            elif msg.note == 48 and current_mode == 'hard' and not input_block:
                submit_button_hard()"""


def start_midi_listener():
    """Function to run the MIDI input handler in a separate thread."""
    listener_thread = threading.Thread(target=handle_midi_input)
    listener_thread.daemon = True
    listener_thread.start()

if __name__ == "__main__":
    # Light up button 54 as white to indicate it's the start button
    pixel(54, 127)  # 127 is usually the highest value for full brightness
    # Start listening for MIDI input
    start_midi_listener()
    # Keep the main thread alive
    while True:
        time.sleep(1)  # Prevent high CPU usage
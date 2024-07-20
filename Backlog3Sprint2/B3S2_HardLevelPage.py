# Launchpad "Hard Page" for Memory Sequence.
# Last edited 17th July, 5pm
# Latest Changes: Updated submit buttons

import mido
import time
import B3S2_LP_Game as gamelist

# Set up Launchpad MIDI ports for input and output
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # Output port for sending commands to Launchpad
inport = mido.open_input(midipad)  # Input port for receiving feedback from Launchpad

# Dictionary to store original colors for each button
ogcolour = {
    64: 10,  # Colors for NORTH  
    44: 4,   # Colors for SOUTH
    55: 40,  # Colors for EAST
    53: 30,  # Colors for WEST  
    54: 1,    # Colors for middle
    48: 74, # Color for submit
    12: 3 # Color for Start seq (Lock)
}

input_block = False

# Function to set the color of a specific button
def pixel(buttonid, colour):
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)  # Output command to Launchpad

# Function to initialize the buttons with their original colors
def initialize_buttons():
  
    buttonnorth(10)
    buttonsouth(4)
    buttonwest(30)
    buttoneast(40)
    middlebutton(1)
    startseqbutton(3)
    submitbutton(74)
   


# Individual button functions to set their colors
def buttonnorth(nbutton):
    pixel(64, nbutton)

def buttonsouth(sbutton):
    pixel(44, sbutton)

def buttonwest(wbutton):
    pixel(53, wbutton)

def buttoneast(ebutton):
    pixel(55, ebutton)

def middlebutton(mbutton):
    pixel(54, mbutton)
    
def startseqbutton(ss):
    pixel(12, 3)
    
def submitbutton(ss):
    pixel(48, 74)



# Function to draw a box with a specific color
def circularpath():
    buttonid = [83, 84, 85, 76, 67, 57, 47, 36, 25, 24, 23, 23, 32, 41, 51, 61, 72]
    startpixel = 0
    startsecondpixel = 1
    startthirdpixel = 2
    


    while True:
        # Turn off the previous LED
        pixel(buttonid[startpixel - 1], 0)
        pixel(buttonid[startsecondpixel - 1], 0)
        pixel(buttonid[startthirdpixel - 1], 0)
        
        # Turn on the current LED
        pixel(buttonid[startpixel], 3) 
        pixel(buttonid[startsecondpixel], 3) 
        pixel(buttonid[startthirdpixel], 3)
        # White color
        # Wait for a short period
        time.sleep(0.15)

        # Move to the next position
        startpixel = (startpixel + 1) % len(buttonid)
        startsecondpixel = (startsecondpixel + 1) % len(buttonid)
        startthirdpixel = (startthirdpixel + 1) % len(buttonid)
        
       

# Initialize buttons with their default colors
initialize_buttons()  

import threading
threading.Thread(target=circularpath, daemon=True).start()


# Functions to handle button presses and releases, updating colors
def pressnorth(): 
    global input_block
    if not input_block:
        print("NORTH")
        pixel(64, 3)  # Change color to indicate press
        gamelist.hard_add_front()
   
def releasenorth(): 
    global input_block
    if not input_block:
        pixel(64, ogcolour[64])  # Reset to original color on release
        

def presssouth(): 
    global input_block
    if not input_block:
        print("SOUTH")
        pixel(44, 3)  # Change color to indicate press
        gamelist.hard_add_back()
    
def releasesouth():  
    global input_block
    if not input_block:
        pixel(44, ogcolour[44])  # Reset to original color on release
    

def presswest():  
    global input_block
    if not input_block:
        print("WEST")
        pixel(53, 3)  # Change color to indicate press
        gamelist.hard_add_left()
   

def releasewest(): 
    global input_block
    if not input_block:
        pixel(53, ogcolour[53])  # Reset to original color on release
   

def presseast(): 
    global input_block
    if not input_block:
        print("EAST")
        pixel(55, 3)  # Change color to indicate press
        gamelist.hard_add_right()

def releaseeast(): 
    global input_block
    if not input_block:
        pixel(55, ogcolour[55])  # Reset to original color on release
    

def presssubmit():
    global input_block
    if not input_block:
        print("Input Sequence Submitted")
        gamelist.hard_level_submit()

def block_inputs():
    global input_block
    input_block = True
    blockedbuttons = [53, 55, 64, 44, 48]
    
    for button in blockedbuttons:
        pixel(12, 0)
        pixel(48, 0)
        time.sleep(14)

    for button in blockedbuttons:
        pixel(53, ogcolour[53])
        pixel(55, ogcolour[55])
        pixel(44, ogcolour[44])
        pixel(64, ogcolour[64])
        pixel(12, ogcolour[12])
        pixel(48, ogcolour[48])
    input_block = False

# Event loop to handle button press/release inputs from the Launchpad
for msg in inport:  # Input commands from Launchpad
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 64:
            if msg.velocity != 0:  # North button pressed
                pressnorth() 
            else:  # North button released
                releasenorth()  
        elif msg.note == 44:
            if msg.velocity != 0:  # South button pressed
                presssouth() 
            else:  # South button released
                releasesouth()  
        elif msg.note == 53:
            if msg.velocity != 0:  # West button pressed
                presswest() 
            else:  # West button released
                releasewest() 
        elif msg.note == 55:
            if msg.velocity != 0:  # East button pressed
                presseast()  
            else:  # East button released
                releaseeast()  
        elif msg.note == 48:
            if msg.velocity != 0:  # Submit button pressed
                presssubmit()           
        elif msg.note == 12:
            if not input_block:
                threading.Thread(target=block_inputs).start()
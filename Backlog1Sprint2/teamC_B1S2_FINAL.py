import RPi.GPIO as GPIO
import time
import tkinter as tk
import threading #important to have if GUI and relay module are to function properly simultaneously

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT) #Relay module set up normally open

def turn_on_laser(): 
    GPIO.output(21, GPIO.LOW) #Sends power to laser
    print('Laser ON')

def turn_off_laser():
    GPIO.output(21, GPIO.HIGH) #Removes power from laser
    print('Laser OFF')

def start_laser():
    bpm = int(bpm_enter.get())
    if bpm <= 0:
        print('Invalid BPM number. Please enter a proper BPM number')
    else:
        print(bpm)

        def pulsing_laser():
            while True:
                turn_on_laser()
                time.sleep(0.06)  # Laser on time (approx 60ms, or 1/1000th of a minute)
                turn_off_laser()
                time.sleep(60.0/bpm - 0.06)  # Ensures time for generated laser is accounted for
                if stop_laser_event.is_set():
                    break

        stop_laser_event.clear()
        threading.Thread(target=pulsing_laser).start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

def stop_laser():
    stop_laser_event.set()
    start_button.config(state=tk.NORMAL) #It's illogical to have start and stop run simulatenously
    stop_button.config(state=tk.DISABLED)

stop_laser_event = threading.Event()

main = tk.Tk()
main.title("Team C Laser Controller")

enter_bpm_here = tk.Label(main, text="Enter BPM here:")
bpm_enter = tk.Entry(main)
turnon_button = tk.Button(main, text="Turn On Laser", bg="GREEN", command=turn_on_laser)
turnoff_button = tk.Button(main, text="Turn Off Laser", bg="RED", command=turn_off_laser)
start_button = tk.Button(main, text="Start Laser", command=start_laser)
stop_button = tk.Button(main, text="Stop Laser", state=tk.DISABLED, command=stop_laser)

enter_bpm_here.grid(row=0, column=0, columnspan=2)
bpm_enter.grid(row=1, column=0, columnspan=2)
turnon_button.grid(row=2, column=0)
turnoff_button.grid(row=2, column=1)
start_button.grid(row=3, column=0)
stop_button.grid(row=3, column=1)

main.mainloop()
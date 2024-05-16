import tkinter as tk
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")
		
# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.104"		# laptop IP
PORT = 8000 # REAPER Local listen port
msg = float(1) # Trigger TRUE Value

def play_and_pause_func():
	send_message(PI_A_ADDR, PORT, "/action/40073", msg)

def firesnapshotone():
	send_message(PI_A_ADDR, PORT, "/action/40161", msg)

def firesnapshottwo():
	send_message(PI_A_ADDR, PORT, "/action/40162", msg)

def firesnapshotthree():
	send_message(PI_A_ADDR, PORT, "/action/40163", msg)

def firesnapshotfour():
	send_message(PI_A_ADDR, PORT, "/action/40164", msg)

main = tk.Tk()
main.title("Team C L-ISA Controller")

tabLabel=tk.Label(main,text="TEAM C GUI", font="20" )
play_and_pause_btn = tk.Button(main, text="Play/Pause",command=play_and_pause_func)
snapshotone_btn = tk.Button(main, text="Jump Marker ONE", bg="GREEN",command=firesnapshotone)
snapshottwo_btn = tk.Button(main, text="Jump Marker TWO", bg="RED",command=firesnapshottwo)
snapshotthree_btn = tk.Button(main, text="Jump Marker THREE", bg="BLUE",command=firesnapshotthree)
snapshotfour_btn = tk.Button(main, text="Jump Marker FOUR", bg="YELLOW",command=firesnapshotfour)


tabLabel.grid(row=0,column=0,columnspan=2)
play_and_pause_btn.grid(row=1,column=0,columnspan=2)
snapshotone_btn.grid(row=2,column=0)
snapshottwo_btn.grid(row=2,column=1)
snapshotthree_btn.grid(row=3,column=0)
snapshotfour_btn.grid(row=3,column=1)

main.mainloop()
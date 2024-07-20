from pythonosc import udp_client
import time

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")
		
# REAPER SETTINGS RIGHT HERE
REA_IP = "192.168.254.30"		# REAPER laptop IP
REA_PORT = 6800 # REAPER Local listen port
REA_MSG = float(1) # Trigger TRUE Value
# addr = "/action & /marker"

def REA_JumpLaserMarker(): #Marker 62, automatically plays
	send_message(REA_IP, REA_PORT, "/marker/62", REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Laser Marker 62 jumped')
	time.sleep(35)
	send_message(REA_IP, REA_PORT, "/action/1016", REA_MSG)
	
def REA_Stop(): #Stop Button
	send_message(REA_IP, REA_PORT, "/action/1016", REA_MSG)
	print('Stop')
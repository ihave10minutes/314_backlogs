# Function Storage for Memory Sequence.
# Last edited 10th July, 11am
# # Latest Changes: Added clear to Lose Sequence

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
		
# GRANDMA3 SETTINGS RIGHT HERE
MA3_IP = "192.168.254.229"		# MA3 laptop IP
MA3_PORT = 8888 # GRANDMA3 Local listen port
MA3_ADDR = "/gma3/cmd" # Trigger TRUE Value
# msg = "Go Sequence wtv"


# REAPER SETTINGS RIGHT HERE
REA_IP = "192.168.254.30"		# REAPER laptop IP
REA_PORT = 6800 # REAPER Local listen port
REA_MSG = float(1) # Trigger TRUE Value
# addr = "/action & /marker"

# GRANDMA3 CODE SEQUENCE

def MA3_Seq91(): # Suspense
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 91")
	print('Sequence 91 played')
	
def MA3_Seq92(): # Station Start
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 92")
	print('Sequence 92 played')

def MA3_Seq93(): # Hard
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 93")
	print('Sequence 93 played')
	
def MA3_Seq94(): # Easy
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 94")
	print('Sequence 94 played')

def MA3_Seq95(): # Laser Sequence Preparation
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 95")
	print('Sequence 94 played')

def MA3_Seq96(): # Lose
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 96")
	print('Sequence 96 played')
	
def MA3_Seq97(): # Win
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 97")
	print('Sequence 97 played')
	
def MA3_Clear():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	print('Sequence cleared')
	
# REAPER CODE SEQUENCE
# When jumping to markers, will automatically play as well

fm=54 # First marker in the timeline

def REA_JumpEasy(): #Marker 54
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm+1), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Easy Marker ' + str(fm+1) + ' jumped')

def REA_JumpHard(): #Marker 53
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Hard Marker ' + str(fm) + ' jumped')

def REA_JumpWin(): #Marker 58
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm+5), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Win Marker ' + str(fm+5) + ' jumped')

def REA_JumpLose(): #Marker 59
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm+6), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Lose Marker ' + str(fm+6) + ' jumped')	

def REA_JumpSampleBeat(): #Marker 55
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm+2), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Sample Marker ' + str(fm+2) + ' jumped')

def REA_JumpSuspense(): #Marker 56
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm+3), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('Suspense Marker ' + str(fm+3) + ' jumped')

def REA_JumpBGM(): #Marker 57
	send_message(REA_IP, REA_PORT, "/marker/"+str(fm+4), REA_MSG)
	send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
	print('BGM Marker ' + str(fm+4) +' jumped')	

def REA_PlayPause(): #Play/Pause
	send_message(REA_IP, REA_PORT, "/action/40073", REA_MSG)
	print('Play/Pause')

def REA_Pause(): #Pause - This function will not be shown on the GUI
	send_message(REA_IP, REA_PORT, "/action/1008", REA_MSG)
	print('Pause')
	
# SEQUENCE CODE SEQUENCE (These are functions stacked to make 1 bigger function)

def SEQ_Intro(): # Act 1 - Intro to our station with BGM
	MA3_Seq92()  # Sequence 92
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_JumpBGM() #Reaper 45, L-ISA 48
	time.sleep(65)
	REA_Pause()

def SEQ_OrangeBtn(): # Act 2 - Launchpad Start Button pressed
	MA3_Seq91() # Sequence 91
	REA_JumpSuspense() # Reaper 43, L-ISA 46
	time.sleep(10)
	REA_Pause()

def SEQ_Easy(): # Act 3 - Easy Level
	MA3_Seq94() # Sequence 94
	REA_JumpEasy() # Reaper 18, L-ISA 45
	time.sleep(50)
	REA_Pause()

def SEQ_Hard(): # Act 4 - Hard Level
	MA3_Seq93() # Sequence 93
	REA_JumpHard() # Reaper 46, L-ISA 44
	time.sleep(70)
	REA_Pause()

def SEQ_Win():# Act 5 - Win Sequence (test from easy AND hard level)
	MA3_Seq97() # Sequence 97
	REA_JumpWin() # Reaper 44, L-ISA 42
	time.sleep(8)
	REA_Pause()
	
def SEQ_Lose(): # Act 6 - Lose Sequence (test from easy AND hard level)
	MA3_Seq96() # Sequence 96
	REA_JumpLose() # Reaper 43, L-ISA 46
	time.sleep(9)
	REA_Pause()

def SEQ_SampleBeat(): # Act 7 - Sample Beat (no MA3)
	REA_JumpSampleBeat() # Reaper 42, L-ISA 47
	time.sleep(8)
	REA_Pause() # the difference between this and the Red button is the addition of the pause button at the end

def SEQ_Blackout(): # Act 8 - Blackout
	MA3_Clear()
	REA_Pause()
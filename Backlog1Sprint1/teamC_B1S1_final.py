import tkinter as tk
from pythonosc import udp_client, osc_message_builder
import time
import socket
import sys
import subprocess

main=tk.Tk()

#destroy ensures that when navigating from one page to another, every element in the navigated page is destroyed
def run_command(command):
    text = 'python3 command.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")

def run_recall(command):
    text = 'python3 recall.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")
        
def volume_up1():
    command = 'set MIXER:Current/InCh/Fader/Level 0 0 1000'
    run_command(command)
    time.sleep(1)

def volume_up2():
    command = 'set MIXER:Current/InCh/Fader/Level 1 0 1000'
    run_command(command)
    time.sleep(1)


def toggle_mute1():
    command = 'set MIXER:Current/InCh/Fader/On  0 0 0'
    run_command(command)
    time.sleep(1)

def toggle_mute2():
    command = 'set MIXER:Current/InCh/Fader/On  1 0 0'
    run_command(command)
    time.sleep(1)

def toggle_unmute1():
    command = 'set MIXER:Current/InCh/Fader/On  0 0 1'
    run_command(command)
    time.sleep(1)

def toggle_unmute2():
    command = 'set MIXER:Current/InCh/Fader/On  1 0 1'
    run_command(command)
    time.sleep(1)

def volume_down1():
    command = 'set MIXER:Current/InCh/Fader/Level 0 0 -32768'
    run_command(command)
    time.sleep(1)

def volume_down2():
    command = 'set MIXER:Current/InCh/Fader/Level 1 0 -32768'
    run_command(command)
    time.sleep(1)        

def send_message(receiver_ip, receiver_port, address, message):
  try:
    # Create an OSC client to send messages
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

    # Send an OSC message to the receiver
    client.send_message(address, message)

    print("Message sent successfully.")
  except:
    print("Message not sent")
        
def send_osc():
    # Define OSC message parameters and send OSC message
    PI_A_ADDR = "192.168.1.128"  # IP address of the receiving Raspberry Pi
    PORTQL1 = 49820  # Port of the receiving Raspberry Pi

    addr = "/print"
    msg = "salutations from pi_B"

    send_message(PI_A_ADDR, PORTQL1, addr, msg)        

LAPTOP_IP = "192.168.0.100"    # send to laptop w grandMA3
PORT = 8000                     # laptop w grandMA3 port number
addr = "/gma3/cmd"

def MA3_Fader1Up():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 2.201 At 100")

def MA3_Fader1Down():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 2.201 At 0")
        
def MA3_Fader2Up():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 2.202 At 100")

def MA3_Fader2Down():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 2.202 At 0")
        
def MA3_Fader1Go():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "Go Fader 201")

def MA3_Fader2Go():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "Go Fader 202")

def Main_Tab():
    def QL1_Tab():
        def backbutton():
            QL1PageLabel.destroy()
            QL1PageFader1Up.destroy()
            QL1PageFader2Up.destroy()
            QL1PageFader1Label.destroy()
            QL1PageFader2Label.destroy()
            QL1PageFader1Down.destroy()
            QL1PageFader2Down.destroy()
            QL1PageFader1Mute.destroy()
            QL1PageFader2Mute.destroy()
            QL1PageFader1Unmute.destroy()
            QL1PageFader2Unmute.destroy()
            QL1PageBackButton.destroy()
            Main_Tab()
        MainTabLabel.destroy()
        QL1PageButton.destroy()
        MA3PageButton.destroy()

        QL1PageLabel=tk.Label(main,text="QL1 Page", font="20" )
        QL1PageFader1Up=tk.Button(main,text="Up",font="20",command=volume_up1)
        QL1PageFader2Up=tk.Button(main,text="Up",font="20",command=volume_up2)
        QL1PageFader1Label=tk.Label(main,text="Fader 1", font="20")
        QL1PageFader2Label=tk.Label(main,text="Fader 2", font="20")
        QL1PageFader1Down=tk.Button(main,text="Down",font="20",command=volume_down1)
        QL1PageFader2Down=tk.Button(main,text="Down",font="20",command=volume_down2)
        QL1PageFader1Mute=tk.Button(main,text="Mute",font="20",command=toggle_mute1)
        QL1PageFader2Mute=tk.Button(main,text="Mute",font="20",command=toggle_mute2)
        QL1PageFader1Unmute=tk.Button(main,text="Unmute",font="20",command=toggle_unmute1)
        QL1PageFader2Unmute=tk.Button(main,text="Unmute",font="20",command=toggle_unmute2)
        QL1PageBackButton=tk.Button(main,text="Back",font="20", command=backbutton)
        
        QL1PageLabel.grid(row=0, column=0)
        QL1PageFader1Up.grid(row=1, column=0)
        QL1PageFader2Up.grid(row=1, column=1)
        QL1PageFader1Label.grid(row=2, column=0)
        QL1PageFader2Label.grid(row=2, column=1)
        QL1PageFader1Down.grid(row=3, column=0)
        QL1PageFader2Down.grid(row=3, column=1)
        QL1PageFader1Mute.grid(row=4, column=0)
        QL1PageFader2Mute.grid(row=4, column=1)
        QL1PageFader1Unmute.grid(row=5, column=0)
        QL1PageFader2Unmute.grid(row=5, column=1)
        QL1PageBackButton.grid(row=6, column=2)

    def MA3_Tab():
        def backbutton2():
            MA3PageLabel.destroy()
            MA3PageFader1Up.destroy()
            MA3PageFader2Up.destroy()
            MA3PageFader1Label.destroy()
            MA3PageFader2Label.destroy()
            MA3PageFader1Down.destroy()
            MA3PageFader2Down.destroy()
            MA3PageFader1Go.destroy()
            MA3PageFader2Go.destroy()
            MA3PageBackButton.destroy()
            Main_Tab()
        MainTabLabel.destroy()
        QL1PageButton.destroy()
        MA3PageButton.destroy()

        MA3PageLabel=tk.Label(main,text="MA3 Page", font="20")
        MA3PageFader1Up=tk.Button(main,text="Up",font="20",command=MA3_Fader1Up)
        MA3PageFader2Up=tk.Button(main,text="Up",font="20",command=MA3_Fader2Up)
        MA3PageFader1Label=tk.Label(main,text="Fader 1", font="20")
        MA3PageFader2Label=tk.Label(main,text="Fader 2", font="20")
        MA3PageFader1Down=tk.Button(main,text="Down",font="20",command=MA3_Fader1Down)
        MA3PageFader2Down=tk.Button(main,text="Down",font="20",command=MA3_Fader2Down)
        MA3PageFader1Go=tk.Button(main,text="Go",font="20",command=MA3_Fader1Go)
        MA3PageFader2Go=tk.Button(main,text="Go",font="20",command=MA3_Fader2Go)
        MA3PageBackButton=tk.Button(main,text="Back",font="20", command=backbutton2)
        MA3PageLabel.grid(row=0, column=0, columnspan=2)
        MA3PageFader1Up.grid(row=1, column=0)
        MA3PageFader2Up.grid(row=1, column=1)
        MA3PageFader1Label.grid(row=2, column=0)
        MA3PageFader2Label.grid(row=2, column=1)
        MA3PageFader1Down.grid(row=3, column=0)
        MA3PageFader2Down.grid(row=3, column=1)
        MA3PageFader1Go.grid(row=4, column=0)
        MA3PageFader2Go.grid(row=4, column=1)
        MA3PageBackButton.grid(row=5, column=2)
    
    MainTabLabel=tk.Label(main,text="TEAM C GUI MAIN PAGE", font="20" )
    QL1PageButton=tk.Button(main,text="QL1 Page",font="20",command=QL1_Tab)
    MA3PageButton=tk.Button(main,text="MA3 Page",font="20",command=MA3_Tab)
    
    MainTabLabel.grid(row=0, column=0, columnspan=2)
    QL1PageButton.grid(row=1, column=0)
    MA3PageButton.grid(row=1, column=1)

Main_Tab()
main.mainloop()
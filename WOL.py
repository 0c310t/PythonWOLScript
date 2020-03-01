import os
import time
from wakeonlan import send_magic_packet

phone = "1.1.1.1"     #My phone's static IP address
computer = "2.2.2.2" # My computer's static IP address
wol_counter = 0            #Increments when a WOL packet is sent to prevent spamming

while True:
        time.sleep(20)
        phone_response = os.system("ping -c 1 " + phone)
        #pc_response = os.system("ping -c 1 " + computer)
        if phone_response == 0:
                if wol_counter == 0:
                        print("Owner phone detected on network, sending magic packet...")
                        send_magic_packet('AA:BB:CC:DD:EE:FF') #Sends a WOL packet to my computer's MAC address 
                        wol_counter = wol_counter + 1
                else:
                        pc_response = os.system("ping -c 1 " + computer)
                        if pc_response != 0:
                                print("Owner computer still offline, resending magic packet...")
                                send_magic_packet('AA:BB:CC:DD:EE:FF')
                        else:
                                print("Owner phone and computer online, standing by...")
                                pass
        else:
                print("Owner phone offline, retrying...")
                pass

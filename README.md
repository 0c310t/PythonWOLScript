# PythonWOLScript
Turns on my computer when my phone connects to my home network. Not extremely practical, just a practice in wake on lan.

I assigned my phone's MAC address a static internal IP address on my network, which my script constantly pings to see if it is online. If my phone comes online, if I come home from work for example, it will send a wol packet to my computer's MAC address. It will then ping my computer's internal IP address (also a static IP) and keep resending wol packets until it hears a response. If both my phone and my computer are on, it will do nothing.

One issue is that when my phone goes to sleep, it stops responding to ping requests, so making the script ignore me turning off my computer but still using my phone on the network is a bit of a weird issue, since the script resets itself once my phone goes to sleep.

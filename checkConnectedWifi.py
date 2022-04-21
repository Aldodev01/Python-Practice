# import subprocess

# if "National Library of Indonesia" in subprocess.check_output("netsh wlan show interfaces"):
#     print("I am on school wifi!")


import subprocess

wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
data = wifi.decode('utf-8')
if "Zafran30" in data:
    print("connected to speccific wifi")
else:
    print("not connected")
import serial
import socket

def send(msg, target):
    ip = target['udp_ip']
    port = target['udp_port']
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(msg, (ip, port))

# AIS receiver at the serial port
serial_port = '/dev/serial0'
baud_rate = 38400

# Show the receive raw messages
debug = True

# Examples for UDP targets
targets = [
    {'name': 'marinetraffic', 'udp_ip': '5.9.207.224', 'udp_port': 5321},
    {'name': 'pocketmariner', 'udp_ip': '54.225.113.225', 'udp_port': 5322},
    {'name': 'shipfinder', 'udp_ip': '109.200.19.151', 'udp_port': 4001}
]
print ("Reading from serial port: " + serial_port)
for target in targets:
    print ("Sending to " + target['name'])
s = serial.Serial( serial_port, baud_rate, timeout=1 )
while True:
    line = s.readline()
    if line != '':
        if debug:
            print (line[:-1])
        for target in targets:
            send(line, target)
s.close()

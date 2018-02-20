# ais-forwarder
This Python script forwards AIS data from the serial port to several UDP hosts like a local OpenCPN installation, marinetraffic.com, aishub.net etc.<br>
I am using a dAISy HAT as AIS receiver on my Raspberry Pi 2. This extremely simple script has proven to be more reliable on my setup than some similar solutions which stopped feeding some of the UDP hosts after several hours without any warning messages.

Dependencies:<br>
pyserial is required and may be installed by "sudo pip install pyserial".

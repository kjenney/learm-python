import serial

# A simple script to do a single servo move on Servo1 (the one connected to the arm).

# CMD_SERVO_MOVE  3
# Header          0x55 0x55
# Length          Parameters + 2
# Low Time Value  01111000 (120)
#
# Parameters: Servo Number, Low Time, High Time
#
#   Header Ln Cm
# 0x55 0x55 8 3 1

import tinytuya

#Tuya implementation for turning on and off the lights

d = tinytuya.BulbDevice('[Device ID]', '[Device IP]', '[Local Key]')
d.set_version(3.3)
def turn_off():
    d.turn_off()

def turn_on():
    d.turn_on()
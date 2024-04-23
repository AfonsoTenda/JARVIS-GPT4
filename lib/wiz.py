import asyncio
from pywizlight import wizlight

#Wiz implementation for turning on and off the lights

light = wizlight("[Bulb IP]")

    
async def turn_on_ff():
    await light.turn_on()

def turn_on():
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(turn_on_ff())

async def turn_off_ff():
    await light.turn_off()

def turn_off():
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(turn_off_ff())
from os import system

def out(pin):
    system(f'gpio mode {pin} out')

def write(pin, state):
    system(f'gpio write {pin} {state}')
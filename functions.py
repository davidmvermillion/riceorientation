# Setup
from math import pi
from os import walk, path, chdir
from os.path import abspath, dirname

# Set directory to current script location
# https://stackoverflow.com/a/69556612/13801562
# chdir(dirname(abspath(__file__)))

def grain_orientation(radians):
    if radians >= pi/3 and radians <= 2*pi/3 or radians >= 4/3*pi and radians <= 5/3*pi:
        return 'Vertical'
    else:
        return 'not Vertical'

# https://stackoverflow.com/a/23326219/13801562
def number():
    while True:
        try:
            chosen_number = int(input('\nChoose a whole number between 1 and 15,000\n\n'))
            break
        except:
            print('Your answer must be an integer between 1 and 15,000. Try again!\n')
    return chosen_number

def rice_options():
    while True:
        try:
            rice = input('\nChoose one of the following rice varietals:\nArborio\nBasmati\nIpsala\nJasmine\nKaracadag\n\n')
            break
        except:
            print('\nYour answer must be one of the following rice varietals:\nArborio\nBasmati\nIpsala\nJasmine\nKaracadag\n\n')
    return rice
# import random
import numpy as np

## Settings
options     = 2
radius      = 3
lattice     = 15
timeSteps   = 25

## Calculations
numRules    = options**radius
numPossible = options**numRules

# Get the possible options with the specific radius
optList = []
for i in range(numRules):
    optList.append(format(i, f'0{radius}b'))

# Show the rules
rule = int(input(f'What rule would you like to select [0-{numPossible-1}]: '))
ruleBin = format(rule, f'0{numRules}b')

ruleDic = {} # Add the rules in a dictionary for easier look up
for idx, opt in enumerate(optList):
    ruleDic[opt] = ruleBin[idx]

print(ruleDic)

lat = np.random.randint(0,2,(1,lattice))[0]

print('Starting lattice:')
print(lat)
print('')

# Loop over the time steps
opt = [i for i in range(-1,lattice)]
opt.append(0)
newLat = [0 for i in range(0,lattice)]
for _ in range(timeSteps):
    print(lat)
    for idx in range(0, lattice):
        states = str(lat[opt[idx]])+str(lat[opt[idx+1]])+str(lat[opt[idx+2]])
        # print(states,'->', ruleDic[states])
        newLat[idx] = ruleDic[states]
    lat = newLat

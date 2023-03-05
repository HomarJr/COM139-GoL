import numpy as np


ON = 255

# STILL LIFES
block_array = np.array([[1, 1], 
                        [1, 1]])

beehive_array = np.array([ [0, 1, 1, 0], 
                           [1, 0, 0, 1], 
                           [0, 1, 1, 0]])

loaf_array = np.array([ [0, 1, 1, 0], 
                        [1, 0, 0, 1], 
                        [0, 1, 0, 1],
                        [0, 0, 1, 0]])

boat_array = np.array([ [1, 1, 0], 
                        [1, 0, 1], 
                        [0, 1, 0]])

tub_array = np.array([ [0, 1, 0], 
                       [1, 0, 1], 
                       [0, 1, 0]])


# OSCILATORS
blinker_arrays = [
    np.array([ [1], 
               [1], 
               [1]]),

    np.array([ [1, 1, 1]])
]
toad_arrays = [
    np.array([ [0, 0, 1, 0], 
               [1, 0, 0, 1], 
               [1, 0, 0, 1],
               [0, 1, 0, 0]]),

    np.array([ [0, 1, 1, 1], 
               [1, 1, 1, 0]])
]
toad_arrays_flipped = [
    np.array([ [0, 1, 0, 0], 
               [1, 0, 0, 1], 
               [1, 0, 0, 1],
               [0, 0, 1, 0]]),

    np.array([ [1, 1, 1, 0], 
               [0, 1, 1, 1]])
]
beacon_arrays = [
    np.array([ [1, 1, 0, 0], 
               [1, 1, 0, 0], 
               [0, 0, 1, 1],
               [0, 0, 1, 1]]),

    np.array([ [1, 1, 0, 0], 
               [1, 0, 0, 0], 
               [0, 0, 0, 1],
               [0, 0, 1, 1]])
]

# SPACHESHIPS
glider_arrays = [
    np.array([ [0, 1, 0], 
               [0, 0, 1], 
               [1, 1, 1]]),

    np.array([ [1, 0, 1], 
               [0, 1, 1], 
               [0, 1, 0]]),
    
    np.array([ [0, 0, 1], 
               [1, 0, 1], 
               [0, 1, 1]]),
    
    np.array([ [1, 0, 0], 
               [0, 1, 1], 
               [1, 1, 0]])
]
lw_spaceship_arrays = [
    np.array([ [1, 0, 0, 1, 0],
               [0, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [0, 1, 1, 1, 1]]),

    np.array([ [0, 0, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [1, 1, 1, 1, 0],
               [0, 1, 1, 0, 0]]),
    
    np.array([ [0, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 1],
               [1, 0, 0, 1, 0]]),
    
    np.array([ [0, 1, 1, 0, 0],
               [1, 1, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 1, 0]])
]


all_lifeforms_tuples = []

all_lifeforms_tuples += [[block_array*ON, 'block']] # perfectly simetrical shape                                                    
all_lifeforms_tuples += [[beehive_array*ON, 'beehive'], [np.rot90(beehive_array)*ON, 'beehive']] # vertical and horizontal
all_lifeforms_tuples += [[np.rot90(loaf_array, i)*ON, 'loaf'] for i in range(4)] # all rotations are different
all_lifeforms_tuples += [[np.rot90(boat_array, i)*ON, 'boat'] for i in range(4)] # all rotations are different
all_lifeforms_tuples += [[tub_array*ON, 'tub']] # perfectly simetrical shape

all_lifeforms_tuples += [[step*ON, 'blinker'] for step in blinker_arrays] # no need to rotate, include every step
all_lifeforms_tuples += [[np.rot90(step, i)*ON, 'toad'] for i in range(2) for step in toad_arrays] # vertical and horizontal, include every step
all_lifeforms_tuples += [[np.rot90(step, i)*ON, 'toad'] for i in range(2) for step in toad_arrays_flipped] # mirror case of last one
all_lifeforms_tuples += [[np.rot90(step, i)*ON, 'beacon'] for i in range(2) for step in beacon_arrays] # vertical and horizontal, include every step

all_lifeforms_tuples += [[np.rot90(step, i)*ON, 'glider'] for i in range(4) for step in glider_arrays] # all rotations are different, include every step
all_lifeforms_tuples += [[np.rot90(step, i)*ON, 'light-weight spaceship'] for i in range(4) for step in lw_spaceship_arrays] # all rotations are different, include every step


LIFEFORMS_TUPLES = all_lifeforms_tuples
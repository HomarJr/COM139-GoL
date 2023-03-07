'''
GoL.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
'''

import argparse, scipy, cv2
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from prettytable import PrettyTable
from datetime import datetime

from lifeforms import LIFEFORMS_TUPLES


ON = 255
KERNEL_3 = np.array([[1,1,1],
                     [1,9,1],
                     [1,1,1]])


def get_matches(grid, pattern):
    return {pt for pt in zip(*np.where(cv2.matchTemplate(grid.astype(np.uint8), pattern.astype(np.uint8), cv2.TM_CCORR_NORMED) >= 0.99)[::-1])}


def report_current_generation(grid):
    global current_generation, report_file_path, log

    # Gather data for each lifeform
    lifeforms = {'block':0, 'beehive':0, 'loaf':0, 'boat':0, 'tub':0, 'blinker':0, 'toad':0, 'beacon':0, 'glider':0, 'light-weight spaceship':0}

    for lifeform_tuple in LIFEFORMS_TUPLES:
        pattern, name = lifeform_tuple
        matches = get_matches(grid, pattern)
        if len(matches) > 0:
            lifeforms[name] += len(matches)
            if log: 
                for match in matches: print(f'{name} found at {match}')


    # Consolidate data
    total = max(sum(lifeforms.values()), 1)
    data = [
        ['Block', lifeforms['block'], round(lifeforms['block']/total*100, 2)],
        ['Beehive', lifeforms['beehive'], round(lifeforms['beehive']/total*100, 2)],
        ['Loaf', lifeforms['loaf'], round(lifeforms['loaf']/total*100, 2)],
        ['Boat', lifeforms['boat'], round(lifeforms['boat']/total*100, 2)],
        ['Tub', lifeforms['tub'], round(lifeforms['tub']/total*100, 2)],
        ['Blinker', lifeforms['blinker'], round(lifeforms['blinker']/total*100, 2)],
        ['Toad', lifeforms['toad'], round(lifeforms['toad']/total*100, 2)],
        ['Beacon', lifeforms['beacon'], round(lifeforms['beacon']/total*100, 2)],
        ['Glider', lifeforms['glider'], round(lifeforms['glider']/total*100, 2)],
        ['LG sp ship', lifeforms['light-weight spaceship'], round(lifeforms['light-weight spaceship']/total*100, 2)]
    ]


    # Write to report file
    with open(f'{report_file_path}.txt', 'a') as report:
        report.write(f'\n\nIteration: {current_generation}\n')
        
        table = PrettyTable([' ', 'Count', 'Percent'])
        table.align[' '] = 'l'
        table.align['Count'] = 'l'
        table.align['Percent'] = 'l'
        
        table.add_rows(data)
        table.add_row(['Total', sum(lifeforms.values()), ' '])

        list_of_table_lines = table.get_string().split('\n')
        horizontal_line = list_of_table_lines[0]
        report.write('\n'.join(list_of_table_lines[:-2]))
        report.write(f'\n{horizontal_line}\n')
        report.write('\n'.join(list_of_table_lines[-2:]))
        

def update(frameNum, img, grid):
    global generations, current_generation, log, disable_report
    
    # Stop condition for the simulation
    if current_generation == generations: return


    # The rules of Conway's Game of Life:
    #   - Any live cell with fewer than two live neighbours dies, as if by underpopulation. 
    #   - Any live cell with two or three live neighbours lives on to the next generation. (2+9, 3+9)
    #   - Any live cell with more than three live neighbours dies, as if by overpopulation. 
    #   - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction. (3)

    # Use a convolution and a mask to determine which cells are alive
    # (center cell has a weight of 9 and neighboors have a weight of 1)
    convolution = scipy.ndimage.convolve(grid, KERNEL_3, mode='constant')
    alive = (convolution==ON*3) | (convolution==ON*11) | (convolution==ON*12)
    next_grid = alive.astype(int)*ON


    # Generate report for current generation
    current_generation += 1
    if log: print(f'\n\n--- GENERATION {current_generation} ---')
    if not disable_report: report_current_generation(next_grid)


    # Update data
    img.set_data(next_grid)
    grid[:] = next_grid[:]
    return img,


def read_input_file(path):
    grid = np.array([])
    generations = w = h = 0

    with open(path) as f:
        lines = [line.rstrip() for line in f]

        w, h = [int(s) for s in lines[0].split(' ')]
        generations = int(lines[1])

        grid = np.zeros(w*h).reshape(w, h)
        for line in lines[2:]:
            x, y = [int(s) for s in line.split(' ')]
            grid[x, y] = ON

    return grid, generations


def main():
    global generations, current_generation, report_file_path, log, disable_report

    # Parse CLI arguments
    parser = argparse.ArgumentParser(
        prog="Conway's Game of Life",
        description="Runs Conway's Game of Life simulation and writes a report about the simulation."
    )
    parser.add_argument('--configuration_file', help='path to configuration input file', type=str, required=True)
    parser.add_argument('--animation_interval', help='delay between animation frames in milliseconds.', default=50, type=int, required=False)
    parser.add_argument('--log', help='use to enable logging', action='store_true', required=False)
    parser.add_argument('--disable_report', help='use to disable report generation', action='store_true', required=False)
    args = parser.parse_args()
    log = args.log
    disable_report = args.disable_report


    # Read input file configurations and do initial set up
    grid, generations = read_input_file(args.configuration_file)

    if not disable_report:
        start = datetime.now()
        report_header = f"Simulation at {start.strftime('%Y-%m-%d')}\nUniverse size {grid.shape[0]} x {grid.shape[1]}"
        report_file_path = f"Simulation Report - {start.strftime('%Y-%m-%d %H-%M')}"
        with open(f'{report_file_path}.txt', 'w+') as report: report.write(report_header)

    current_generation = 0
    if not disable_report: report_current_generation(grid)


    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='none')
    _ = animation.FuncAnimation(fig, update, fargs=(img, grid, ), interval=args.animation_interval, save_count=100, repeat=False)
    plt.show()



if __name__ == '__main__':
    main()

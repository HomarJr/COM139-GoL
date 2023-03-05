import os, sys, csv


files = os.listdir(sys.argv[1])

for file in files:
    input_path = os.path.join(sys.argv[1], file)
    output_path = ''.join(input_path.split('.')[:-1])

    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        reader = csv.reader(input_file)
        for y, row in enumerate(reader):
            for x, cell in enumerate(row):
                if cell == '1': output_file.write(f"{x},{y}\n")

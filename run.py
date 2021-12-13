
import os
from itertools import cycle
import time

'''run this file to execute the program'''

'''cycles between the two datasets to simulate changing camera footage'''
mydataset = ['1','2']
data_cycle = cycle(mydataset)
while True:
    '''edits run_config.yml to read new dataset'''
    path = 'PeekingDuck/data'
    files = os.listdir(path)
    result = [i for i in files if i.startswith('stats')]
    df = os.remove('PeekingDuck/data/' + str(result[0]))
    a_file = open("run_config.yml", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = "    input_dir : 'input/data" + next(data_cycle) + "'\n"

    a_file = open("run_config.yml", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

    os.system("peekingduck run")
    os.system("python3 python.py")
    print("updated!")
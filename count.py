from os import listdir
from os.path import isfile, join, isdir
from scipy import stats
import numpy as np


def save_log_to_file(string, file):
    text_file = open(file, "w")
    n = text_file.write(string)
    text_file.close()

def print_basic_statistics(arr):
    mean = np.mean(arr)
    median = np.median(arr)
    
    # measures of dispersion
    min = np.amin(arr)
    max = np.amax(arr)
    range = np.ptp(arr)
    varience = np.var(arr)
    sd = np.std(arr)
    
    print("Descriptive analysis")
    print("Amount of files =", len(arr))
    print("Measures of Central Tendency")
    print("Mean =", mean)
    print("Median =", median)
    print("Measures of Dispersion")
    print("Minimum =", min)
    print("Maximum =", max)
    print("Range =", range)
    print("Varience =", varience)
    print("Standard Deviation =", sd)


FILESE_LINES_SIZES = []
STR_MANIPULATION_ERRORS_MESSAGES = ''

def count_lines_of_code(path):
    global STR_MANIPULATION_ERRORS_MESSAGES
    try:
        if isfile(path):
            if path.endswith('.ts'):
                num_lines = sum(1 for line in open(path))
                FILESE_LINES_SIZES.append(num_lines)
                print(f"Number of lines in {path} : {num_lines}")
        else:
            ficheros = listdir(path)
            for fichero in ficheros:
                count_lines_of_code(join(path, fichero))
    except UnicodeDecodeError:
        STR_MANIPULATION_ERRORS_MESSAGES += f"Error manipulating {path} \n"
        print(f"Error manipulating {path}")

PATH = r'E:\UNI\DECIMO CICLO SEGUNDA PARTE\CALIDAD DE SOFTWARE\mini-diary-master\src'
count_lines_of_code(PATH)

save_log_to_file(STR_MANIPULATION_ERRORS_MESSAGES, './logs_errors.txt')
print_basic_statistics(FILESE_LINES_SIZES)
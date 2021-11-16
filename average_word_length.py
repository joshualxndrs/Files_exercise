import os
import re
os.chdir('C:\\Users\\josua\\Documents\\CS_SEM1\\ALGOPROG\\ALGOPRO_HW\\Files_exercise')

def calc_length(text_path):
    file = open(text_path)
    words_length = re.findall('\w+', file.read())
    
    return sum([len(word) for word in words_length]) / len(words_length)


if __name__ == "__main__":
    print(calc_length('C:\\Users\\josua\\Documents\\CS_SEM1\\ALGOPROG\\ALGOPRO_HW\\Files_exercise\\south africa flowers edited.txt'))
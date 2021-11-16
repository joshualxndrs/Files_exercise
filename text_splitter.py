import re
import os

os.chdir('C:\\Users\\josua\\Documents\\CS_SEM1\\ALGOPROG\\ALGOPRO_HW\\Files_exercise')

def splitter(text_file):
    text_file = open(text_file)
    content_read = text_file.read()

    text_contents = re.split(r'(?<=[^A-Z].[.?!]) +(?=[A-Z])', content_read)
    for words in text_contents:
        print(words)


splitter('C:\\Users\\josua\\Documents\\CS_SEM1\\ALGOPROG\\ALGOPRO_HW\\Files_exercise\\example4.txt')
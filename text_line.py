import os
os.chdir('C:\\Users\\josua\\Documents\\CS_SEM1\\ALGOPROG\\ALGOPRO_HW\\Files_exercise')

text_path = 'C:\\Users\\josua\Documents\\CS_SEM1\\ALGOPROG\\ALGOPRO_HW\\Files_exercise\\example 2'
open_path = open(text_path, 'r')
new_text = open('new_text.txt', 'w')
text = open_path.read().split("\n")
x = 1

while x < len(text):
    text[x] = str(x) + ". " + text[x] + "\n"
    new_text.write(text[x])
    x += 1
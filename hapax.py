import string
text_path = 'south africa flowers edited.txt'
text_open = (text_path, 'r')
text = text_open.read().lower().replace("\n","")

new_text = ""
for i in text:
    if i not in string.punctuation:
        new_text += i

text =new_text
splits = text.split(" ")
d = {}
for x in splits:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

newd = []
for x in d:
    if d[x] == 1:
        newd.append(x)
print("Here are the lists of happaxes found in this text: ")

for word in newd:
    print(word)
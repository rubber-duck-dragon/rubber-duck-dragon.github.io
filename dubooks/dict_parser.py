# create lists of hsk vocab

with open('hsk_l1.txt') as file:
    lines = file.read().split('\n')
    hsk1 = list(lines)

with open('hsk_l2.txt') as file:
    lines = file.read().split('\n')
    hsk2 = list(lines)

with open('hsk_l3.txt') as file:
    lines = file.read().split('\n')
    hsk3 = list(lines)

with open('hsk_l4.txt') as file:
    lines = file.read().split('\n')
    hsk4 = list(lines)

with open('hsk_l5.txt') as file:
    lines = file.read().split('\n')
    hsk5 = list(lines)

with open('hsk_l6.txt') as file:
    lines = file.read().split('\n')
    hsk6 = list(lines)

#open CEDICT file

with open('cedict_sample.u8') as file:
    text = file.read()
    lines = text.split('\n')
    dict_lines = list(lines)
    dict_lines.remove('')

#define functions

def parse_line(line):
    parsed = {}
    line = line.rstrip('/')
    line = line.split('/')
    trans = line[1]
    line[0].rstrip(']')
    char_and_pinyin = line[0].split('[')
    character = char_and_pinyin[0].rstrip(' ')
    pinyin = char_and_pinyin[1]
    parsed['char'] = character
    parsed['pinyin'] = pinyin
    parsed['trans'] = trans
    list_of_dicts.append(parsed)

def find_hsk_level(x):
    if x['char'] in hsk1:
        x['hsk'] = 1
    elif x['char'] in hsk2:
        x['hsk'] = 2
    elif x['char'] in hsk3:
        x['hsk'] = 3
    elif x['char'] in hsk4:
        x['hsk'] = 4
    elif x['char'] in hsk5:
        x['hsk'] = 5
    elif x['char'] in hsk6:
        x['hsk'] = 6
    else: 
        x['hsk'] = 0
        

list_of_dicts = []

#make each line into a dictionary
for line in dict_lines:
        parse_line(line)

#add hsk level as a value to each dict
for dict in list_of_dicts:
    find_hsk_level(dict)
    
print(list_of_dicts)
    # line = character + ',' + pinyin + ',' + trans
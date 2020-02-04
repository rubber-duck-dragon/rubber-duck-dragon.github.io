from django.core.management.base import BaseCommand, CommandError
from vocab.models import Word 

class Command(BaseCommand):
    #open the HSK files
    def handle(self, *args, **options):
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

        with open('cedict_ts.u8') as file:
            text = file.read()
            lines = text.split('\n')
            dict_lines = list(lines)
    

        #define functions

        def parse_line(line):
            parsed = {}
            if line == '':
                dict_lines.remove(line)
                return 0
            line = line.rstrip('/')
            line = line.split('/')
            if len(line) <= 1:
                return 0
            english = line[1]
            char_and_pinyin = line[0].split('[')
            characters = char_and_pinyin[0]
            characters = characters.split()
            traditional = characters[0]
            simplified = characters[1]
            pinyin = char_and_pinyin[1]
            pinyin = pinyin.rstrip()
            pinyin = pinyin.rstrip("]")
            parsed['traditional'] = traditional
            parsed['simplified'] = simplified
            parsed['pinyin'] = pinyin
            parsed['english'] = english
            list_of_dicts.append(parsed)
    
        def remove_surnames():
            for x in range(len(list_of_dicts)-1, -1, -1):
                if "surname " in list_of_dicts[x]['english']:
                    if list_of_dicts[x]['traditional'] == list_of_dicts[x+1]['traditional']:
                        list_of_dicts.pop(x)

        def find_hsk_level(x):
            if x['simplified'] in hsk1:
                x['hsk'] = 1
            elif x['simplified'] in hsk2:
                x['hsk'] = 2
            elif x['simplified'] in hsk3:
                x['hsk'] = 3
            elif x['simplified'] in hsk4:
                x['hsk'] = 4
            elif x['simplified'] in hsk5:
                x['hsk'] = 5
            elif x['simplified'] in hsk6:
                x['hsk'] = 6
            else: 
                x['hsk'] = 0
                

        list_of_dicts = []

        #make each line into a dictionary
        print("Parsing dictionary . . .")
        for line in dict_lines:
                parse_line(line)

        #remove entries for surnames from the data
        print("Removing Surnames . . .")
        remove_surnames()

        #add hsk level as a value to each dict
        print("Searching HSK . . .")
        for dict in list_of_dicts:
            find_hsk_level(dict)

        #save to the database
        print("Saving to database (this may take a few minutes) . . .")
        for one_dict in list_of_dicts:
            new_word = Word(traditional = one_dict["traditional"], simplified = one_dict["simplified"], english = one_dict["english"], pinyin = one_dict["pinyin"], hsk = one_dict["hsk"])
            new_word.save()
        print('Done!')


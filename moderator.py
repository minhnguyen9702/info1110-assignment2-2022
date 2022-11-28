"""
Author: Nguyen Nguyen Nhat Minh
SID: 510190381
Unikey: nngu8085
"""

# importing sys is important here because I will use it later
# in order to use command line arguments.
import sys

# Validation functions: these are the functions I wrote that
# I am going to use in order to validate different parts of the code
# later on
def is_valid_name(name):
    if not type(name) == str:
        return False
    if name == "" or name.isspace():
        return False
    else:
        i = 0
        while i < len(name):
            if name[i].isalpha() or name[i].isspace() or name[i] == "-":
                i += 1
            else:
                return False
    return True

def is_valid_date(date):
    if not type(date) == str:
        return False
    if len(date) == 19:
        if (date[4] == "-" and date[7] == "-" and 
        date[10] == "T" and date[13] == ":" and
        date[16] == ":"):
            if (date[0].isnumeric() and date[1].isnumeric() and
            date[2].isnumeric() and date[3].isnumeric() and
            date[5].isnumeric() and date[6].isnumeric() and
            date[8].isnumeric() and date[9].isnumeric() and
            date[11].isnumeric() and date[12].isnumeric() and
            date[14].isnumeric() and date[15].isnumeric() and
            date[17].isnumeric() and date[18].isnumeric()):
                return True
    return False

def is_valid_score(score):
    try:
        if -10 <= int(score) <= 10:
            return True
    except:
        return False

def is_valid_header(filename):
    try:
        if type(filename) == str:
            i = 0
            ls = []
            f = open(filename)
            while i < 2:
                ls.append(f.readline())
                i += 1
            f.close()
            if not ls[0] == "\n" and ls[1] == "\n":
                return True
        return False
    except:
        return

def get_file(task):
    ls = sys.argv
    i = 0
    while i < len(ls):
        if ls[i] == task:
            return ls[i+1]
        i += 1

def reformat_date(date):
    date = date.strip()
    date = date.replace("/t", "")
    date = date.replace("-", "")
    date = date.replace("T", "")
    date = date.replace(":", "")
    return date


# part 2
# this is a function that I wrote specifically to answer Part 2
# 
def command_check(ls):
    command_ls = ["task", "log", "forum", "words", "people"]
    i = 0
    while i < len(ls):
        if ls[i] == "-task":
            if (
                ls[i + 1] == "rank_people"
                or ls[i + 1] == "validate_forum"
                or ls[i + 1] == "censor_forum"
                or ls[i + 1] == "evaluate_forum"
            ):
                command_ls.remove("task")
            else:
                return "Task argument is invalid.", False
        elif ls[i] == "-log":
            command_ls.remove("log")
        elif ls[i] == "-forum":
            command_ls.remove("forum")
            try:
                f = open(ls[i + 1])
                f.close()
            except:
                return f"{ls[i+1]} cannot be read.", False
        elif ls[i] == "-words":
            command_ls.remove("words")
            try:
                f = open(ls[i + 1])
                f.close()
            except:
                return f"{ls[i+1]} cannot be read.", False
        elif ls[i] == "-people":
            command_ls.remove("people")
            try:
                f = open(ls[i + 1])
                f.close()
            except:
                return f"{ls[i+1]} cannot be read.", False
        i += 1
    if command_ls == []:
        return "Moderator program starting...", True
    else:
        return f"No {command_ls[0]} arguments provided.", False

result = command_check(sys.argv)
print(result[0])

# part 3 the reason i'm making this a function. is so that I can have early returns
# and stop doing part 3 if necessary

def get_people_ls():
    f = open(get_file("-people"))
    f.readline()
    f.readline() #these two f.readline() statments skip over the header
    ls = []
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.strip()
        line = line.split(",")
        ls.append(line)
    return(ls)

def is_valid_people():
    if is_valid_header(get_file("-people")):
        ls = get_people_ls()
        i = 0
        while i < len(ls):
            if is_valid_name(ls[i][0]):
                if is_valid_score((ls[i][1])):
                    i += 1
                else:
                    f = open(get_file("-log"), "w")
                    f.write(f"Error: people file read. The personality score is invalid on line {i+3}\n")
                    f.close()
                    return False
            else:
                f = open(get_file("-log"), "w")
                f.write(f"Error: people file read. The user's name is invalid on line {i+3}\n")
                f.close()
                return False
        f = open(get_file("-log"), "w")
        f.write("")
        f.close()
        return True
    else:
        f = open(get_file("-log"), "w")
        f.write("Error: people file read. The people file header is incorrectly formatted\n")
        f.close()
        return False

# I had to implement a bubble sort algorithim because we weren't allowed to use
# lambda >:( and i did it WITH ONLY WHILE LOOPS
def sort_people():
    ls = get_people_ls()
    i = 0
    while i < len(ls):
        i2 = 0
        while i2 < (len(ls) - 1 - i):
            if int(ls[i2][1]) < int(ls[i2+1][1]):
                ls[i2], ls[i2+1] = ls[i2+1], ls[i2]
            i2 += 1
        i += 1
    ls2 = []
    i3 = 0
    f = open(get_file("-people"))
    while i3 < 2:
        ls2.append(f.readline())
        i3 += 1
    f.close()
    i4 = 0
    while i4 < len(ls):
        ls[i4] = ls[i4][0]+","+ls[i4][1]+"\n"
        i4 += 1
    ls = ls2 + ls
    i5 = 0
    f = open(get_file("-people"), "w")
    while i5 < len(ls):
        f.write(ls[i5])
        i5 += 1
    f.close()
    return ls

if get_file("-task") == "rank_people":
    if is_valid_people():
        sort_people()
#part 4

def is_valid_forum():
    if is_valid_header(get_file("-forum")):
        f = open(get_file("-forum"))
        f.readline()
        f.readline()
        i = 0
        i2 = -1
        all_dates = []
        file_structure = []

        while True:
            line = f.readline()
            line2 = f.readline()
            line3 = f.readline()
            if line == "":
                break
            
            if line.find("\t") != 0:
                if line2.find("\t") == 0:
                    f2 = open(get_file("-log"), "w")
                    f2.write(f"Error: forum file read. The post has an invalid format on line {2 + 2 + (i*3)}\n")
                    f2.close()
                    return False
                elif line3.find("\t") == 0:
                    f2 = open(get_file("-log"), "w")
                    f2.write(f"Error: forum file read. The post has an invalid format on line {2 + 3 + (i*3)}\n")
                    f2.close()
                    return False
                else:
                    temp = reformat_date(line)
                    temp_ls = []
                    temp_ls.append(temp)
                    all_dates.append(temp_ls)
                    i2 += 1
                    file_structure.append("post")

            if line.find("\t") == 0:
                if line2.find("\t") != 0:
                    f2 = open(get_file("-log"), "w")
                    f2.write(f"Error: forum file read. The post has an invalid format on line {2 + 2 + (i*3)}\n")
                    f2.close()
                    return False
                elif line3.find("\t") != 0:
                    f2 = open(get_file("-log"), "w")
                    f2.write(f"Error: forum file read. The post has an invalid format on line {2 + 3 + (i*3)}\n")
                    f2.close()
                    return False
                else:
                    temp = reformat_date(line)
                    all_dates[i2].append(temp)
                    file_structure.append("reply")

            temp = line.strip()
            temp = temp.replace("\t", "")
            if is_valid_date(temp) == False:
                f2 = open(get_file("-log"), "w")
                f2.write(f"Error: forum file read. The datetime string is invalid on line {2 + 1 + (i*3)}\n")
                f2.close()
                return False

            temp = line2.strip()
            temp = temp.replace("\t", "")
            if is_valid_name(temp) == False:
                f2 = open(get_file("-log"), "w")
                f2.write(f"Error: forum file read. The user's name is invalid on line {2 + 2 + (i*3)}\n")
                f2.close()
                return False

            i += 1
# the only time a reply can be in front of the post is at the very beginning on line 3
        if file_structure[0] != "post": 
            f2 = open(get_file("-log"), "w")
            f2.write("Error: forum file read. The reply is placed before a post on line 3\n")
            f2.close()
            return False

        i3 = 1
        i4 = 0
        while i4 < len(all_dates):
            i5 = 0
            while i5 < (len(all_dates[i4]) - 1):
                if all_dates[i4][i5] < all_dates[i4][i5+1]:
                    i3 += 1
                    i5 += 1
                else:
                    f2 = open(get_file("-log"), "w")
                    f2.write(f"Error: forum file read. The reply is out of chronological order on line {3 + i3*3}\n")
                    f2.close()
                    return False
            i3 += 1
            i4 += 1

        i6 = 0
        i7 = 0
        while i6 < (len(all_dates) - 1):
            i7 += len(all_dates[i6])
            if all_dates[i6][0] < all_dates[i6+1][0]:
                i6 += 1
            else:
                f2 = open(get_file("-log"), "w")
                f2.write(f"Error: forum file read. The post is out of chronological order on line {3 + i7*3}\n")
                f2.close()
                return False
            
        f.close()
        f = open(get_file("-log"), "w")
        f.write("")
        f.close()
        return True
    else:
        f = open(get_file("-log"), "w")
        f.write("Error: forum file read. The forum file header is incorrectly formatted\n")
        f.close()
        return False
# if i were to redo this assignment, I'd defintely make a function 
# for writing error messages.

if get_file("-task") == "validate_forum" and result[1] == True:
    is_valid_forum()

# part 5

def is_valid_words():
    if is_valid_header(get_file("-words")):
        f = open(get_file("-words"))
        lines = f.readlines()
        del lines[0:2]
        i = 0

        while i < len(lines):
            if lines[i].find("\n") != (len(lines[i]) - 1): # if banned word doesn't end with "\n"
                f2 = open(get_file("-log"), "w")
                f2.write(f"Error: words file read. The banned word is invalid on line {3 + i}\n")
                f2.close()
                return False
            if lines[i].isspace():
                f2 = open(get_file("-log"), "w")
                f2.write(f"Error: words file read. The banned word is invalid on line {3 + i}\n")
                f2.close()
                return False
            if lines[i] == "":
                f2 = open(get_file("-log"), "w")
                f2.write(f"Error: words file read. The banned word is invalid on line {3 + i}\n")
                f2.close()
                return False
            i+=1
        f.close()

        f = open(get_file("-log"), "w")
        f.write("")
        f.close()
        return True
    else:
        f = open(get_file("-log"), "w")
        f.write("Error: words file read. The words file header is incorrectly formatted\n")
        f.close()
        return False

def get_words():
    f = open(get_file("-words"))
    lines = f.readlines()
    del lines[0:2]
    i = 0
    while i < len(lines):
        lines[i] = lines[i].strip()
        i += 1
    return lines
# i need all of these to account for every possible combination, 
# 100 string.replaces() in all
def censor_word(word:str, message:str):
    message = message.replace(f" {word} ", " "+len(word)*"*"+" ")
    message = message.replace(f" {word}\n", " "+len(word)*"*"+"\n")
    message = message.replace(f" {word}\t", " "+len(word)*"*"+"\t")
    message = message.replace(f" {word},", " "+len(word)*"*"+",")
    message = message.replace(f" {word}.", " "+len(word)*"*"+".")
    message = message.replace(f" {word}'", " "+len(word)*"*"+"'")
    message = message.replace(f' {word}"', " "+len(word)*"*"+'"')
    message = message.replace(f" {word}!", " "+len(word)*"*"+"!")
    message = message.replace(f" {word}?", " "+len(word)*"*"+"?")
    message = message.replace(f" {word}(", " "+len(word)*"*"+"(")
    message = message.replace(f" {word})", " "+len(word)*"*"+")")

    message = message.replace(f"\n{word} ", "\n"+len(word)*"*"+" ")
    message = message.replace(f"\n{word}\n", "\n"+len(word)*"*"+"\n")
    message = message.replace(f"\n{word}\t", "\n"+len(word)*"*"+"\t")
    message = message.replace(f"\n{word},", "\n"+len(word)*"*"+",")
    message = message.replace(f"\n{word}.", "\n"+len(word)*"*"+".")
    message = message.replace(f"\n{word}'", "\n"+len(word)*"*"+"'")
    message = message.replace(f'\n{word}"', "\n"+len(word)*"*"+'"')
    message = message.replace(f"\n{word}!", "\n"+len(word)*"*"+"!")
    message = message.replace(f"\n{word}?", "\n"+len(word)*"*"+"?")
    message = message.replace(f"\n{word}(", "\n"+len(word)*"*"+"(")
    message = message.replace(f"\n{word})", "\n"+len(word)*"*"+")")

    message = message.replace(f"\t{word} ", "\t"+len(word)*"*"+" ")
    message = message.replace(f"\t{word}\n", "\t"+len(word)*"*"+"\n")
    message = message.replace(f"\t{word}\t", "\t"+len(word)*"*"+"\t")
    message = message.replace(f"\t{word},", "\t"+len(word)*"*"+",")
    message = message.replace(f"\t{word}.", "\t"+len(word)*"*"+".")
    message = message.replace(f"\t{word}'", "\t"+len(word)*"*"+"'")
    message = message.replace(f'\t{word}"', "\t"+len(word)*"*"+'"')
    message = message.replace(f"\t{word}!", "\t"+len(word)*"*"+"!")
    message = message.replace(f"\t{word}?", "\t"+len(word)*"*"+"?")
    message = message.replace(f"\t{word}(", "\t"+len(word)*"*"+"(")
    message = message.replace(f"\t{word})", "\t"+len(word)*"*"+")")

    message = message.replace(f",{word} ", ","+len(word)*"*"+" ")
    message = message.replace(f",{word}\n", ","+len(word)*"*"+"\n")
    message = message.replace(f",{word}\t", ","+len(word)*"*"+"\t")
    message = message.replace(f",{word},", ","+len(word)*"*"+",")
    message = message.replace(f",{word}.", ","+len(word)*"*"+".")
    message = message.replace(f",{word}'", ","+len(word)*"*"+"'")
    message = message.replace(f',{word}"', ","+len(word)*"*"+'"')
    message = message.replace(f",{word}!", ","+len(word)*"*"+"!")
    message = message.replace(f",{word}?", ","+len(word)*"*"+"?")
    message = message.replace(f",{word}(", ","+len(word)*"*"+"(")
    message = message.replace(f",{word})", ","+len(word)*"*"+")")

    message = message.replace(f".{word} ", "."+len(word)*"*"+" ")
    message = message.replace(f".{word}\n", "."+len(word)*"*"+"\n")
    message = message.replace(f".{word}\t", "."+len(word)*"*"+"\t")
    message = message.replace(f".{word},", "."+len(word)*"*"+",")
    message = message.replace(f".{word}.", "."+len(word)*"*"+".")
    message = message.replace(f".{word}'", "."+len(word)*"*"+"'")
    message = message.replace(f'.{word}"', "."+len(word)*"*"+'"')
    message = message.replace(f".{word}!", "."+len(word)*"*"+"!")
    message = message.replace(f".{word}?", "."+len(word)*"*"+"?")
    message = message.replace(f".{word}(", "."+len(word)*"*"+"(")
    message = message.replace(f".{word})", "."+len(word)*"*"+")")

    message = message.replace(f"'{word} ", "'"+len(word)*"*"+" ")
    message = message.replace(f"'{word}\n", "'"+len(word)*"*"+"\n")
    message = message.replace(f"'{word}\t", "'"+len(word)*"*"+"\t")
    message = message.replace(f"'{word},", "'"+len(word)*"*"+",")
    message = message.replace(f"'{word}.", "'"+len(word)*"*"+".")
    message = message.replace(f"'{word}'", "'"+len(word)*"*"+"'")
    message = message.replace("'"+word+'"', "'"+len(word)*"*"+'"')
    message = message.replace(f"'{word}!", "'"+len(word)*"*"+"!")
    message = message.replace(f"'{word}?", "'"+len(word)*"*"+"?")
    message = message.replace(f"'{word}(", "'"+len(word)*"*"+"(")
    message = message.replace(f"'{word})", "'"+len(word)*"*"+")")

    message = message.replace(f'"{word} ', '"'+len(word)*"*"+" ")
    message = message.replace(f'"{word}\n', '"'+len(word)*"*"+"\n")
    message = message.replace(f'"{word}\t', '"'+len(word)*"*"+"\t")
    message = message.replace(f'"{word},', '"'+len(word)*"*"+",")
    message = message.replace(f'"{word}.', '"'+len(word)*"*"+".")
    message = message.replace(f'"'+word+"'", '"'+len(word)*"*"+"'")
    message = message.replace(f'"'+word+'"', '"'+len(word)*"*"+'"')
    message = message.replace(f'"{word}!', '"'+len(word)*"*"+"!")
    message = message.replace(f'"{word}?', '"'+len(word)*"*"+"?")
    message = message.replace(f'"{word}(', '"'+len(word)*"*"+"(")
    message = message.replace(f'"{word})', '"'+len(word)*"*"+")")

    message = message.replace(f"!{word} ", "!"+len(word)*"*"+" ")
    message = message.replace(f"!{word}\n", "!"+len(word)*"*"+"\n")
    message = message.replace(f"!{word}\t", "!"+len(word)*"*"+"\t")
    message = message.replace(f"!{word},", "!"+len(word)*"*"+",")
    message = message.replace(f"!{word}.", "!"+len(word)*"*"+".")
    message = message.replace(f"!{word}'", "!"+len(word)*"*"+"'")
    message = message.replace(f'!{word}"', "!"+len(word)*"*"+'"')
    message = message.replace(f"!{word}!", "!"+len(word)*"*"+"!")
    message = message.replace(f"!{word}?", "!"+len(word)*"*"+"?")
    message = message.replace(f"!{word}(", "!"+len(word)*"*"+"(")
    message = message.replace(f"!{word})", "!"+len(word)*"*"+")")

    message = message.replace(f"?{word} ", "?"+len(word)*"*"+" ")
    message = message.replace(f"?{word}\n", "?"+len(word)*"*"+"\n")
    message = message.replace(f"?{word}\t", "?"+len(word)*"*"+"\t")
    message = message.replace(f"?{word},", "?"+len(word)*"*"+",")
    message = message.replace(f"?{word}.", "?"+len(word)*"*"+".")
    message = message.replace(f"?{word}'", "?"+len(word)*"*"+"'")
    message = message.replace(f'?{word}"', "?"+len(word)*"*"+'"')
    message = message.replace(f"?{word}!", "?"+len(word)*"*"+"!")
    message = message.replace(f"?{word}?", "?"+len(word)*"*"+"?")
    message = message.replace(f"?{word}(", "?"+len(word)*"*"+"(")
    message = message.replace(f"?{word})", "?"+len(word)*"*"+")")

    message = message.replace(f"({word} ", "("+len(word)*"*"+" ")
    message = message.replace(f"({word}\n", "("+len(word)*"*"+"\n")
    message = message.replace(f"({word}\t", "("+len(word)*"*"+"\t")
    message = message.replace(f"({word},", "("+len(word)*"*"+",")
    message = message.replace(f"({word}.", "("+len(word)*"*"+".")
    message = message.replace(f"({word}'", "("+len(word)*"*"+"'")
    message = message.replace(f'({word}"', "("+len(word)*"*"+'"')
    message = message.replace(f"({word}!", "("+len(word)*"*"+"!")
    message = message.replace(f"({word}?", "("+len(word)*"*"+"?")
    message = message.replace(f"({word}(", "("+len(word)*"*"+"(")
    message = message.replace(f"({word})", "("+len(word)*"*"+")")

    message = message.replace(f"){word} ", ")"+len(word)*"*"+" ")
    message = message.replace(f"){word}\n", ")"+len(word)*"*"+"\n")
    message = message.replace(f"){word}\t", ")"+len(word)*"*"+"\t")
    message = message.replace(f"){word},", ")"+len(word)*"*"+",")
    message = message.replace(f"){word}.", ")"+len(word)*"*"+".")
    message = message.replace(f"){word}'", ")"+len(word)*"*"+"'")
    message = message.replace(f'){word}"', ")"+len(word)*"*"+'"')
    message = message.replace(f"){word}!", ")"+len(word)*"*"+"!")
    message = message.replace(f"){word}?", ")"+len(word)*"*"+"?")
    message = message.replace(f"){word}(", ")"+len(word)*"*"+"(")
    message = message.replace(f"){word})", ")"+len(word)*"*"+")")
    return message

def redact_forum():
    f = open(get_file("-forum"))
    forum = f.readlines()
    f.close()
    words = get_words()
    i = 4

    while i < len(forum):
        i2 = 0
        while i2 < len(words):
            forum[i] = censor_word(words[i2], forum[i])
            i2 += 1
        i += 3

    i3 = 0
    f = open(get_file("-forum"), "w")
    while i3 < len(forum):
        f.write(forum[i3])
        i3 += 1
    f.close()
    return True

if get_file("-task") == "censor_forum" and result[1] == True:
    if is_valid_words():
        redact_forum()

# Part 6

class User:
    def __init__(self, name: str):
        self.name = name
        self.engagement = 0
        self.expressiveness = 0
        self.offensiveness = 0

    def process_message(self, message: str, banned_words: list):
        if isinstance(message, str):
            if message.find("\t") == 0:
                self.engagement += 1
                i = 0
                while i < len(banned_words):
                    if message.find(banned_words[i]) != -1:
                        self.offensiveness += 1
                        break
                    i+=1
                if message.find("!") != -1 and message.find("?") != -1:
                    self.expressiveness += 2
                elif message.find("!") != -1:
                    self.expressiveness += 1
                elif message.find("!") == -1 and message.find("?") == -1:
                    self.expressiveness -= 1
                return True
            if message.find("\t") != 0:
                self.engagement += 1.5
                i = 0
                while i < len(banned_words):
                    if message.find(banned_words[i]) != -1:
                        self.offensiveness += 1.5
                        break
                    i+=1
                if message.find("!") != -1 and message.find("?") != -1:
                    self.expressiveness += 3
                elif message.find("!") != -1:
                    self.expressiveness += 1.5
                elif message.find("!") == -1 and message.find("?") == -1:
                    self.expressiveness -= 1.5
                return True
        else:
            return False

    def calculate_personality_score(self):
        engagement = self.engagement
        expressiveness = self.expressiveness
        offensiveness = self.offensiveness

        new_personality_score = expressiveness - offensiveness

        if new_personality_score > engagement:
            new_personality_score = engagement

        new_personality_score = int(new_personality_score)
        return new_personality_score

def judge_forum():
    f = open(get_file("-people"))
    people_start = []
    people_start.append(f.readline())
    people_start.append(f.readline())
    ls = []
    i = 0
    banned_words = get_words()

    while True:
        line = f.readline()
        if line == "":
            break
        line = line.strip()
        line = line.split(",")
        ls.append(User(line[0]))
        ls[i].old_personality_score = int(line[1])
        i += 1
    f.close()

    f = open(get_file("-forum"))
    f.readline()
    f.readline()

    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if line1 == "":
            break
        
        i2 = 0
        temp = line2.strip()
        temp = temp.replace("\t", "")
        while i2 < len(ls):
            if temp == ls[i2].name:
                ls[i2].process_message(line3, banned_words)
            i2 += 1
    f.close()
    
    i3 = 0
    while i3 < len(ls):
        ls[i3].new_personality_score = ls[i3].calculate_personality_score()
        ls[i3].personality_score = ls[i3].old_personality_score + ls[i3].new_personality_score
        if ls[i3].personality_score > 10:
            ls[i3].personality_score = 10
        if ls[i3].personality_score < -10:
            ls[i3].personality_score = -10
        i3 += 1

    f = open(get_file("-people"), "w")
    f.write(people_start[0])
    f.write(people_start[1])

    i4 = 0
    while i4 < len(ls):
        f.write(f"{ls[i4].name},{ls[i4].personality_score}\n")
        i4 += 1
    return

if get_file("-task") == "evaluate_forum" and result[1] == True:
    if is_valid_forum():
        if is_valid_people():
            judge_forum()
            sort_people()

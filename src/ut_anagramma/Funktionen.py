import re

def iterate(w):
    """
    iterate through word's characters looking for numbers and spaces
    """
    for i in w:
        if i.isalpha() == False:
            print(f"Do not introduce spaces, numbers or alphanumeric characters")
            exit()
        else:
            pass 
            
def too_long(w):
    """
    Does not allow too long strings
    """
    if len(w) >= 28:
        print(f"I don't know a word that long. Please try a shorter one")
        exit()
    else:
        pass                           

def do_text_to_list(w, f):
    """
    Make a list of the filename
    """
    filename = "words.txt"
    with open(filename) as file_object:
        lines = file_object.readlines()
        file_object.close()
    for line in lines:
        if len(line) == len(w) +1:
            f.append(line.rstrip())
    return f

def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    s1 = s1.lower()
    s2 = s2.lower()

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False
    
    return stillOK

def cjk_detect(texts):
    '''
    Extracted from https://gist.github.com/ceshine/1f8cd81ce34d89f1429d0928c28d97e4
    '''
    # korean
    if re.search("[\uac00-\ud7a3]", texts):
        return "ko"
    # japanese
    if re.search("[\u3040-\u30ff]", texts):
        return "ja"
    # chinese
    if re.search("[\u4e00-\u9FFF]", texts):
        return "zh"
    return None

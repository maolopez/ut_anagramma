import more_itertools
from numpy import unique

def iterate(w):
    """
    iterate trhough word's characters looking for numbers and spaces
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
    if len(w) >= 14:
        print(f"I don't know a word that long. Please try a shorter one")
        exit()
    else:
        pass                           

def do_text_to_list(f):
    """
    Make a list of the filename
    """
    filename = "words.txt"
    with open(filename) as file_object:
        lines = file_object.readlines()
    for line in lines:
        f.append(line.rstrip())
    return f
    
def permutas(permutas, p):
    """    
    create a list with all possible permutations of the characters in a word
    """
    permutas = ["".join(perm) for perm in more_itertools.distinct_permutations(p)]
    permutas = unique(permutas)
    permutas = sorted(permutas)
    return permutas

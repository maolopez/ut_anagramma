from Funktionen import iterate, do_text_to_list, permutas

anagrammas = []
file_words = []

def find_anagrammas(f, listas):
    """
    compare the list anagrams with the filename's list looking for matches
    """
    for lista in listas:
        for file_word in file_words:
            if lista == file_word:
                f.append(lista)
    return f, listas
     
#introduce the word and iterate in order to create a list of unique permutations    
word = input(f"Introduce the English word: ")
iterate(word)
anagrams = permutas(permutas, word)
do_text_to_list(file_words)
find_anagrammas(anagrammas, anagrams)

print(anagrammas)


         


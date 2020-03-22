from Funktionen import iterate, do_text_to_list, too_long, anagramSolution4

anagrammas = []
file_words = []
    
#introduce the word and iterate in order to create a list of unique permutations    
word = input(f"Introduce the English word: ")
too_long(word)
iterate(word)
do_text_to_list(word, file_words)

for file_word in file_words:
    if anagramSolution4(word,file_word) == True:
        anagrammas.append(file_word)

print(anagrammas)


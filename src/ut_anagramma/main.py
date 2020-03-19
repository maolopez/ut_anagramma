from Funktionen import do_text_to_list, permutas, iterate
from flask import Flask, request, render_template
    
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def adder_page():
    """
    Part of this function will replace iterate()
    This also will render the HTML templates
    """
    if request.method == "POST":
        word = None
        try:
            word = request.form["word"]
            iterate(word)
        except:
            return render_template("error.html")
        if word is not None:
            anagrammas = []
            file_words = []
            anagrams = permutas(permutas, word)
            do_text_to_list(file_words)
            for anagram in anagrams:
                for file_word in file_words:
                    if anagram == file_word:
                        anagrammas.append(anagram)
            return render_template("result.html").format(result=anagrammas)
        else:
            return render_template("error.html")
    return render_template("home.html")


     
#introduce the word and iterate in order to create a list of unique permutations    
#word = input(f"Introduce the English word: ")
#adder_page(word)
#iterate(word)
#anagrams = permutas(permutas, word)
#do_text_to_list(file_words)
#find_anagrammas(anagrammas, anagrams)

#print(anagrammas)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

         

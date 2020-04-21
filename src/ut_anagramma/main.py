from Funktionen import cjk_detect, do_text_to_list, iterate, too_long, anagramSolution4
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
            if cjk_detect(word) is None:
               pass
            if cjk_detect(word) == "ko":
               return render_template("no_english.html")    
            if cjk_detect(word) == "ja":
               return render_template("no_english.html") 
            if cjk_detect(word) == "zh":
               return render_template("no_english.html")
            too_long(word)
        except:
            return render_template("too_long.html")
        else:    
            try:
                iterate(word)
            except:
                return render_template("error.html")            
        if word is not None:
            anagrammas = []
            file_words = []
            do_text_to_list(word, file_words)
            for file_word in file_words:
                if anagramSolution4(word,file_word) == True:
                    anagrammas.append(file_word)
            return render_template("result.html").format(result=anagrammas)
        else:
            return render_template("error.html")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

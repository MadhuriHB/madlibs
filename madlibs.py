from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/') #Home page
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello') #route to say_hello function
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")  #takes us to hello.html


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", #takes us to compliment.html and also passes 2 arguments, person and compliment
                           person=player,
                           compliment=compliment)
@app.route('/game')
def show_madlib_form():
    response = request.args.get("response") #gives yes or no response
    print response
    if response == "no":
        return render_template("goodbye.html") #if no, go to goodbye.html
    else:
        return render_template("game.html") #if yes, go to game.html

@app.route('/madlib')
def show_madlib():
    name = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    animals = request.args.getlist("favorite_animal")
    
    

    return render_template("madlib.html",    # renders madlib.html with arguments name, color, noun and adjective 
                            person=name,
                            color=color,
                            noun=noun,
                            adjective=adjective, animals=animals)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

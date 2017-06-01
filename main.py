from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tomorrow = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrow + "</li>"
    content += "</ul>"
    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ['Sleepless in Seattle', 'The Fate of the Furious', 'Get Out', 'Beauty and the Beast', 'Baywatch']
    # TODO: randomly choose one of the movies, and return it
    x = len(movie_list)
    pick_movie = random.randrange(1, x)
    return movie_list[pick_movie]


app.run()

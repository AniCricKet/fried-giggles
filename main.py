# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition
import random
from words import wordlist

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/aniket/')  # connects /aniket/ URL to aniket() function
def aniket():
    return render_template("aniket.html")


@app.route('/soham/')  # connects /soham/ URL to soham() function
def soham():
    return render_template("soham.html")


@app.route('/ryan/')  # connects /ryan/ URL to ryan() function
def ryan():
    return render_template("ryan.html")


@app.route('/lucas/')  # connects /lucas/ URL to lucas() function
def lucas():
    return render_template("lucas.html")
    

@app.route('/team/')  # connects /team/ URL to team() function
def team():
    return render_template("team.html")

@app.route('/scrumboard/')  # connects /team/ URL to team() function
def scrumboard():
    return render_template("scrumboard.html") 


@app.route('/hangmangame/')
def hangmangame():
    return render_template("hangmangame.html")


@app.route('/randomword')
def randomword():
    #return ' '.join(random.choice(list(wordlist.items())))
    return random.choice(list(wordlist.values()))


# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=9999)

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index():
    """Show an index page."""
#Render the template created in the html/css assesment onto this route   
    return render_template("application-form.html")

@app.route("/application")
def response_page():
    """Show the user a response to their application"""
    #Render the info collected in the application form to a Jinja template onto this route
    #Get responses from form, assign them variable names
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    jobtitle = request.args.get("jobtitle")
    salaryrequirement = request.args.get("salaryrequirement")
    salaryrequirement = str(salaryrequirement)

#Rnder the responses into the response template
    return render_template("application-response.html", firstname = firstname, lastname = lastname, jobtitle = jobtitle, salaryrequirement = salaryrequirement)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
from flask import Flask, render_template


# Creating the calculator application
# only will need 1 route index.html

Flask_App = Flask(__name__) # Creating our Flask Instance


@Flask_App.route('/')
def index():
    """
    Displays the index page accessible at '/'
    """

    return render_template('index.html')

@Flask_App.route('/operation')
def operation_result():
    return render_template('index.html')

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()

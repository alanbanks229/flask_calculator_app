from flask import Flask, render_template, request

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    result = None
    calculation_success = False

    try:
        # request.form looks for:
        # html tags with matching "name= "
        input1 = float(request.form['Input1'])
        input2 = float(request.form['Input2'])
        operation = request.form['operation']

        #On Default, the operation on webpage is addition
        if operation == "add":
            operation = "plus "
            result = input1 + input2
            calculation_success = True

        elif operation == "sub":
            operation = "minus "
            result = input1 - input2
            calculation_success = True

        # this will throw ZeroDivisionError if input2 is 0
        elif operation == "div":
            operation = "divided by "
            result = input1 / input2 
            #calculation_success = True will not be hit if error occurs above.
            calculation_success = True

        elif operation == "mult":
            operation = "multiplied by "
            result = input1 * input2
            calculation_success = True

        else:
            operation = "modulo "
            result = input1 % input2
            calculation_success = True

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            successful=calculation_success
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            error="You cannot divide by zero"
        )
    except ValueError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            error="Cannot perform numeric operations with provided input"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()

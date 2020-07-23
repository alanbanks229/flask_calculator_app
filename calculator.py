from flask import Flask, render_template, request


# Creating the calculator application
# only will need 1 route index.html

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
            result = add(input1, input2)
            operation = "plus "
            calculation_success = True

        elif operation == "sub":
            result = subtract(input1, input2)
            operation = "minus "
            calculation_success = True

        # this will throw ZeroDivisionError if input2 is 0
        elif operation == "div":
            operation = "divided by "
            result = input1 / input2 
            #calculation_success = True will not be hit if error occurs above.
            calculation_success = True

        elif operation == "mult":
            result = multiply(input1, input2)
            operation = "multiplied by "
            calculation_success = True

        else:
            result = mod(input1, input2)
            operation = "modulo "
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

# Our helper methods.
def add(input1, input2):
    answer = input1 + input2
    print("The addition of", input1, "and", input2, "is", answer)
    return answer

def subtract(input1, input2):
    answer = input1 - input2
    print("The difference of", input1, "and", input2, "is", answer)
    return answer

def multiply(input1, input2):
    answer = input1 * input2
    print("The multiplication of", input1, "and", input2, "is", answer)
    return answer

def mod(input1, input2):
    answer = input1 % input2
    print("The modulus of", input1, "and", input2, "is", answer)
    return answer

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()

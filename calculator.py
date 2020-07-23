from flask import Flask, render_template, request


# Creating the calculator application
# only will need 1 route index.html

Flask_App = Flask(__name__) # Creating our Flask Instance


@Flask_App.route('/')
def index():
    """
    Displays the index page accessible at '/'
    """

    return render_template('index.html')


@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():

    error = None
    result = None
    try:
        # looks for html tags with specified name=
        input1 = float(request.form['Input1'])
        input2 = float(request.form['Input2'])
        operation = request.form['operation']

        #operation on default is addition.
        if operation == "add":
            result = add(input1, input2)
            operation = "plus "
        elif operation == "sub":
            result = subtract(input1, input2)
            operation = "minus "
        elif operation == "div":
            # this will throw ZeroDivisionError if input2 is 0
            result = input1 / input2
            operation = "divided by "
        elif operation == "mult":
            result = multiply(input1, input2)
            operation = "multiplied by "
        else:
            result = mod(input1, input2)
            operation = "modulo "
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result
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

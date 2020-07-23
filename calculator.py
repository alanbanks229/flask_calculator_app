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

    # looks for html tags with specified name=
    input1 = request.form['Input1']
    input2 = request.form['Input2']
    operation = request.form['operation']
    result = None
    # conditional to check if input1 AND input2 are instances int or float.
    # also checking if operation is not null.
    if (isinstance(input1, (int, long)) and 
        isinstance(input2, (int, long)) and
        operation):
        if operation == "add":
            result = add(input1, input2)
        elif operation == "sub":
            result = subtract(input1, input2)
        elif operation == "div":
            try:
                result = input1 / input2
            except ZeroDivisionError:
                error = "Warning: dividing by zero is not allowed"
                return render_template(
                    'index.html',
                    input1=input1,
                    input2=input2,
                    operation=operation,
                    error=error
                )
        elif operation == "mult":
            result = multiply(input1, input2)
        else:
            result = mod(input1, input2)
        
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result
        )
    # else
    return render_template(
        'index.html',
        error="invalid input",
        input1=input1,
        input2=input2,
        operation=operation
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

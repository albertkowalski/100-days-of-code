import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
run_calculation = True

num1 = float(input("What's the first number?:"))
while run_calculation:
    for keys in operations:
        print(keys)
    correct = False
    operator = "Error!"
    while not correct:
        operator = input("Pick a operator: ")
        if operator in operations:
            correct = True
    calculation_function = operations[operator]

    num2 = float(input("What's the second number?:"))

    print(f"{num1} {operator} {num2} = {calculation_function(num1, num2)}")
    num1 = calculation_function(num1, num2)
    wrong_decision = True
    while wrong_decision:
        decision = input("Do you want ot continue calculations? Type 'y' or 'n': ")
        if decision == 'n':
            run_calculation = False
            wrong_decision = False
        if decision == 'y':
            run_calculation = True
            wrong_decision = False

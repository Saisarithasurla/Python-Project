# calculator_module.py
def calculate(expression):
    try:
        result = eval(expression)
    except Exception:
        result = "Invalid calculation."
    return result

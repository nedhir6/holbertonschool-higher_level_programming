#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = len(sys.argv)
    if (args == 4):
        operators = ["+", "-", "*", "/"]
        op = sys.argv[2]
        if op in operators:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = sub(a, b)
            elif op == "*":
                result = mul(a, b)
            else:
                result = div(a, b)
            print("{} {} {} = {}".format(a, op, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

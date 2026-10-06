from calc.calculator import Calculator

def main():
    calc = Calculator()
    
    print("Addition with two arguments (2 + 3):", calc.add(2, 3))
    print("Addition with one argument (adding 2 to memory):", calc.add(2))
    
    print("Subtraction with two arguments (5 - 3):", calc.sub(5, 3))
    print("Subtraction with one argument (subtracting 5 from memory):", calc.sub(5))
    
    print("Multiplication with two arguments (2 * 3):", calc.mul(2, 3))
    print("Multiplication with one argument (multiplying memory by 2):", calc.mul(2))
    
    print("Division with two arguments (6 / 3):", calc.div(6, 3))
    print("Division with one argument (dividing memory by 6):", calc.div(6))

if __name__ == "__main__":
    main()
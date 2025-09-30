#!/usr/bin/env python3
"""
Python Calculator - A comprehensive calculator for various mathematical operations
Author: GitHub Copilot
Date: September 30, 2025
"""

import math
import statistics

class Calculator:
    """A comprehensive calculator class with various mathematical operations"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division with error handling"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent"""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, number):
        """Calculate square root"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(number)
        self.history.append(f"√{number} = {result}")
        return result
    
    def factorial(self, n):
        """Calculate factorial"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        result = math.factorial(int(n))
        self.history.append(f"{n}! = {result}")
        return result
    
    def percentage(self, value, percent):
        """Calculate percentage of a value"""
        result = (percent / 100) * value
        self.history.append(f"{percent}% of {value} = {result}")
        return result
    
    def compound_interest(self, principal, rate, time, compounds_per_year=1):
        """Calculate compound interest"""
        amount = principal * (1 + rate/100/compounds_per_year) ** (compounds_per_year * time)
        interest = amount - principal
        self.history.append(f"Compound Interest: P={principal}, R={rate}%, T={time} years = {interest}")
        return {"amount": amount, "interest": interest}
    
    def bmi_calculator(self, weight_kg, height_m):
        """Calculate Body Mass Index"""
        bmi = weight_kg / (height_m ** 2)
        self.history.append(f"BMI: {weight_kg}kg, {height_m}m = {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        return {"bmi": round(bmi, 2), "category": category}
    
    def trigonometry(self, angle_degrees, function="sin"):
        """Calculate trigonometric functions"""
        angle_radians = math.radians(angle_degrees)
        
        if function.lower() == "sin":
            result = math.sin(angle_radians)
        elif function.lower() == "cos":
            result = math.cos(angle_radians)
        elif function.lower() == "tan":
            result = math.tan(angle_radians)
        else:
            raise ValueError("Function must be 'sin', 'cos', or 'tan'")
        
        self.history.append(f"{function}({angle_degrees}°) = {result}")
        return result
    
    def statistics_calc(self, numbers):
        """Calculate basic statistics for a list of numbers"""
        if not numbers:
            raise ValueError("List cannot be empty!")
        
        stats = {
            "mean": statistics.mean(numbers),
            "median": statistics.median(numbers),
            "mode": statistics.mode(numbers) if len(set(numbers)) != len(numbers) else "No mode",
            "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0,
            "min": min(numbers),
            "max": max(numbers),
            "range": max(numbers) - min(numbers),
            "sum": sum(numbers),
            "count": len(numbers)
        }
        
        self.history.append(f"Statistics calculated for {len(numbers)} numbers")
        return stats
    
    def quadratic_formula(self, a, b, c):
        """Solve quadratic equation ax² + bx + c = 0"""
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in quadratic equation!")
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return "No real solutions (complex roots)"
        elif discriminant == 0:
            x = -b / (2*a)
            self.history.append(f"Quadratic: {a}x² + {b}x + {c} = 0, Solution: x = {x}")
            return {"x1": x, "x2": x}
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            self.history.append(f"Quadratic: {a}x² + {b}x + {c} = 0, Solutions: x1 = {x1}, x2 = {x2}")
            return {"x1": x1, "x2": x2}
    
    def area_calculator(self, shape, **kwargs):
        """Calculate area of different shapes"""
        shape = shape.lower()
        
        if shape == "rectangle":
            area = kwargs["length"] * kwargs["width"]
            self.history.append(f"Rectangle area: {kwargs['length']} × {kwargs['width']} = {area}")
        elif shape == "circle":
            area = math.pi * kwargs["radius"] ** 2
            self.history.append(f"Circle area: π × {kwargs['radius']}² = {area}")
        elif shape == "triangle":
            area = 0.5 * kwargs["base"] * kwargs["height"]
            self.history.append(f"Triangle area: 0.5 × {kwargs['base']} × {kwargs['height']} = {area}")
        elif shape == "square":
            area = kwargs["side"] ** 2
            self.history.append(f"Square area: {kwargs['side']}² = {area}")
        else:
            raise ValueError("Unsupported shape! Use: rectangle, circle, triangle, or square")
        
        return area
    
    def get_history(self):
        """Return calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        print("History cleared!")

# Example usage and demonstration
def main():
    """Demonstrate calculator functionality"""
    calc = Calculator()
    
    print("=== Python Calculator Demo ===\n")
    
    # Basic arithmetic
    print("Basic Arithmetic:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 3 = {calc.subtract(10, 3)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2^8 = {calc.power(2, 8)}")
    print(f"√16 = {calc.square_root(16)}")
    print(f"5! = {calc.factorial(5)}")
    
    print("\nAdvanced Calculations:")
    # Percentage
    print(f"15% of 200 = {calc.percentage(200, 15)}")
    
    # Compound interest
    interest_result = calc.compound_interest(1000, 5, 2)
    print(f"Compound Interest: Amount = ${interest_result['amount']:.2f}, Interest = ${interest_result['interest']:.2f}")
    
    # BMI
    bmi_result = calc.bmi_calculator(70, 1.75)
    print(f"BMI: {bmi_result['bmi']} ({bmi_result['category']})")
    
    # Trigonometry
    print(f"sin(30°) = {calc.trigonometry(30, 'sin'):.4f}")
    print(f"cos(60°) = {calc.trigonometry(60, 'cos'):.4f}")
    
    # Statistics
    numbers = [10, 15, 20, 25, 30, 25, 20]
    stats = calc.statistics_calc(numbers)
    print(f"\nStatistics for {numbers}:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']}")
    print(f"Standard Deviation: {stats['std_dev']:.2f}")
    
    # Quadratic equation
    quad_result = calc.quadratic_formula(1, -5, 6)
    print(f"\nQuadratic equation x² - 5x + 6 = 0:")
    print(f"Solutions: x1 = {quad_result['x1']}, x2 = {quad_result['x2']}")
    
    # Area calculations
    print(f"\nArea Calculations:")
    print(f"Rectangle (5×3): {calc.area_calculator('rectangle', length=5, width=3)}")
    print(f"Circle (radius=4): {calc.area_calculator('circle', radius=4):.2f}")
    print(f"Triangle (base=6, height=8): {calc.area_calculator('triangle', base=6, height=8)}")
    
    # Show history
    print(f"\nCalculation History ({len(calc.get_history())} operations):")
    for i, operation in enumerate(calc.get_history()[-5:], 1):  # Show last 5
        print(f"{i}. {operation}")

if __name__ == "__main__":
    main()

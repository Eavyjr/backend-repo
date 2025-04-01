import sympy as sp 
import numpy as np 

def classify_expression(expression): 
    try: 
        expr = sp.sympify(expression) 
        category = "Unknown" 
        if expr.is_polynomial(): category = "Polynomial" 
        elif expr.is_rational_function(): category = "Rational Function" 
        elif expr.is_trig(): category = "Trigonometric Function" 
        elif expr.is_real and expr.is_positive: category = "Exponential/Logarithmic Function" 
        elif expr.has(sp.Derivative): category = "Differential Equation" 
        elif expr.has(sp.Integral): category = "Integral Equation" 
        elif expr.is_comparable: category = "Equation" 
        x = sp.Symbol("x") 
        f_lambdified = sp.lambdify(x, expr, modules=["numpy"]) 
        x_values = np.linspace(-10, 10, 100) 
        y_values = f_lambdified(x_values).tolist() 
        return { "expression": str(expr), "category": category, "plot_data": {"x": x_values.tolist(), "y": y_values} } 
    except Exception as e: 
        return {"error": str(e)}
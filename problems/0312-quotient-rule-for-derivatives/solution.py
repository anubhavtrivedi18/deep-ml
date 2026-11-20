import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here

    
    power_2 = len(h_coeffs)-1
    j = 0
    h_derivatives  = 0
    h_eqn = 0
    while j<len(h_coeffs):
        power = power_2-j
        result_2 = h_coeffs[j]*(x**(power))
        h_eqn+=result_2
        if power > 0:
            result_1 = h_coeffs[j]*(power)*(x**(power-(+1)))
            h_derivatives+=result_1
        j+=1
    if h_eqn==0:
        return [-1]
    power_1 = len(g_coeffs)-1
    i = 0
    g_derivatives  = 0
    g_eqn = 0 
    while i<len(g_coeffs):
        power = power_1-i
        result_2 = g_coeffs[i]*(x**(power))
        g_eqn+=result_2
        if power >0:
            result_1 = g_coeffs[i]*(power)*(x**(power-(1)))
            g_derivatives+=result_1
        i+=1
    output = (g_derivatives*h_eqn-g_eqn*h_derivatives)/(h_eqn)**2
    return output    
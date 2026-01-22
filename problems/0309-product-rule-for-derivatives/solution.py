import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    # derivative of f_x
    if len(f_coeffs) <= 1:
        df_dx = np.array([0,0])
    else:
        df_dx = f_coeffs[1:]*np.arange(1,len(f_coeffs))
    # derivative of g_xa
    if len(g_coeffs) <= 1:
        dg_dx = np.array([0,0])
    else:
        dg_dx = g_coeffs[1:]*np.arange(1,len(g_coeffs))
    
    term1 = np.convolve(df_dx,g_coeffs)
    term2 = np.convolve(dg_dx,f_coeffs)
    n = max(len(term1),len(term2))
    output = np.zeros(n, dtype = float)
    output[:len(term1)] += t
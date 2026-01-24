import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
    grad = np.array(gradient)
    magn = 0
    for i in range(0,len(grad)):
        magn+=grad[i]**2
    magnitude = np.sqrt(magn)
    if magnitude ==0:
        direction = [0.0]*len(grad)
        descent_direction = [0.0]*len(grad)
    else:
         direction = grad/magnitude
         descent_direction = -direction
    dict = {'magnitude':magnitude,'direction':direction,'descent_direction':descent_direction}
    return dict
	pass
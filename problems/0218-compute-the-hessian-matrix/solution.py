from typing import Callable

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Hessian matrix of function f at the given point using finite differences.
    
    Args:
        f: A scalar function that takes a list of floats and returns a float
        point: The point at which to compute the Hessian (list of coordinates)
        h: Step size for finite differences (default: 1e-5)
        
    Returns:
        The Hessian matrix as a list of lists (n x n where n = len(point))
    """
    # Your code here
    if len(point)==2:
        x = point[0]
        y = point[1]
        df_dx_2 = (f([x+h,y])-2*f([x,y])+f([x-h,y]))/(h**2)
        df_dy_2 = (f([x,y+h])-2*f([x,y])+f([x,y-h]))/(h**2)
        df_dx_dy = df_dy_dx = (f([x+h,y+h])-f([x+h,y-h])-f([x-h,y+h])+f([x-h,y-h]))/(4*h**2)
        return [[df_dx_2,df_dx_dy],[df_dy_dx,df_dy_2]]
    else:
        x = point[0]
        y = point[1]
        z = point[2]
        df_dx_2 = (f([x+h,y,z])-2*f([x,y,z])+f([x-h,y,z]))/(h**2)
        df_dy_2 = (f([x,y+h,z])-2*f([x,y,z])+f([x,y-h,z]))/(h**2)
        df_dz_2 = (f([x,y,z+h])-2*f([x,y,z])+f([x,y,z-h]))/(h**2)
        df_dx_dy = df_dy_dx = (f([x+h,y+h,z])-f([x+h,y-h,z])-f([x-h,y+h,z])+f([x-h,y-h,z]))/(4*h**2)
        df_dz_dy = df_dy_dz = (f([x,y+h,z+h])-f([x,y-h,z+h])-f([x,y+h,z-h])+f([x,y-h,z-h]))/(4*h**2)
        df_dz_dx = df_dx_dz = (f([x+h,y,z+h])-f([x-h,y,z+h])-f([x+h,y,z-h])+f([x-h,y,z-h]))/(4*h**2)
        return [[df_dx_2,df_dx_dy,df_dx_dz],[df_dy_dx,df_dy_2,df_dz_dy],[df_dx_dz,df_dy_dz,df_dz_2]]

    
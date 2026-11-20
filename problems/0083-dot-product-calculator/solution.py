import torch

def calculate_dot_product(vec1: torch.Tensor, vec2: torch.Tensor) -> torch.Tensor:
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (torch.Tensor): 1D tensor representing the first vector.
        vec2 (torch.Tensor): 1D tensor representing the second vector.
    Returns:
        torch.Tensor: The dot product of the two vectors as a scalar tensor.
    """
    # Your code here
    vec1 = torch.tensor(vec1)
    vec2 = torch.tensor(vec2)
    if len(vec1)!=len(vec2):
        return torch.tensor(-1)
    else:
        vec3 = torch.dot(vec1,vec2)
        return vec3
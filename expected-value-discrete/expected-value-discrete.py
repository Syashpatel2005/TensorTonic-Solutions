import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """ 
    x = np.array(x)
    p = np.array(p)
    if x.shape!=p.shape:
        raise ValueError('shape sould not be same')
    if not np.isclose(sum(p),1,atol=1e-6):
        raise ValueError('sum of probability must not equal to 1')
    return float(np.dot(x,p))
        
    pass

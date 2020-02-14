def distance(a, b):
    if(len(a) != len(b)):
        raise ValueError("Different lengths detected")
    
    return len([i for i, j in zip(a, b) if i != j])

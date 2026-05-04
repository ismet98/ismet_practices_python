


def max_function(x,y,z):
    
    if x > y:
        if x > z:
            return x
        else: 
            return z
    else:
        if y > z:
            return y
        else:   
            return z
        


print(max_function(5,3,7))
def remainder(a,b):
    #your code here
    
    try:
        return (max(a, b) % min(a, b))
    except:
        return None
        

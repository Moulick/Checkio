def checkio(data):
    
    l1 = []
    
    for x in data:
        if data.count(x)>1:
            l1.append(x)
    return l1

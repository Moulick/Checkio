import math
def checkio(a, b, c):

    degen = a+b>c and a+c>b and b+c>a
    angles = []    
    if degen:
        angle_a = math.acos((a**2+b**2-c**2)/(2*a*b))
        angle_b = math.acos((-a**2+b**2+c**2)/(2*c*b))
        angle_c = math.acos((a**2-b**2+c**2)/(2*a*c))
        
        
        angles.append(round((angle_a*180)/math.pi))
        angles.append(round((angle_b*180)/math.pi))
        angles.append(round((angle_c*180)/math.pi))
        return sorted(angles)
    else:
        return [0, 0, 0]

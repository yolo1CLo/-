import math
def quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("The Discriminant is inferior to zero.")
        return None  
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2
def Newton (variables):
    m,a,F = variables
    if m is None:
        try: 
            m = F/a
            print (f"The value of {F} divided by {a} is equal to the m being {m} kg.")
            return m
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    elif a is None:
        try: 
            a = F/m
            print (f"The value of {F} divided by {m} is equal to the m being {a} kg.")
            return a
        except ZeroDivisionError:
            print("Error: Division by zero.")
    else: 
        F =  m * a
        print (f"The value of {m} multiplicated by {a} is equal to the Force being {F}")
        return F
def Work (variables): 
    d,F,c,W = variables
    if d is None:
        try:
            d = W/math.cos(c)*F
            print (f"The value of tghe distance is equal too {d}")
            return d
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    elif F is None:
        try:
            F = W/d.math.cos(c)
            print (f"The Fore is equal too {F}N")
            return F
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    elif c is None:
        try:
            c = W/d*F
            print (f"The value of the angle is equal too {c}.")
            return c
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    else: 
        W = F * d * math.cos(c)
        print (f"The Work for this calculus is equal too {W}J")
        return UserWarning
def Speed (variables):
    d,t,v = variables
    if d is None:
        d = v*t
        print (f"The value of the distance is equal to {d}.")
        return d
    elif t is None:
        try:
            t = d/v
            print (f"The value of the time is equal to {t}")
            return t
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    else: 
        try:
            v = d / t
            print (f"The speed is equal to {v}m/s.")        
            return v
        except ZeroDivisionError:
            print("Error: Division by zero. ")
def Kinetic_Energy (variables):
    c = 0.5
    m,v,KE = variables
    if m is None:
        try:
            m = KE/(v**2) * c
            print (f"The value of the mass is equal to {m}.")
            return m
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    elif v is None:
        try:
            v = math.sqrt(KE/c*m)
            print (f"The value of the speed is equal to {v}")
            return v
        except ZeroDivisionError:
            print("Error: Division by zero. ")
    else: 
        KE =  c* v**2 * m
        print (f"The Kinetic Energy is equal to {KE}N")
        return KE

print ("You can choose bewteen: Quadratic, Newton, Work, Speed, Kinetic energy")
type = input("What do you want? = ")
if type.lower() == 'quadratic'.lower():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    quadratic(a,b,c)
elif type.lower() == 'Newton'.lower():
    print("Enter the values for the variables in the formula. Leave empty for the unknown variable: ")
    variables = [input("mass = "), input("acceleration = "), input("force = ")]
    for i in range(len(variables)):
        if variables[i] == "":  
            variables[i] = None
        else:   
            variables[i] = float(variables[i])
    inconnue = Newton(variables)
elif type.lower() == 'Work'.lower():
    print("Enter the values for the variables in the formula. Leave empty for the unknown variable: ")
    variables = [input("distance = "), input("force = "), input("angle= "), input("Work=")]
    for i in range(len(variables)):
        if variables[i] == "": 
            variables[i] = None
        else:   
            variables[i] = float(variables[i])
    inconnue = Work(variables)
elif type.lower() == 'Speed'.lower():
    print("Enter the values for the variables in the formula. Leave empty for the unknown variable: ")
    variables = [input("distance = "), input("time = "), input("speed= ")]
    for i in range(len(variables)):
        if variables[i] == "":  
            variables[i] = None
        else:  
            variables[i] = float(variables[i])
    inconnue = Speed(variables)
elif type.lower() == 'Kinetic energy'.lower():
    print("Enter the values for the variables in the formula. Leave empty for the unknown variable: ")
    variables = [input("mass = "), input("speed = "), input("Kinetic energy= ")]
    for i in range(len(variables)):
        if variables[i] == "": 
            variables[i] = None
        else:   
            variables[i] = float(variables[i])
    inconnue = Kinetic_Energy(variables)
else:
    print("Invalid input. Please enter a correct choice.")
#########################################################
import numpy as np
import math

vec_x = float(input("Vector's X coordinate:"))
vec_y = float(input("Vector's Y coordinate:"))
vec_z = float(input("Vector's Z coordinate:"))
vec = [[vec_x], [vec_y], [vec_z]]
print(vec)

ang = int(input("A rotation angle in degrees:"))
#counter-clockwise is positive
if ang < 0 :
    ang += 360
else:
    pass
    
ax = int(input("Rotation Axis(X=1,Y=2,Z=3):"))

def nvec(vec,ang,ax):
    ang = math.radians(ang)

    if ax==1:
        X = [[1, 0, 0], 
             [0, np.cos(ang), np.sin(ang)], 
             [0, -np.sin(ang), np.cos(ang)]]
        result = np.dot(X,vec)
        return result
    if ax==2:
        Y = [[np.cos(ang), 0, -np.sin(ang)], 
             [0, 1, 0], 
             [np.sin(ang), 0 ,np.cos(ang)]]
        result = np.dot(Y,vec)
        return result
    if ax==3:
        Z = [[np.cos(ang), np.sin(ang), 0], 
             [-np.sin(ang), np.cos(ang), 0], 
             [0, 0, 1]]
        result = np.dot(Z,vec)
        return result

print(f"A [3x1] vector that icludes X,Y,Z coordinates of the defined point in the new system:\n{nvec(vec,ang,ax)}")                  

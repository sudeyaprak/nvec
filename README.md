# nvec (vec,ang,ax)

1. Input:
The `nvec` function takes three arguments:

- `vec`: A 3x1 vector representing the coordinates of a point in 3D space. It is provided as a list of lists in the form `[[x], [y], [z]]`.
- `ang`: The rotation angle in degrees. This angle specifies the amount of rotation that will be applied to the vector.
- `ax`: The rotation axis. It's an integer value that determines which axis the rotation will be performed around. The axis is represented as follows: `1` for X-axis, `2` for Y-axis, and `3` for Z-axis.

2. Purpose:
The primary purpose of the `nvec` function is to perform a rotation on a 3D vector (`vec`) around a specified axis (`ax`) by a given rotation angle (`ang`). The function returns a new 3x1 vector representing the coordinates of the point after the rotation.

3. Rotation Matrices:
The function uses rotation matrices to perform the 3D rotations. Each rotation matrix corresponds to a specific axis of rotation (X, Y, or Z). The rotation matrices are based on trigonometric functions (cosine and sine) of the rotation angle. The rotation matrices are as follows:

- X-Axis Rotation Matrix:
```
X = [[1, 0, 0], 
     [0, cos(ang), sin(ang)], 
     [0, -sin(ang), cos(ang)]]
```

- Y-Axis Rotation Matrix:
```
Y = [[cos(ang), 0, -sin(ang)], 
     [0, 1, 0], 
     [sin(ang), 0, cos(ang)]]
```

- Z-Axis Rotation Matrix:
```
Z = [[cos(ang), sin(ang), 0], 
     [-sin(ang), cos(ang), 0], 
     [0, 0, 1]]
```

4. Angle Conversion:
Before applying the rotation, the function converts the input rotation angle (`ang`) from degrees to radians using the `math.radians()` function.

5. Rotation Calculation:
The function selects the appropriate rotation matrix based on the specified axis (`ax`). It then performs the matrix multiplication (`np.dot()`) between the selected rotation matrix and the 3x1 vector `vec`, resulting in the rotated vector `result`.

6. Return Value:
The function returns the new 3x1 vector `result`, which represents the coordinates of the point after the specified rotation around the chosen axis.

Overall, the function `nvec` allows for easy 3D vector rotation around the X, Y, or Z axis by a specified angle in degrees. This can be useful for various applications in 3D graphics, computer vision, robotics, and other fields where transformations of 3D points are required.

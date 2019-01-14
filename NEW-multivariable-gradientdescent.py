from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

f = x**2 + y**2 - 2*x*y
#first partial derivatives
f_x = f.diff(x)
f_y = f.diff(y)
#gradient
G = [f_x, f_y]
#data
theta_x = 830
theta_y = 220
alpha = 0.01
iterations = 0
check = 0
precision = 1/1000000
printData = True
maxIterations = 1000

while True:
    temp_theta_x = theta_x - alpha*N(f_x.subs(x, theta_x).subs(y,theta_y)).evalf()
    temp_theta_y = theta_y - alpha*N(f_y.subs(y, theta_y).subs(x,theta_x)).evalf()

    iterations += 1
    if iterations > maxIterations:
        print("Too many Iterations!")
        printData = False
        break
    if abs(temp_theta_x-theta_x)<precision and abs(themp_theta_y-theta_y)<precision:
              break

    theta_x = temp_theta
    theta_y = themp_theta_1

    if printData:
              print("The function " + str(f) +" converge to a minimum")
              print("Number of iterations: ", iterations, sep = " ")
              print("theta(x0) = ", temp_theta_x, sep = " ")
              print("theta(y0) = ", temp_theta_y, sep = " ")
    

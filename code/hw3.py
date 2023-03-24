#-------------------------------Importation of required libraries-------------------------------------
import sympy as sp

#------------------------------Declaration of variables and symbols-----------------------------------
theta = [i for i in sp.symbols('Θ(1:8)')]
alpha = [i for i in sp.symbols('α(1:8)')]
a = [0 ,0, sp.symbols("a3"), -sp.symbols("a3"), 0, sp.symbols("a3"), 0]
d = [sp.symbols("d1"), 0, sp.symbols("d3"), 0, sp.symbols("d5"), 0, -sp.symbols("d7")]

t01 = "\u2070" + "T" + "\u2081"                                                 #Unicodes for super and subscripts
t12 = "\u00b9" + "T" + "\u2082"                                                 #Unicodes for super and subscripts
t23 = "\u00b2" + "T" + "\u2083"                                                 #Unicodes for super and subscripts
t34 = "\u00b3" + "T" + "\u2084"                                                 #Unicodes for super and subscripts
t45 = "\u2074" + "T" + "\u2085"                                                 #Unicodes for super and subscripts
t56 = "\u2075" + "T" + "\u2086"                                                 #Unicodes for super and subscripts
t67 = "\u2076" + "T" + "\u2087"                                                 #Unicodes for super and subscripts

t = [t01, t12, t23, t34, t45, t56, t67]

#-----------------------------Calculations of Transformation Matrices---------------------------------
T = []
for i in range(7):
    x = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
         [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
         [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
         [0, 0, 0, 1]
        ])
    print("\nTransformation Matrix ", t[i], "= ")
    sp.pprint(x)
    print("\n")
    T.append(x)

#--------------------------Giving the values of d, a, alpha instead of symbols------------------------------------
d[0] = 0.3330
d[1] = 0
d[2] = 0.3160
d[3] = 0
d[4] = 0.3840
d[5] = 0
d[6] = -0.1070

a[0] = 0
a[1] = 0
a[2] = 0.0880
a[3] = -0.0880
a[4] = 0
a[5] = 0.0880
a[6] = 0

alpha[0] = sp.pi/2
alpha[1] = -sp.pi/2
alpha[2] = -sp.pi/2
alpha[3] = sp.pi/2
alpha[4] = sp.pi/2
alpha[5] = -sp.pi/2
alpha[6] = 0

theta = [0, -sp.pi/2, 0, 0, 0, 0, 0]

#-----------------------------Calculations of Homogeneous Transformation Matrices---------------------------------

T_calc = []
for i in range(7):
    x = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
         [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
         [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
         [0, 0, 0, 1]
        ])
    T_calc.append(x)

t07 = "\u2070" + "T" + "\u2087"                                                 #Unicodes for super and subscripts

print("Final Transformation Matrix ", t07, " = ")
final_trans = T_calc[0]*T_calc[1]*T_calc[2]*T_calc[3]*T_calc[4]*T_calc[5]*T_calc[6]


print("---------------------------------Case 1--------------------------------------\n")
print("Θ2 = -90 degrees")
print("Final Transformation Matrix ", t07, " = ")
sp.pprint(final_trans.evalf())


print("---------------------------------Case 2--------------------------------------\n")
print("Θ1 = 90 degrees")
print("Final Transformation Matrix ", t07, " = ")
theta = [sp.pi/2, 0, 0, 0, 0, 0, 0]
T_calc = []
for i in range(7):
    x = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
         [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
         [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
         [0, 0, 0, 1]
        ])
    T_calc.append(x)
final_trans = T_calc[0]*T_calc[1]*T_calc[2]*T_calc[3]*T_calc[4]*T_calc[5]*T_calc[6]
sp.pprint(final_trans.evalf())


print("---------------------------------Case 3--------------------------------------\n")
print("All theta 0 degrees")
print("Final Transformation Matrix ", t07, " = ")
theta = [0, 0, 0, 0, 0, 0, 0]
T_calc = []
for i in range(7):
    x = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
         [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
         [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
         [0, 0, 0, 1]
        ])
    T_calc.append(x)
final_trans = T_calc[0]*T_calc[1]*T_calc[2]*T_calc[3]*T_calc[4]*T_calc[5]*T_calc[6]
sp.pprint(final_trans.evalf())

print("---------------------------------Case 4--------------------------------------\n")
print("Θ4 = 90 degrees")
print("Final Transformation Matrix ", t07, " = ")
theta = [0, 0, 0, sp.pi/2, 0, 0, 0]
T_calc = []
for i in range(7):
    x = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
         [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
         [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
         [0, 0, 0, 1]
        ])
    T_calc.append(x)
final_trans = T_calc[0]*T_calc[1]*T_calc[2]*T_calc[3]*T_calc[4]*T_calc[5]*T_calc[6]
sp.pprint(final_trans.evalf())

print("---------------------------------Case 5--------------------------------------\n")
print("Θ6 = 90 degrees")
print("Final Transformation Matrix ", t07, " = ")
theta = [0, 0, 0, 0, 0, sp.pi/2, 0]
T_calc = []
for i in range(7):
    x = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
         [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
         [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
         [0, 0, 0, 1]
        ])
    T_calc.append(x)
final_trans = T_calc[0]*T_calc[1]*T_calc[2]*T_calc[3]*T_calc[4]*T_calc[5]*T_calc[6]
sp.pprint(final_trans.evalf())
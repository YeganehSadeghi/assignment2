  #calculator for radical-factorial - sin-cos-tan-cot
  #assignment 2-1
 


import math

n = int(input(" enter  a number="))
op=input ("chose  an operation=")

if op == "radical":
    radical=math.sqrt(n)
    print(radical)


if op =="factorial":
    factorial=math.factorial(n)
    print(factorial)


if op =="sin":
    sin=math.sin(n)
    print(sin)

 
if op =="cos":
    cos=math.cos(n)
    print(cos)


if op =="tan":
    tan=math.tan(n)
    print(tan)

if op ==  "cot":
    cot=math.cos(n)/sin(n)
    
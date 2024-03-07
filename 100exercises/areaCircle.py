"""
Calculate the area of circle with a given radius
Formula: π r²
"""
import math

def areaCircle(radius):
    try:
        radius = float(radius)
        area = math.pi*radius**2
        print("Area: "f"{area}")
    except ValueError:
        print("Digite un numero válido")
    

radius = int(input("Digite el valor de radio: "))
areaCircle(radius)

import math

r = float(input("Radius r: "))
# circle
cir = 2.0*math.pi*r
area = math.pi * r ** 2
message = f"""Circle r: {r}
Circumference = {cir}
Area = {area}
"""
print(message)
# sphere
volume = 4.0 * math.pi / 3.0 * r ** 3
area = 4 * math.pi * r ** 2
message = f"""Sphere r: {r}
Volume = {volume}
Surface Area = {area}
"""
print(message)
# hypersphere
volume = math.pi ** 2 / 2.0 * r ** 4
area = 2 * math.pi ** 2 * r ** 3
message = f"""Hypersphere r: {r}
Volume = {volume}
Surface Area = {area}
"""
print(message)

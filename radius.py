import math

print("Please give a value")
r = input("Radius r: ")
if r.replace('.','').isdigit():
    r = float(r)
if isinstance(r, (int, float)) == False:
    print("please give a valid integer or float")
    exit(0)


def volume_nball (radius, dimensions):
    volume = math.pi ** (dimensions / 2) / math.gamma(dimensions/2+1) * radius ** dimensions
    return volume

def surface_nball (radius, dimensions):
    r = radius
    n = dimensions
    surface = 2 * math.pi ** (n/2) * r ** (n-1) / math.gamma(n/2)
    return surface

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
test = {volume_nball(r,3)}
test 2 = {surface_nball(r,3)}
"""
print(message)
# hypersphere
# n=4 # surface = 2 * math.pi ** 2 * r ** 3
# n=4 # volume = 1/2 * math.pi ** 2 * r ** 4
message = f"""Hypersphere r: {r}
Volume = {volume_nball(r,4)}
Surface Area = {surface_nball(r,4)}
"""
print(message)
# n-ball n = 5
message = f"""n-ball n: 5 r: {r}
Volume = {volume_nball(r,5)}
Surface Area = {surface_nball(r,5)}
"""
print(message)

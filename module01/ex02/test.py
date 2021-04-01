from vector import Vector

vec = Vector((10, 16))
print(vec)
vec = Vector(5)
print(vec)
vec = Vector([2.0, 3.0, 8.0, 7.0])
print(vec)
vec2 = Vector((0, 4))
print(vec2)
vec = vec.__add__(vec2)
print(vec)

print(vec + 'asd')
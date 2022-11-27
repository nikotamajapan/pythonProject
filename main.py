def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

c=circle_area_func(3)
cc=circle_area_func(3.14)

print(c(10))
print(cc(10))


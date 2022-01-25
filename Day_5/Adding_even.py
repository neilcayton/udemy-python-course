# 6. [Interactive Coding Exercise] Adding Even Numbers
add = 0
for i in range(2,101,2):
    add += i
print(add)

add = 0
for i in range(1,101):
    if i % 2 == 0:
        add += i
print(add)

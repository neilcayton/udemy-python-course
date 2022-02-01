# def greet_with(name, location):
#     print(f' hello {name}')
#     print(f' what it is like in {location}')
#
#
# greet_with(name="neil", location='london')
import math
test_h = int(input('what is the height: '))
test_w = int(input('what is the weight: '))
coverage = int(input('what is the coverage: '))


def point_calc(height, width, cov):
    area = height * width
    number_of_cans = math.ceil(area / cov)
    print(f"You'll need {number_of_cans} cans of paint")


point_calc(height=test_h, width=test_w, cov=coverage)

# 상위 폴더 import -> from 상위폴더명 import 모듈이름
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))


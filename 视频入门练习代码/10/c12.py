
import re

a = 'PythonPythonPythonPythonPython'

r = re.findall('(Python){3}', a)  # []里面是或关系，（）里是且关系
print(r)

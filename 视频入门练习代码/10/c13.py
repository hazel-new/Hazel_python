# re的第三个参数，模式匹配，可以有好几个，用|连接, 同时生效
# re.I 忽略大小写
# re.S 表示.将匹配所有字符，包括\n

import re

language = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}', language, re.I | re.S)
print(r)

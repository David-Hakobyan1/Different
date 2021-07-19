import re
import camelcase

txt = "hasri ep gar"
x = re.findall("ar",txt)
print(x)
y = re.search("ar",txt)
print(y.start())
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

import re
txt = input()
result = re.search('[a-b]*', '[1-6]{5}', txt)
if result:
    print(True)
else:
    print(False)
import re
pattern = re.compile(r'\d+')
# splits a string into a list delimited by the passed pattern
result = re.split(pattern, "A1B2C3D4E5F6")
if result:
    print result
else:
    print "fail to match"
import re
# compile regex to pattern object
pattern = re.compile(r'\d+')
# use re.match() to try to match the patten with given string
result1 = re.match(pattern, "123abc")  # re.match() will only match at the beginning of the string
                                       # and not at the beginning of each line.
if result1:
    print result1.group()
else:
    print "fail to match result1"

result2 = re.match(pattern, "abc123")

if result2:
    print result2.group()
else:
    print "fail to match result2"

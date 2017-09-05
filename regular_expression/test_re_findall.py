import re
pattern = re.compile(r'\d+')
# findall() is to scan the whole string and return all matched substrings in list
result = re.findall(pattern, "sdjia23023sdj231mdks02313kdm321")
if result:
    print result
else:
    print "fail to match"
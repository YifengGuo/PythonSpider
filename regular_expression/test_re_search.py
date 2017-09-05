import re
pattern = re.compile(r'\d+')

# re.search() is to scan the whole string and try
# to match the pattern and return
result = re.search(pattern, 'abc123efg')

if result:
    print result.group()
else:
    print "fail to match"

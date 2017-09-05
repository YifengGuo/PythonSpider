import re
pattern = re.compile(r'\d+')

# scan the whole string and return matched substring by iterator
results = re.finditer(pattern, "smi23jisjd2913ji32sdj22iej9i2")

for result in results:
    print result.group()


import requests
r = requests.get('http://www.baidu.com')
print 'content-->'+r.content  # return byte format
print 'text-->'+r.text  # return text format
print 'encoding-->'+r.encoding  # based on HTTP header then guess encoding of web page
r.encoding='utf-8'
print 'new  text-->'+r.text
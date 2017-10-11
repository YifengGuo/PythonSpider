import requests
r = requests.get('http://www.baidu.com')
# use status_code of Requests to get response code
# headers of Requests to get response header
if r.status_code == requests.codes.ok:
    print r.status_code  # to get response code
    print r.headers  # response header
    print r.headers.get('content-type')  # recommended way to get certain field of headers
else:
    r.raise_for_status()    # when status_code == 4xx or 5xx
                            # raise_for_status() will throw exception
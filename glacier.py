#!/usr/bin/env python2
'''
Upload an archive to glacier. Some references:

* https://github.com/paulengstler/glacier
* http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
* http://docs.amazonwebservices.com/amazonglacier/latest/dev/api-common-request-headers.html
* http://docs.amazonwebservices.com/amazonglacier/latest/dev/api-archive-post.html

'''
import requests

REGIONS={
    'US East': 'glacier.us-east-1.amazonaws.com',
}
REGIONS[None] = region['US East']
ACCOUNT_ID=''
VAULT_NAME=''

def upload_archive(region):
    url = 'http://%(region)s/%(account_id)s/vaults/%(vault_name)s/archives'
    params = {
        'region': REGIONS[region],
        'account_id': ACCOUNT_ID,
        'vault_name': VAULT_NAME,
    }
    headers = {
        'Date': ,
        'Authorization': ,
        'x-amz-archive-description': ,
        'x-amz-sha256-tree-hash': ,
        'x-amz-content-sha256': ,
    }
    requests.post(url % params, headers = headers, files = files)
Host: glacier.Region.amazonaws.com
x-amz-glacier-version: 2012-06-01
Date: Date
Authorization: SignatureValue
x-amz-archive-description: Description
x-amz-sha256-tree-hash: SHA256 tree hash
x-amz-content-sha256: SHA256 linear hash
Content-Length: Length


>>> url = 'http://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}

>>> r = requests.post(url, files=files)
>>> r.text

import hashlib
data = 'This a md5 test'
hash_md5 = hashlib.md5(data)
hash_md5.hexdigest()
import hashlib

hash = hashlib.new('sha1')
hash.update(input().encode())

print(hash.hexdigest())
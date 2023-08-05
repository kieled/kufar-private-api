import hashlib

SECRET = '49f6882c2234a1ec7f9acedb849852cbad7aa7e1'

def decode_signature(input_str: str):
    input_str = input_str + SECRET
    message_digest = hashlib.sha1()
    input_bytes = input_str.encode('utf-8')
    message_digest.update(input_bytes)
    hashed_str = message_digest.hexdigest()
    return hashed_str

import base64
import hashlib
import hmac

##rrwat: generated from keystone
def get_signature(url, secret):
    import pdb; pdb.set_trace()
    msg = base64.urlsafe_b64decode(str(url))
    key = str(secret)
    signed = base64.encodestring(
        hmac.new(key, msg, hashlib.sha1).digest()).strip()
    return signed


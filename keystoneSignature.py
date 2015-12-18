import base64
import hashlib
import hmac

##rrwat: generated from keystone
#url is you url after the base url-> http://localhost:5000/v3/create_user?xyz=abc will be create_user?xyz=abc
def get_signature(url, secret):
    import pdb; pdb.set_trace()
    msg = base64.urlsafe_b64decode(str(url))
    key = str(secret)
    signed = base64.encodestring(
        hmac.new(key, msg, hashlib.sha1).digest()).strip()
    return signed


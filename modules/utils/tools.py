import random
import string
import time
import json

def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_external_ref():
    timestamp = int(time.time())
    return "BILLY_" + generate_random_string(7) +  str(timestamp)

def is_json(jstr=None):
    if jstr != None:
        try:
            json_obj = json.loads(jstr)
            return True
        except ValueError as e: 
            return False
        return True
    else:
        return False

def json_loader(jstr=None):
    if is_json(jstr=jstr) == False:
        startidx = jstr.find('(')
        endidx = jstr.rfind(')')
        return json.loads(jstr[startidx + 1:endidx])
    else:
        return json.loads(jstr)
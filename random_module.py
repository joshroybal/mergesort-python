# module for generating random lists
from random import randint, random

def random_integer(): return randint(0, 2147483648)
def random_real(): return random()

def random_record():
    RECSIZ = 128
    NORECS = 405995
    idx = int(NORECS * random_real())
    direct_access = open('/home/slacker/dat/data.dat', 'rb')
    direct_access.seek(idx * RECSIZ)
    record = direct_access.read(RECSIZ);
    direct_access.close()
    return record.strip()

def random_list(n, fn):
    return [fn() for i in xrange(n)]

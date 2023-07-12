import random
import string
N = 15
external_id = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
print(external_id)
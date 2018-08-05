import os
import hashlib
import random



m = random.getrandbits(64)
print m
base_hash1 = hashlib.sha256(str(m))
base_hash2 = base_hash1.hexdigest()
base_hash = base_hash2[0:7]
print base_hash
found = False
num_trials = 0


while not found:
  num_trials = num_trials + 1
  m = m + 1 
  if num_trials % 100000000 == 0:
    print num_trials
  test_hash1 = hashlib.sha256(str(m))
  test_hash2 = test_hash1.hexdigest()
  test_hash = test_hash2[0:7]
  if(base_hash == test_hash):
    found = True
    print m
    print test_hash
    print num_trials

# 12744724942869876931
# above is the first number, below is its hash to 28 bits
# 8b169a2

# 12744724943394076582
# above is the second number, below is its hash to 28 bits
# 8b169a2

# below is the number of trials my code took
# 524199651

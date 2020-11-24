import hashlib

with open('top-10000-passwords.txt') as passwords_file:
  passwords = passwords_file.read().splitlines()

with open('known-salts.txt') as salts_file:
  salts = salts_file.read().splitlines()

def hash_matches(password, hash):
  return hashlib.sha1(password.encode()).hexdigest() == hash

def crack_sha1_hash(hash, use_salts=False):
  for password in passwords:
    if use_salts:
      for salt in salts:
        if hash_matches(salt + password, hash) |            hash_matches(password + salt, hash):
          return password

    else:
      if hash_matches(password, hash):
        return password
  
  return 'PASSWORD NOT IN DATABASE'
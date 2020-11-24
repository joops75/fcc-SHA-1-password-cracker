import hashlib

def hash_matches(password, hash):
  return hashlib.sha1(password.encode()).hexdigest() == hash

def crack_sha1_hash(hash, use_salts=False):
  with open('top-10000-passwords.txt') as passwords_file:
    for line in passwords_file:
      password = line.rstrip('\n\r')
      if use_salts:
        with open('known-salts.txt') as salts_file:
          for line in salts_file:
            salt = line.rstrip('\n\r')
            if hash_matches(salt + password, hash) |        hash_matches(password + salt, hash):
              return password

      else:
        if hash_matches(password, hash):
          return password
  
  return 'PASSWORD NOT IN DATABASE'
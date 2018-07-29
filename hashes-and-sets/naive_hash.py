HASH_MAX = 20

def naive_hash(str):
    sum = 0

    for char in str:
        sum += ord(char)

    return sum % HASH_MAX

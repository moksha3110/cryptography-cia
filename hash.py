def polynomial_hash(s):
    s = s.lower()
    p = 31
    m = 1000000007

    hash_value = 0
    power = 1

    for ch in s:
        if ch.isalpha():
            val = ord(ch) - 96
            hash_value = (hash_value + val * power) % m
            power = (power * p) % m

    return hash_value

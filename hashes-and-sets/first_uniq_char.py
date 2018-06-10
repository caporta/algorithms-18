def first_uniq_character(str):
    freq_hash = {}
    for char in str:
        if freq_hash.get(char) is not None:
            freq_hash[char] += 1
        else:
            freq_hash[char] = 1

    uniq_set = {char for char in freq_hash.keys() if freq_hash[char] == 1}
    for i, char in enumerate(str):
        if char in uniq_set:
            return i

    return -1

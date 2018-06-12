def get_first_uniq_char(str):
    first_uniq = float('inf')
    table = {}
    for i, char in enumerate(str):
        if char in table:
            table[char] = -1
        else:
            table[char] = i

    for key, val in table.items():
        if val != -1 and first_uniq > val:
            first_uniq = val

    return first_uniq if first_uniq < float('inf') else -1

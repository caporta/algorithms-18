def two_sum(addends, target_sum):
    table = {}
    for i, addend in enumerate(addends):
        comp_addend = target_sum - addend
        if comp_addend in table.keys():
            return table[comp_addend], i
        table[addend] = i

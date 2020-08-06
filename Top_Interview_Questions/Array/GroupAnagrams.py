def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = []
    hash_table = defaultdict(int)
    if len(strs) == 0:
        return ans
    if len(strs) == 1:
        ans.append(strs)
        return ans
    for element in strs:
        sorted_element = ''.join(sorted(element))
        if sorted_element not in hash_table:
            hash_table[sorted_element] = [element]
        else:
            hash_table[sorted_element].append(element)
    for k, v in hash_table.items():
        ans.append(v)
    return ans
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict
    # blank_count = strs.count("")
    # if blank_count >= 1:
    #     strs = [s for s in strs if s != ""]
    #     print(strs)

    # if len(list(set(strs))) == 1 and blank_count == 0:
    #     return [strs]
    anagrams = []
    # anagram_vals = []
    # balnk_arrs = []

    # sorted_strs = [''.join(sorted(s)) for s in strs]
    # sorted_original = {}

    # print(sorted_strs)
    # for i, s in enumerate(strs):
    #     sorted_original[s] = sorted_strs[i]
    
    
    # for key, val in sorted_original.items():
    #     anagrams.setdefault(val, []).append(key)

    # if blank_count >= 1:
    #     for i in range(1, blank_count+1):
    #         print(balnk_arrs)
    #         balnk_arrs.append("")
    #         print(balnk_arrs)
    #     anagrams = list(anagrams.values()) + [balnk_arrs]
    # return sorted(anagrams, key=len)
    
    # sorted_strs = [''.join(sorted(s)) for s in strs]
    # print(sorted_strs)
    # for i, s in enumerate(sorted_strs):
    #     temp = []
    #     if s == None: 
    #             continue
    #     j = i + 1
    #     for j in range(len(strs) - 1):
    #         if strs[j] == None: 
    #             continue
    #         if sorted(strs[j]) == sorted(s):
    #             temp.append(strs[j])
    #             strs[j] = None
    #             sorted_strs[j] = None
    #     if temp:
    #         anagrams.append(sorted(temp))

    # return sorted((anagrams), key=len)

    # words_in_hash = defaultdict(list)

    # for s in strs:
    #     words_in_hash[tuple(sorted(s))].append(s)
    
    # return list(words_in_hash.values())
    words_in_hash = {}

    for s in strs:
        if tuple(sorted(s)) not in words_in_hash.keys():
            words_in_hash[tuple(sorted(s))] = []
        words_in_hash[tuple(sorted(s))].append(s)
    return words_in_hash


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
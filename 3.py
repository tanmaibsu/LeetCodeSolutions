def lengthOfLongestSubstring(s: str):
    sub_strs = []
    if s == " " or len(s) == 1:
        return 1

    for i1, char1 in enumerate(s):
        sub_str = ""
        sub_str += char1
        for i2, char2 in enumerate(s[i1+1:], start=i1+1):
            if char2 not in sub_str:
                sub_str += char2
                if i2 == len(s) - 1:
                    sub_strs.append(sub_str)
                print(sub_str)
            else:
                if sub_str not in sub_strs:
                    print(sub_str)
                    sub_strs.append(sub_str)
                    break
                else:
                    break
        
    
    if len(sub_strs) == 0:
            return 0
    print(sub_strs)
    return len(max(sub_strs, key = len))

    # sub_str = ""
    # sub_strs = []
    # if s == " ":
    #     return 1
    # for index, char in enumerate(s):
        
    #     if char not in sub_str:
    #         sub_str += char
    #         print(sub_str)
    #         if index == len(s) - 1:
    #             sub_strs.append(sub_str)
    #         continue
    #     else:
    #         if sub_str not in sub_strs:
    #             sub_strs.append(sub_str)
            
    #         if index == len(s) - 1 and sub_str not in sub_strs:
    #             sub_strs.append(sub_str)
            
    #         sub_str = sub_str.replace(sub_str, char)

            # if s[index - 1] == char:
            #     sub_str = sub_str.replace(sub_str, char)
            #     continue
            # else:
            #     print("I am here")
            #     sub_str = sub_str.replace(sub_str, sub_str.replace(char, "") + str(char))
            #     print(sub_str)

    
    # if len(sub_strs) == 0:
    #         return 0
    # print(sub_strs)
    # return len(max(sub_strs, key = len))
    


print(lengthOfLongestSubstring("fstmtifkfvyyyrnlfnhedjkivvoxxoachwqcewmj"))
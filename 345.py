def swap_characters(string, index1, index2):
    str_list = list(string)
    str_list[index1], str_list[index2] = str_list[index2], str_list[index1]
    return ''.join(str_list) 

def reverseVowels(s: str) -> str:
        i = 0
        l = len(s) - 1
        print(l)
        j = l
        # if len(s) % 2 == 0:
        #     h_l = (l/2) + 1
        # else:
        h_l = l/2

        vowels = list(['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O','U'])
        reversed_s = s
        while i <= h_l:
            if s[i] in vowels:
                while j >= h_l:
                        if s[j] in vowels:
                            reversed_s = swap_characters(reversed_s, i, j)
                            j -= 1
                            break
                        j -= 1
            i += 1
        return reversed_s

print(reverseVowels("Marge, let's \"went.\" I await news telegram."))
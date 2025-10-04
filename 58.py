def lengthOfLastWord(s: str) -> int:
        splitted_s = s.split()
        str_without_spc = []
        for st in splitted_s:
            if st != " ":
                str_without_spc.append(st)
        print(str_without_spc)
        return len(str_without_spc[-1])


print(lengthOfLastWord("Hello World"))
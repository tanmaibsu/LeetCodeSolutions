def compress(chars: list[str]) -> int:

        s = []
        for i, char in enumerate(chars):
            count = 0
            if char != "":
                if char in s:
                    continue
                for c in chars:
                    # print(chars)
                    if char == c:
                        count += 1
                if count > 1 and count < 9:
                    s.append(char)
                    s.append(str(count))
                if count == 1:
                    s.append(char)
                if count > 9:
                    s.append(char)
                    s.append(str(count//10))
                    s.append(str(count%10))
        print(s)
        print(chars)
        # print(groups)
        return len(s)

compress(["a","a","b","b","c","c","c"])

class Solution:
    def countBits(self, n: int) -> List[int]:

        count_arr = [0] * (n+1)
        for i in range(n+1):
            bin_i = bin(i)[2:].count("1")
            count_arr[i] = bin_i
        
        return count_arr
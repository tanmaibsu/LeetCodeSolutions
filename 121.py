def maxProfit(prices: list[int]) -> int:
        
        diffs = []

        for i, elm in enumerate(prices):
            for j, elm1 in enumerate(prices[i+1:], start=i+1):
                diff = elm - elm1
                if diff < 0:
                    diffs.append(diff)
        
        return abs(min(diffs))

print(maxProfit([7,1,5,3,6,4]))

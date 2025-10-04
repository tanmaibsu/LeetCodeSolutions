def canPlaceFlowers(flowerbed, n):
        
        for i, elm in enumerate(flowerbed):
            if elm == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        if n > 0:
                            flowerbed[i] = 1
                            n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        if n > 0:
                            flowerbed[i] = 1
                            n -= 1
        return n == 0   

print(canPlaceFlowers([1,0,0,0,0,1], 2))
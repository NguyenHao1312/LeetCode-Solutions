class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0: return True
        
        for i in range(len(flowerbed)):
            # Kiểm tra vị trí i trống (0)
            # VÀ bên trái trống (hoặc là đầu luống)
            # VÀ bên phải trống (hoặc là cuối luống)
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1 # Trồng hoa vào
                n -= 1
                if n == 0: return True
                
        return False
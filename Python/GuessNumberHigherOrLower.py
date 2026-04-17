# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
class Solution(object):
    def guess(self, num):
        """
        :type num: int
        :rtype: int
        """
        pass
    
    def guessNumber(self, n):
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            res = self.guess(mid) # Gọi API đã được hệ thống định nghĩa sẵn
            
            if res == 0:
                return mid       # Đoán trúng
            elif res == -1:
                high = mid - 1   # Số bạn đoán lớn hơn số bí mật, tìm ở nửa trái
            else:
                low = mid + 1    # Số bạn đoán nhỏ hơn số bí mật, tìm ở nửa phải
                
        return -1
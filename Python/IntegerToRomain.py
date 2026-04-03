class Solution(object):
    def intToRoman(self, num):
        # Danh sách các cặp giá trị và ký hiệu La Mã (bao gồm cả các trường hợp đặc biệt)
        # Bắt buộc phải sắp xếp theo thứ tự giảm dần
        value_symbols = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        res = []
        
        # Duyệt qua từng cặp giá trị - ký hiệu
        for val, sym in value_symbols:
            if num == 0:
                break
            
            # Tìm số lượng ký hiệu hiện tại có thể lấy ra
            count = num // val
            
            if count > 0:
                res.append(sym * count) # Thêm ký hiệu vào danh sách kết quả
                num %= val              # Cập nhật lại số num (phần dư còn lại)
                
        # Nối các chuỗi lại với nhau và trả về
        return "".join(res)
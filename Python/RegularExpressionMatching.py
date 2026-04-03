class Solution(object):
    def isMatch(self, s, p):
        # Dùng dictionary để lưu lại các trạng thái đã tính toán
        memo = {}

        def dp(i, j):
            # Nếu trạng thái (i, j) đã có trong memo, trả về kết quả luôn
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Nếu pattern đã duyệt hết, chuỗi s cũng phải duyệt hết mới là True
            if j == len(p):
                ans = i == len(s)
            else:
                # Kiểm tra ký tự hiện tại có khớp không
                first_match = i < len(s) and p[j] in {s[i], '.'}
                
                # Xử lý trường hợp có dấu '*'
                if j + 1 < len(p) and p[j+1] == '*':
                    # 1. Bỏ qua ký tự và dấu * (dp(i, j + 2))
                    # 2. Khớp 1 ký tự và giữ nguyên pattern để xét tiếp (first_match and dp(i + 1, j))
                    ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    # Chuyển sang ký tự tiếp theo của cả s và p
                    ans = first_match and dp(i + 1, j + 1)
            
            # Lưu kết quả vào memo trước khi trả về
            memo[(i, j)] = ans
            return ans

        # Gọi hàm đệ quy bắt đầu từ index 0 của s và 0 của p
        return dp(0, 0)
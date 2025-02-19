def is_palindrome_number(n):
    s = str(n)  # Chuyển số thành chuỗi
    length = len(s)
    
    for i in range(length // 2):  # Duyệt từ 0 đến nửa độ dài chuỗi
        if s[i] != s[length - 1 - i]:  # So sánh ký tự đầu và cuối
            return False
    
    return True

# Kiểm tra
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
print(is_palindrome_number(1221)) # True
print(is_palindrome_number(12921)) # True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10  # Chia lấy phần nguyên

        return reverse == xcopy  
    ''' s = str(x)
        return s == s [::-1]'''

# Kiểm thử
solution = Solution()
test_cases = [121, 1234, 434, 989989, 33433, 1441]

for num in test_cases:
    print(f"{num} -> {solution.isPalindrome(num)}")

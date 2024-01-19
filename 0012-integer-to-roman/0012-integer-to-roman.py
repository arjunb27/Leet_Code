class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        num = roman_map[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                num += roman_map[s[i]]
            else:
                num -= roman_map[s[i]]
        return num

    def intToRoman(self, num: int) -> str:
        roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                          50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ""
        for value, numeral in roman_numerals.items():
            while num >= value:
                result += numeral
                num -= value
        return result

# Example usage
solution_instance = Solution()
integer_value = solution_instance.romanToInt("IX")
print(integer_value)  # Output: 9

roman_numeral = solution_instance.intToRoman(9)
print(roman_numeral)  # Output: IX

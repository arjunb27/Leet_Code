class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for left symbols
        leftSymbols = []
        # Loop for each character of the string
        for c in s:
            # If left symbol is encountered
            if c in ['(', '{', '[']:
                leftSymbols.append(c)
            # If right symbol is encountered
            elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
                leftSymbols.pop()
            elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
                leftSymbols.pop()
            # If none of the valid symbols is encountered
            else:
                return False
        return leftSymbols == []

# Example usage
solution_instance = Solution()
result = solution_instance.isValid("()[]{}")
print(result)

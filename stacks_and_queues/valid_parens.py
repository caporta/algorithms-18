class ParenValidator:
    @staticmethod
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        openers = {'(', '{', '['}
        stack = []

        for char in s:
            if char in openers:
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        if not stack:
            return True

        return False

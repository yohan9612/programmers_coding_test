class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Set
        """
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(s) == set(suffix):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

        """
        Stack
        """
        counter, seen, stack = collections.Counter(s), set(), []

        for c in s:
            counter[c] -= 1
            if c in stack:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)

        return ''.join(stack)

from queue import LifoQueue 
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        parentheses_dict = {'(':')','[':']','{':'}'}
        stack = LifoQueue(maxsize = len(s))
        for ch in s:
            if ch in parentheses_dict:
                stack.put(ch)
            else:
                if stack.qsize() == 0:
                    return False
                if parentheses_dict[stack.get()] != ch:
                    return False
        if stack.qsize() != 0:
            return False
        return True
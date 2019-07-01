class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 0:
            return ''
        stack = []
        for v in path.split('/'):
            if v == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            elif v == '.' or v == '':
                continue
            else:
                stack.append(v)
        return '/' + '/'.join(stack)

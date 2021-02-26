class SimplifyPath:
    def simPath(self,path):
        stack=[]
        for p in path.split('/'):
            if p=='..':
                if stack:
                    stack.pop()
            elif p and p !='.':
                stack.append(p)
        return '/'+'/'.join(stack)
obj=SimplifyPath()
print(obj.simPath("/a/./b/../../c/"))
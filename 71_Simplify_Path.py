#Given an absolute path for a file (Unix-style), simplify it.

#For example,
#path = "/home/", => "/home"
#path = "/a/./b/../../c/", => "/c"

## SOLUTION: Split on '/' ignoring '.' and ''. Create a stack and iterate through the created list. 
# If the element observed is '..' pop from the stack (we are moving a folder up) 
# else append the new element to the stack.

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p!="." and p!=""]
        
        stack = []
        for p in places:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

""" Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might 
  get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.

"""

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        if name[i] != typed[j]:
            return False
        
        while i < len(name) or j < len(typed):
            count_n, count_t = 0, 0
            while i < len(name)-1 and name[i] == name[i+1]:
                count_n += 1
                i += 1
            while j < len(typed)-1 and typed[j] == typed[j+1]:
                count_t += 1
                j += 1
            if count_n > count_t:
                return False
            
            if i >= len(name) or j >= len(typed):
                return False
            
            if name[i] != typed[j]:
                return False

            i += 1
            j += 1

        return True
                

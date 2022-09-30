class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sor = {}
        temp= []
        sp = " "
        s = list(s.split(' '))
        for i in s:
            num = int(i[-1])
            i = i[:-1]
            sor[num-1] = i
        for key in sorted(sor):
            temp.append(sor[key])
        final = sp.join(temp)
            
       
        return final
    
e = Solution()
print(e.sortSentence("is2 sentence4 This1 a3"))
        

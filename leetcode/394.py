class Solution:
    def decodeString(self, s: str) -> str:
        l1 = []
        final = ''
        inter = ''
        i = 0
        while i < len(s):
            inter = ''
            if s[i] in string.digits:
                #print("digit", s[i])
                rep = int(s[i])
                i += 2
                while s[i] in string.ascii_letters:
                    #print("letter", s[i])
                    inter += s[i]
                    i += 1
                #print("inter", inter)
                if s[i] == ']':
                    final = ''
                    #print('close bracket', s[i])
                    i += 1
                    final += inter * rep
                    #print("final", final)
                    l1.append(final)
                else:
                    l1.append(rep)
                    l1.append(inter)
                #print("iteration", l1)
            else:
                if s[i] in string.ascii_letters:
                    l1.append(s[i])
                i += 1
        
        #print('-'*10)
        final = ''
        j = 0
        rep = 1
        while j < len(l1):
            inter = ''
            pattern = ''
            if str(l1[j]) in string.digits:
                #print("join digit", l1[j])
                rep = l1[j]
                j += 1
            else:
                #handle letters
                while j < len(l1):
                    if l1[j] not in string.digits:
                        pattern += l1[j]
                        j += 1
                #print("pattern", pattern)
                #print("rep", rep)
                inter = pattern * rep
            final += inter
            #print("real final:", final)
        
        return final

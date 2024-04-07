class Solution:
    # Need to track indexes correctly as the list shrinks. That's why DDRRR fails.
    def predictPartyVictory(self, senate: str) -> str:
        l1 = list(senate)
        cnt = Counter() 
        i = 0
        while i < len(l1):
            cnt = Counter(l1)
            print(f"Before cnt: {cnt.items()}")
            if l1[i] == "R":
                if cnt['R'] > cnt['D']:
                    return "Radiant"
            elif l1[i] == "D":
                if cnt['D'] > cnt['R']:
                    return "Dire"

            print(f"Before i: {i}, l1: {l1}")
            if l1[i] == 'R':
                if 'D' in l1:
                    l1.pop(l1.index('D'))
            elif l1[i] == "D":
                if 'R' in l1:
                    l1.pop(l1.index('R'))
            print(f"After i: {i}, l1: {l1}")
            cnt = Counter(l1)
            print(f"After cnt: {cnt.items()}")
            print('-' * 10)
            i += 1
        
        if cnt['R'] > cnt['D']:
            return "Radiant"
        elif cnt['D'] > cnt['R']:
            return "Dire"

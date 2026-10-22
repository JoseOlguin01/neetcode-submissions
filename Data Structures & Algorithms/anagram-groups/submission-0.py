class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for word in strs:
            ksort = ''.join(sorted(word))
            if ksort in ana:
                ana[ksort].append(word)
            else:
                ana[ksort] = [word]
        
        return list(ana.values())


class Solution:
    def encode(self, strs: List[str]) -> str:
        coded = ""
        for word in strs:
            coded += str(len(word)) + "#" + word
        return coded
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            i = end
            
        return decoded
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()
        aux = {}
        flag = 0
        res = []

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for n, c in counts.items():
            if c in aux:
                aux[c].append(n)
            else:
                aux[c] = [n]


        for key, value in sorted(aux.items(), reverse=True):
            for n in value:

                if flag >= k:
                    break
                res.append(n)
                flag += 1
            
            if flag >= k:
                break
        
        return sorted(res)



        

            

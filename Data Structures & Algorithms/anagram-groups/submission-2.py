class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        result = defaultdict(list)


        for s in strs:
            sortedS = "".join(sorted(s))
            result[sortedS].append(s)


        # result = {[act]: [act], [cat], [hat]...}

        return list(result.values())

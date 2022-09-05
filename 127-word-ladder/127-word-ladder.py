from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbors=defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
                
        visit=set([beginWord])
        queue=[]
        queue.append(beginWord)
        ans=1
        
        while queue:
            for i in range(len(queue)):
                word=queue.pop(0)
                if word==endWord:
                    return ans
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for n in neighbors[pattern]:
                        if n not in visit:
                            visit.add(n)
                            queue.append(n)
            ans+=1
        return 0
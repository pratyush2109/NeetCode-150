class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
            
        curr.endOfWord=True

    def search(self, word: str) -> bool:
        def fun(index, root):
            if index == len(word):
                if root.endOfWord:
                    return True
                return False
            if word[index] in root.children:
                return fun(index+1, root.children[word[index]])
            else:
                if word[index] == '.':
                    for key, value in root.children.items():
                        if fun(index+1, value):
                            return True
                return False
        return fun(0, self.root)
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
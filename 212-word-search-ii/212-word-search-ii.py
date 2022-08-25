class TrieNode:
    '''
    provide a trie node
    '''
    def __init__(self):
        self.children = dict()
        self.end = False
        
class Trie:
    '''
    implement trie
    '''
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()   
            node = node.children[char]
        node.end = True
        
    def prune(self, word):
        '''
        word has to be added before calling prune
        Go to the last node and marked the end as false
        then maintain a list of traversed key and node pairs
        delete a node only if it is a leaf node and it is not an end
        if currNode has children or being an end of other word then break immediately
        '''
        node = self.root
        path = [(None, node)]
        for char in word:
            node = node.children[char]
            path.append((char, node))
        node.end = False
        
        for i in range(len(path)-1, 0, -1):
            char, currNode = path[i][0], path[i][1]
            parentNode = path[i - 1][1]
            if currNode.end or currNode.children:
                break
            del parentNode.children[char]
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
            
        res = []
        visited = set()
        m, n = len(board), len(board[0])
        
        def dfs(i, j, node, word):
            if i < 0 or i == m or j < 0 or j == n or board[i][j] not in node.children or (i, j) in visited:
                return
            
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.end:
                res.append(word)
                trie.prune(word)
                
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            visited.remove((i, j))
    

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, '')

        return res
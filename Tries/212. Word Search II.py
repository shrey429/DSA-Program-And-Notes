# getting TLE using the logic of 'word search 1' i.e serarching the word one by one.
# time: O(w.m*n.4^(m*n))  , w: # words

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans= []
        for word in words:
            print(word,"word")
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.dfs(board, i, j, word):
                        ans.append(word)
        return list(set(ans))   # we can get duplicate of same word if any word can be formed from more than one way.

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


# we can optimise the above problem to O(m*n.4^(m*n)) + O(n) (for inserting all words into Trie).
# logic: First insert all words into the Trie.
# search from each cell in the matrix only one time. (here we are searching from each cell only one time not 'w' time for each word)
# And if we find any word then add into the ans.

# We are removing the 'word' from the trie after we have found that to reduce the time complexity.
# since we only need only distinct word. 
# and there are chances that we can get the same word from different starting point.

class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.isWord= False
        self.prefix_count= 0   # will tell no of word staring with a given prefix. after every node you are inserting increase this count.

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        cur.prefix_count+= 1
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
            # increase the prefix count of this node.
            cur.prefix_count+= 1
        # now increase the word_count for this node.
        cur.isWord= True
    
    def removeWord(self, word):
        cur= self.root
        cur.prefix_count-= 1
        for c in word:
            cur= cur.children[c]
            cur.prefix_count-= 1
        cur.isWord= False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert all words into Trie.
        trie= Trie()
        for word in words:
            trie.insert(word)

        # now start searching from each cell.
        rows, cols= len(board), len(board[0])
        ans= set()  # storing in set since same word can be formed from more than one cell as starting node.
        visited= set()  # to check if we have already visited any cell.
        
        def dfs(r, c, node, word):
            # write all the invalid possible cases together.
            if r <0 or r== rows or c < 0 or c== cols or (r,c) in visited or board[r][c] not in node.children or node.prefix_count < 1:
                return 
            word+= board[r][c]
            visited.add((r,c))
            node= node.children[board[r][c]]
            # we can get any matching word anytime so keep checking after each node.
            if node.isWord:
                ans.add(word)
                trie.removeWord(word)
            # visit all the four possible directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            # now backtrack
            visited.remove((r, c))
        
        # # now start searching from each cell.
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie.root, "")

        return (list(ans))


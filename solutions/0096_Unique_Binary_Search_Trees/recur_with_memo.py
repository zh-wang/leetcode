# STAR

class Solution:
    def numTrees(self, n: int) -> int:
        # num of unique BST with index from 0 to n
        dp = [0 for _ in range(n)]
        return self.recur(dp, 0, n-1)

    def recur(self, dp, i, j):
        '''
        calc num of unique BST with index from i to j
        BST whose root index is i, has all node in left subtree smaller than i,
        and all node in right subtree larger than i.
        '''
        if dp[j-i] > 0:
            return dp[j-i]
        if i == j:
            dp[j-i] = 1
        else:
            # pick a root, split range i to j into two parts
            #
            # [0, 1, 2, ... , 8, 9]
            #     ^ <-------> ^
            for k in range(i+1, j): # for k as the root, multipy #left-sub-tree & #right-sub-tree
                dp[j-i] += self.recur(dp, i, k-1) * self.recur(dp, k+1, j)
            # [0, 1, 2, ... , 8, 9]
            #  ^
            dp[j-i] += self.recur(dp, i+1, j)
            # [0, 1, 2, ... , 8, 9]
            #                    ^
            dp[j-i] += self.recur(dp, i, j-1)
        return dp[j-i]

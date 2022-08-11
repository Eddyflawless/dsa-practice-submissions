
def tree_sum(root):
    if root is None: #base case
        return 0

    leftSum = tree_sum(root.left)
    rightSum = tree_sum(root.left)
    return root.data + leftSum + rightSum



def tree_max(root):
    if root is None: #base case
        return float("-inf")

    leftMax = tree_max(root.left)
    rightMax = tree_max(root.left)
    return max(root.data, leftMax , rightMax)   

        
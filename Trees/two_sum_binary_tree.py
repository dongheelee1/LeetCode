class TreeNode(object): 

  def __init__(self, value): 
    self.val = value
    self.left = None 
    self.right = None 


def treeToList(root, res):
  #base case 
  if root is None: 
    #backtrack 
    return res 
  else: 
    res.append(root.val)
    res = treeToList(root.left, res)
    res = treeToList(root.right, res)
  return res 

def twoSum(lst, target): 

  hashList = []

  for i in range(len(lst)): 
    remainder = target - lst[i]

    if remainder in hashList: 
      return [lst[i], remainder]
    else: 
      hashList.append(remainder)

  return None

root = TreeNode(10)
root.right = TreeNode(5)
root.left = TreeNode(15)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)

l = treeToList(root, [])
res = twoSum(l, 20)
print(res)

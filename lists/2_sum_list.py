def twoSumList(nums, target): 

  '''
  idea: 

  initialize a hashmap 

  loop through the data

    subtract current element from target 

    check to see if remainder is in hashmap 

    if remainder is in the hashmap 

      make result[0] = current element 
      make result[1] = remainder 
    
    otherwise 
      add current element to the hashmap 

  '''

  hashmap = {}
  
  for i in range(len(nums)): 
      
      
      remainder = target - nums[i] #remainder is key in the hashmap
      
      if remainder in hashmap: 
          return [hashmap[remainder], i]
      else: 
          hashmap[nums[i]] = i 

  return hashmap

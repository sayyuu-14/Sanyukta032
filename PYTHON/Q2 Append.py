def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
  print("After appending", middleThree)
  
appendMiddle("Chrisdem", "IamNewString")
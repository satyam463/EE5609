class point:
  '''
  A class for 3 Dimensional Points
  '''
  def __init__(self,x_val,y_val,z_val):
    self.x = x_val
    self.y = y_val
    self.z = z_val

def check(p1,p2,p3,p4):
  '''
  A function to check wheather two lines are parallel or perpendicular 
  Args : p1,p2,p3,p4 (point objects) where p1,p2 belongs to the first line and p3,p4 belongs to the second line.
  returns: "Parallel", "Perpendicular" and "Neither Parallel nor Perpendicular"
  '''
  # Direction ratios for Line 1
  a1 = p2.x - p1.x
  b1 = p2.y - p1.y
  c1 = p2.z - p1.z
  # Direction ratios for Line 2
  a2 = p4.x - p3.x
  b2 = p4.y - p3.y
  c2 = p4.z - p3.z

  print("Direction Ratios for Line 1: ",a1,b1,c1)
  print("Direction Ratios for Line 2: ",a2,b2,c2)

  if (a1/a2==b1/b2 and a1/a2==c1/c2):
    "Satisfies the condition for being parallel"
    return "Parallel"
  elif (a1*a2 + b1*b2 + c1*c2 == 0):
    "Satisfies the condition for being perpendicular"
    return "Perpendicular"
  else:
    "Neither parallel nor perpendicular"
    return "Neither Parallel nor Perpendicular"

# Driver Code

# Line 1
P1 = point(1,-1,2) 
P2 = point(3,4,-2)

# Line 2
P3 = point(0,3,2)
P4 = point(3,5,6)

print ("The lines through the given points are : {}".format(check(P1,P2,P3,P4)))
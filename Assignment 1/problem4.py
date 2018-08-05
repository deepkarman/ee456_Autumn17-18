#y^2=x^3+9x+5 over field mod 13

import os

for t in range(0,13):
  x = ((t^3)+(9*t)+5)%13
  if x == 1:
    print '({},1)'.format(t)
    print '({},-1)'.format(t)
    print '({},12)'.format(t)
    print '({},-12)'.format(t)
  elif x == 4:
    print '({},2)'.format(t)
    print '({},-2)'.format(t)
    print '({},11)'.format(t)
    print '({},-11)'.format(t)
  elif x == 9:
    print '({},3)'.format(t)
    print '({},-3)'.format(t)
    print '({},10)'.format(t)
    print '({},-10)'.format(t)
  elif x == 3:
    print '({},4)'.format(t)
    print '({},-4)'.format(t)
    print '({},9)'.format(t)
    print '({},-9)'.format(t)
  elif x == 12:
    print '({},5)'.format(t)
    print '({},-5)'.format(t)
    print '({},8)'.format(t)
    print '({},-8)'.format(t)
  elif x == 10:
    print '({},6)'.format(t)
    print '({},-6)'.format(t)
    print '({},7)'.format(t)
    print '({},-7)'.format(t)
  elif x == 3:
    print '({},4)'.format(t)
    print '({},-4)'.format(t)
  elif x == 0:
    print '({},0)'.format(t)
  else: 
    print '{} does not have a solution'.format(t)

#0 does not have a solution
#(1,4)
#(1,9)
#2 does not have a solution
#3 does not have a solution
#(4,3)
#(4,10)
#(5,2)
#(5,11)
#(6,5)
#(6,8)
#7 does not have a solution
#(8,6)
#(8,7)
#9 does not have a solution
#(10,0)
#11 does not have a solution
#12 does not have a solution
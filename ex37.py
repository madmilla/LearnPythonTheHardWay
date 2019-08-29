#Keywords
# Needs to be extended with examples.
keyword     Description                                                         Example
And         Logical and.                                                        True and False == False
as          Part of the with as statement                                       With X as Y: pass
assert      Assert (ensure) that something is true                              assert False, "Error"
break       Stop this loop right now                                            while True: Break
class       Define a class                                                      class Person(object)
continue    Don't process more of the loop, do it again                         while True: continue
def         define a function                                                   def X(): pass
del         Delete from dictionary                                              del X[Y]
elif        Else if condition                                                   if: X; elif: Y; else: J
else        Else condition                                                      if: X; elif: Y; else: J
except      if an exception happens, do this.                                   except ValueError, e: print(e)
exec        Run a string as Python                                              exec 'print("Helloo")'
finally     Exceptions or not, finally do this no matter what                   finally: pass
for         Loop over a collection of things                                    for X in Y: pass
from        Importing specific parts of a module                                from x import Y
global      Declare that you want a global variable                             global X
if          If condition                                                        if: X; elif: Y; else: J
import      import a module into this one to use                                import os
in          part of for-loops. Also a test of X in Y.                           for X in Y: pass also 1 in [1] == True
is          like == to test equality.                                           1 is 1 == True
lambda      create a short anonymous function                                   s = lambda y: y**y; s(3)
not         logical not                                                         not True == False
or          logical or                                                          True or False == True
pass        This block is empty.                                                def empty(): pass
print       Print this string                                                   print("this string")
raise       Raise an exception when things go wrong                             raise ValueError("No")
return      Exit the function with a return value.                              def X(): return Y
try         Try this block, and if exception, go to except.                     Try: pass
while       While loop.                                                         while X: pass
with        With an expression as a variable do.                                with X as Y: pass
yield       Pause here and return to caller                                     def X(): yield Y; X().next()

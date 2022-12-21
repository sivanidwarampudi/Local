"""try:
   print("before")
   raise TypeError("type mismatch")
   print("after")
except TypeError as e:
    print(e)"""

"""try:
   print("before")
   2/0
   raise TypeError("mismatch")
   print("after")
except ZeroDivisionError:
    print("caught")
except TypeError as e:
    print(e)
#except (TypeError,ZeroDivisionError) as e:
    #print(e)"""
#except:only mentioning this takes sll exceptions or except Exception
#when no exception raised else block gets executed
"""try:
   print("before")
   print("after")
except ZeroDivisionError:
    print("caught")
else: 
    print("nothing") 
finally:
    print("done")"""
    
"""def a():
    try:
        b()
        def b():
            try:
                c()
            except ZeroDivisionError:
                print("caught")
                def c():
                    try:
                        b()
                    except TypeError:
                        print("GF")"""

l=[x for x in dir(__builtins__)  if x.endswith("error") and x.__base__!='Exception']
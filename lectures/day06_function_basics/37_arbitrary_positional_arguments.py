def func(*args):
    print(args)
    print(type(args))

func() # () <class 'tuple'>
func(1) # (1,) <class 'tuple'>
func(1,2) # (1,2,) <class 'tuple'>
func(1,2,3) # (1,2,3) <class 'tuple'>
func(1,2,3,4) # (1,2,3,4) <class 'tuple'>
func(1,2,3,4,5) # (1,2,3,4,5) <class 'tuple'>
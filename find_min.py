import functools
strs = ["ashish","jyoti","flower","lily","cam"]

res = functools.reduce(lambda x,y: x if len(x) < len(y) else y,strs)

print((len(res)))
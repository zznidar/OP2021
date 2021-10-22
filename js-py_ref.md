js  | py
:-------------: | :-------------:
`for(a of array)`  | `for a in arr:`
`for(key in dict)` | `for key in dict:`
`typeof(var)` | `type(var)`
`` `test ${var1+var2} test` `` | `f"test {var1+var2} test"`
`[first, second, ...rest] = [1, 2, 3, 4];` | `first, second, *rest = [1, 2, 3, 4]`
`sum = (x, y) => x + y;` | `sum = lambda x, y: x + y`
`var1 && var2` | `var1 and var2`
`else if` | `elif`
`[].push(el)` | `[].append(el)`
`dict?.key \|\| default` | `dict.get(key, default)`
`5/(0 \| 1)` | `5/(0 or 1)`
`10>5 ? true : false` | `True if 10>5 else False`
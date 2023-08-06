# xstr

#### New python3 strings just dropped. 

# Installation

```bash
cd <project>
https://github.com/Donny-GUI/xstr.git
```

```python3
from xstr import ustr
from xtr import dstr
from xstr import hstr
```

or

```python3

import xstr

```

or 

```python3
import hstr
# import dstr
# import ustr
```


# HypenString  --    hstr()

```python3
from xstr import hstr


x = hstr('hello new world and all who inhabit it.')
print(x)
# hello-new-world-and-all-who-inhabit-it.
print(x.original())
# hello new world and all who inhabit it.

```

output


```output
hello-new-world-and-all-who-inhabit-it.
hello new world and all who inhabit it.
```


# DotString   --  dstr()  

```python3
from xstr import dstr


x = dstr('hello new world and all who inhabit it.')
print(x)
# hello.new.world.and.all.who.inhabit.it.
print(x.original())
# hello new world and all who inhabit it.

```


output


```output
hello.new.world.and.all.who.inhabit.it.
hello new world and all who inhabit it.
```

# UnderlineString --  ustr()  

```python3
from xstr import ustr


x = ustr('hello new world and all who inhabit it.')
print(x)
# hello_new_world_and_all_who_inhabit_it.
print(x.original())
# hello new world and all who inhabit it.

```

output


```output
hello_new_world_and_all_who_inhabit_it.
hello new world and all who inhabit it.
```


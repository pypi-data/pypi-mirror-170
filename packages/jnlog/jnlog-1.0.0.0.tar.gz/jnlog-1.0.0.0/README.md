# jnlog
### ___Simple to use colored text logger for python___
#### How to use:
```python
from jnlog import jnlog
name = 'MyScript' #used to identify one logger in many
loglevel = jnlog.INFO
logger = jnlog.jnlog(name=name, loglevel=loglevel)
logger.info('Hello, World!')
```
#### result:
![](prev.png)

See example.py for more 

### loglevels:
| fn\ll   | INFO | WARNING | ERROR |
|---------|------|---------|-------|
| info()  | +    | -       | -     |
| warn()  | +    | +       | -     |
| error() | +    | +       | +     |

### license: MIT
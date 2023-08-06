# Ascii Geometry
A simple library for drawing geometrical shapes using ascii characters

### Installation
```
pip install ascii_geometry
```

### Quick Demo
```
from ascii_geometry import AsciiContext

if __name__ == '__main__':
    #Create context object
    ctx = AsciiContext('0')
    
    #print a triangle of length 10
    print(ctx.get_triangle(10))

```

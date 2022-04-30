# pdto

**P**ython **D**ictionary **T**o **O**bject — function used to transform dictionaries into classes.  
Nested dictionaries are transformed into nested classes.

🙋‍♂️ **Why does this exist ?**  
➜ Python needed another bad-performance useless tool 🧠  
➜ Plus it looks like JavaScript now, be ready to rock these "ninja developer" 🐱‍👤 and "js sorcerer" 🧙‍♂️ interviews.

## How to use

```python
dct = {
    'str': 'str value',
    'dct': {'key': 'value'},
    'lst': ['v1', 'v2'],
    '_1': 1923,
    '1': 1924
}

obj = pdto(dct)

print(f"Obj: {obj}")
print(f"Obj.str: {obj.str}")
print(f"Obj.1: {obj.s1}")
print(f"Obj._1: {obj._1}")
print(f"Obj.dct: {obj.dct}")
print(f"Obj.dct.key: {obj.dct.key}")
print(f"Obj.lst: {obj.lst}")
print(f"Obj.lst[0]: {obj.lst[0]}")
```

# Input and Output

## Strings

Tbh, as you can probably tell from the other modules, I just use
```python
f"My text: {my_variable}"
```

Mainly because it is more readable and easier to use.

But it also has the perk of being the fastest formatter - performance wise.

### .format()

The only valid case at least for me, is the one I go over in [1_formatting_strings.py](./1_formatting_strings.py).

## Files

There is the old way and there is the good practice.

Both use `open()`, but the second one uses `with`.

### Common modes

From my experience, you'll usually employ 3 modes:

1. `r` - only for reading a file, not writing.
2. `r+` - reading AND writing BUT the file must exist.
3. `a` - reading AND appending WITHOUT deleting the existing content of the file like `w`.

### Old way which I won't cover

```python
f = open('workfile', 'w', encoding="utf-8")
```

Don't use it for a few reasons the documentation already covers.

# Resources

1. [Reading and Writing Files in Python 3.](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

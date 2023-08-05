# Colors1 library for Python

__A library for working with colors in Python.__

## Installation

```bash
pip install colors1
```

## Usage

```python
from colors1 import colors

print(colors.terminalRed + "This is red" + colors.end)
```
Add `colors.terminalRed` or any color before your 
string to make the string
colored, and use `colors.end`
to end the color. Use
`colors.terminal` colors ONLY FOR TERMINAL PRINTING.

You can also use `colors.hexRed` or `colors.rgbRed`
to get the hex or rgb value of a color.

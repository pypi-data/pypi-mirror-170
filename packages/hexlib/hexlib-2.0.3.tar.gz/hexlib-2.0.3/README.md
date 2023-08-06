# Description

Basic tools to read, format, filter and display hex values

# Installation

`pip install hexlib`

# Usage

- The class `HexTwin` is a hexadecimal representation of a file
  - `HexTwin` reads a file in 16 byte chunks
  - Each of this chunks is saved as as tuple together with the following information:
    - tuple[0] = Offset 
    - tuple[1] = A bytearray containing the 16 bytes
    - tuple[2] = A boolean indicating if the bytes are all zero 
    - tuple[3] = A boolean indicating if the bytes are all non ASCII values
- The class `Hexdump` format and prints `HexTwin` instances

# Example

```python
from hexlib.HexTwin import HexTwin
from hexlib.Hexdump import Hexdump

# 1.) HexTwin instance
twin = HexTwin("path/to/file/test.txt")
dump = Hexdump()

# Activates filtering for zero rows
dump.filter(filterZeroRows=True) 
dump.printTwin("path/to/result.txt", twin)

# Activates filtering for non-ascii rows (Includes also zero rows)
dump.filter(filterNonAsciiRows=True) 
dump.printTwin("path/to/result.txt", twin)

# 2.) Create HexTwin from bytes (Filtering can also be used here)
f = open("path/to/file", "rb")
twinFromBytes = HexTwin.fromBytes(f.read(16))
dumpFromBytes = Hexdump()

dumpfromBytes.printTwin("path/to/bytes-result.txt", twinFromBytes)

# 3.) Create a HexTwin from a offset reading x bytes (Filtering can also be used here)
twinFromOffset = HexTwin.fromOffset("path/to/file.txt", offset=50, noOfBytes=10)
dumpFromOffset = Hexdump()

dumpFromOffset.printTwin("path/to/offset-result.txt", twinFromOffset)
```

# License

MIT
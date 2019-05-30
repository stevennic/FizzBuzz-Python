# Preparation
To build an executable, make sure you have pyinstaller: 
`pip install pyinstaller`

# Test
Testing requires pytest: `pip install pytest`

To run all unit tests, `cd` to `test/` and run: `pytest test.py`

# Build
Windows:
`build.bat [destination]`

Linux: `./build.sh [destination]`

If a destination is not specified, the executable will go to `src/dist`

You can also deploy your artifacts to network paths:

`build.bat \\Integration\Debug`

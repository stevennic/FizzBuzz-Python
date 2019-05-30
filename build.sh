#!/bin/bash
if [ "$1" ]; then
    distpath="--distpath $1"
fi

cd src
echo Building standalone executable
pyinstaller main.py -y -F ${distpath}

echo Building source distribution
python3 setup.py sdist

echo Building binary Wheel distribution
python3 setup.py bdist_wheel
@ECHO OFF
SETLOCAL
IF "%~1" NEQ "" (SET distpath=--distpath %1)

@cd src
@echo Building standalone .exe
pyinstaller main.py -y -F %distpath%

@echo Building source distribution
python setup.py sdist

@echo Building binary Wheel distribution
python setup.py bdist_wheel

@cd ../
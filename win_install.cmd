@echo off
python --version 2>NUL
if errorlevel 1 goto nopython
:yespython
echo Installing/Updating Ursina Engine...
pip install ursina
echo Installing/Updating Perlin Noise...
pip install perlin-noise
python3 voxel.py
goto:eof

:nopython
echo Installing Python...
winget install Python
echo Press any key to continue :)
pause>nul
echo Installing/Updating Ursina Engine...
pip install ursina
echo Installing/Updating Perlin Noise...
pip install perlin-noise
echo Installing/Updating Numpy...
pip install numpy
goto:eof


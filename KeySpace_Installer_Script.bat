@echo off
title Installing KeySpace...
color 81
set load=
set/a loadnum=0
:Loading
set load=%load%лл
cls
echo.
echo Loading Data...
echo -----------------------------------------
echo %load%                    
echo -----------------------------------------
echo.
echo.
echo Made by Velocity7
ping localhost -n 2 >nul
set/a loadnum=%loadnum% +1
if %loadnum%==20 goto Done
goto Loading
:Done
echo.
pause
cls
tree
pip install customtkinter
move "%UserProfile%\Downloads\KeySpace Package\KeySpace" "%AppData%\KeySpace"
move "%AppData%\KeySpace\ShortCut\*.*" "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
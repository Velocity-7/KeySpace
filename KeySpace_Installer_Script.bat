@echo off
title Connecting to Blunt Mark Server's...
color 81
set load=
set/a loadnum=0
:Loading
set load=%load%��
cls
echo.
echo Connecting to Server...
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
title {Connection Established}
cls
tree
pip install customtkinter
move "%UserProfile%\Downloads\KeySpace Package\KeySpace" "%AppData%\KeySpace"
move "%AppData%\KeySpace\ShortCut\*.*" "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
@echo off
title Updating KeySpace...
color 81
set load=
set/a loadnum=0
:Loading
set load=%load%��
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
rename "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\KeySpace V1.5.lnk" "KeySpace V1.8.lnk"
rmdir /q /s %AppData%\KeySpace
move "%UserProfile%\Downloads\KeySpace_Package_V1.8\KeySpace" "%AppData%\KeySpace"
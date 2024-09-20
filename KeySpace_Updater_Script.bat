@echo off
title Updating KeySpace...
color 81
set load=
set/a loadnum=0
:Loading
set load=%load%ŰŰ
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
attrib "%AppData%\KeySpace\KeySpace.py" -h
attrib "%AppData%\KeySpace\KeySpace.py" -r
del /q /s %AppData%\KeySpace\KeySpace.py
rename "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\KeySpace V1.8.lnk" "KeySpace V2.0.lnk"
rename "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\KeySpace V1.5.lnk" "KeySpace V1.8.lnk"
rename "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\KeySpace V1.0.lnk" "KeySpace V1.8.lnk"
attrib "%UserProfile%\Downloads\KeySpace_Package_V1.8\KeySpace\KeySpace.py" -h
move "%UserProfile%\Downloads\KeySpace_Package_V1.8\KeySpace\KeySpace.py" "%AppData%\KeySpace"
attrib "%AppData%\KeySpace\KeySpace.py" +h

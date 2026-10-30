@echo off
rem `openfilm` for cmd.exe: every path expands from LOCALAPPDATA / USERPROFILE, so no
rem non-ASCII literal sits in this file (cmd.exe reads it in the OEM code page).
setlocal
set "OF_EXE=%LOCALAPPDATA%\Programs\OpenFilm\OpenFilm.exe"
set "OF_CLI=%LOCALAPPDATA%\Programs\OpenFilm\resources\app.asar\node_modules\openfilm\bin\openfilm.mjs"
set "ELECTRON_RUN_AS_NODE=1"
set "OPENFILM_NO_UPDATE_CHECK=1"
set "PLAYWRIGHT_BROWSERS_PATH=%LOCALAPPDATA%\Programs\OpenFilm\resources\runtime\ms-playwright"
set "PATH=%LOCALAPPDATA%\Programs\OpenFilm\resources\runtime\ffmpeg;%PATH%"
"%OF_EXE%" "%OF_CLI%" %*

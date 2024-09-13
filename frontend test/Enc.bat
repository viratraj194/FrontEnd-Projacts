@echo off
set "key_file=key.key"
set "ignore_files=encrypt.bat decrypt.bat %key_file%"

:: Check if the key exists
if not exist %key_file% (
    openssl rand -base64 32 > %key_file%
)

for %%f in (*.*) do (
    set "current_file=%%f"
    call :check_ignore %%f
)

exit /b

:check_ignore
for %%i in (%ignore_files%) do (
    if /i "%~nx1"=="%%i" exit /b
)

:: Encrypt the file
echo Encrypting %~nx1...
openssl enc -aes-256-cbc -salt -in "%~nx1" -out "%~nx1.enc" -pass file:%key_file%
del "%~nx1"
exit /b

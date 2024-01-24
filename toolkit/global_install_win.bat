@echo off
SET "PS_COMMAND=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -ExecutionPolicy Bypass -Command"

echo Installing Chocolatey...
%PS_COMMAND% "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
echo Chocolatey installation complete.

echo Installing Python 3...
choco install python3 -y
echo Python 3 installation complete.

echo Installing Python dependencies...
pip install -r requirements.txt
echo Python dependencies installation complete.

pause

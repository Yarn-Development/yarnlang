@echo off
echo "Adding new Path..."
cd "C:\%username%\"
mkdir .yrn
setx /M path "%path%;C:\%username%\.yrn\"
echo "PATH Successfully Added at C:\%username%\.yrn\"
move yrn.bat C:\%username%\.yrn\ 
echo "YarnLang Successfully Installed. Files can now be run using yrn <file>.yrn"
echo "Thank you for installing YarnLang!"
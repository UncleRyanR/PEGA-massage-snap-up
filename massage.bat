@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
powershell -ExecutionPolicy RemoteSigned -File massage.ps1
REM powershell -ExecutionPolicy RemoteSigned -File D:\Tools\massage.ps1
REM pause
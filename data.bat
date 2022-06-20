BREAK> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\system_info.txt
BREAK> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\task_list.txt 
BREAK> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\net_user.txt 
BREAK> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\software_list.txt 
ECHO off
CLS
systeminfo >> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\system_info.txt
tasklist >> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\task_list.txt
net user >> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\net_user.txt
CLS

reg export HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall temp1.txt
find "DisplayName" temp1.txt| find /V "ParentDisplayName" > temp2.txt
for /f "tokens=2,3 delims==" %%a in (temp2.txt) do (ECHO %%a >> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\software_list.txt)
ECHO ================= >> D:\facultate\Dizertatie\python\build\exe.win-amd64-3.10\data\software_list.txt
DEL temp1.txt
DEL temp2.txt

exit
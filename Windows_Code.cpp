// Cyber Patriot Code
// Written by Moses Arocha
// This code will attempt to follow password history, account lockouts, audit logs, security options
// turn on firewall, updates, disable and stop services, deny ports

#include <iostream>
#include <string> 
#include <ctime>
#include <vector>


using namespace std;

int main() 
{
    cout << "\n\t Welcome To The Cyber Patriot Code For Windows Machines!\n" << endl;
    cout << "\n\n\t What Is The First Thing You Would Like To Do?" << endl;
    system("NetSh Advfirewall set allprofiles state on"); // enables the firewall
    system("net user guest /active:no");                  // disables the guest user account
    system("net user /add Moses moses");                  // adds users
    system("net localgroup administrators Moses /add");   // adds user as admin
    system("net stop wuauserv");
    cout << " \n\t Enables Remote Desktop:"
         << "reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f";
    cout << "\n\t Disables Remote Desktop:"
         << "reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f";
         
    return 0;
}

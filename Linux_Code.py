#!/usr/bin/env python2
# written by Moses Arocha

from Tkinter import *

import tkMessageBox
import json
import os


window = Tk()
window.title("CyberPatriot Code")
window.geometry("350x50")
window.configure(background="#a1bdcd")


def getIP():
    print ipVar


attack = Label(window, text=" Please Check Attacking IP ADDRESS Before Attacks")
enter = Button(window, text = "Check IP", command = getIP)


ipVar = raw_input(" Please Insert IP Address: ")

attack.pack()
enter.pack()


def Tshark():
    filewin = Toplevel(window)
    button = Button(filewin, text="Verison Of Tshark")
    RunTshark = os.system('tshark -v')
    print RunTshark  
    button.pack()


def TsharkInstall():
    filewin = Toplevel(window)
    button = Button(filewin, text="Installing Tshark")
    InstallTShark = os.system('sudo apt-get update | sudo apt-get upgrade | sudo apt-get install tshark')
    print InstallTShark
    button.pack()


def TsharkSetup():
    filewin = Toplevel(window)
    button = Button(filewin, text="If Tshark doesn't Work")
    FixTShark = os.system('sudo dpkg-reconfigure wireshark-common | sudo adduser wireshark')
    print FixTShark
    button.pack()


def help():
    filewin = Toplevel(window)
    button = Button(filewin, text="This code is written in Python and uses the Terminal as output. In order to get the full effect please run this code as a SuperUser.")
    button.pack()


def about():
    filewin = Toplevel(window)
    button = Button(filewin, text="This is a program, written by Moses Arocha which utilizes the tools of Nmap and Tshark for the Holmes High School CyberPatriot Team. All Rights Reserverd.")
    button.pack()


def TsharkNetworkAdapter():
    filewin = Toplevel(window)
    button = Button(filewin, text=" Should State: 1. eth0 2. nflog 3.nfqueue 4. any 5.lo")
    NetworkAdapter = os.system('sudo tshark -D')
    print NetworkAdapter
    button.pack()


def TsharkAny():
    filewin = Toplevel(window)
    button = Button(filewin, text=" Monitoring Any Network...")
    AnyMonitor = os.system('sudo tshark -i any')
    print AnyMonitor
    button.pack()


def TsharkEth():
    filewin = Toplevel(window)
    button = Button(filewin, text=" Monitoring Ethernet Only...")
    EthMonitor = os.system('sudo tshark -i -eth0')
    print EthMonitor
    button.pack()


def TsharkSpecs():
    filewin =Toplevel(window)
    button = Button(filewin, text=" Package Number, Time Stamp, Sender's IP Address, Receiver's IP Address, Package Contents")
    Specification = os.system('sudo tshark -i any -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e col.Info')
    print Specification
    button.pack()


# beginning of code for Nmap

def Nmap():
    ipstring="sudo nmap -v "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Ping, SYN Stealth Scan, TCP Port Scan")
    Ping = os.system(ipstring)
    print Ping
    button.pack()


def NmapPing():
    ipstring="sudo nmap -sP "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Ping Scan")
    Ping = os.system(ipstring)
    print Ping
    button.pack()


def NmapSyn():
    ipstring="sudo nmap -sS "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Syn Scan")
    Syn = os.system(ipstring)
    print Syn
    button.pack()

def NmapUDP():
    ipstring="sudo nmap -sU "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="UDP Port Scan")
    UDP = os.system(ipstring)
    print UDP
    button.pack()

def NmapPort():
    ipstring="sudo nmap -p1-65535 "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Full Port Scan")
    FullPort = os.system(ipstring)
    print FullPort
    button.pack()
  
def NmapVersion():
    ipstring="sudo nmap -sV "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Version Detection")
    Verison = os.system(ipstring)
    print Verison
    button.pack()

def NmapOS():
    ipstring="sudo nmap -O "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="OS Detection")
    OSD = os.system(ipstring)
    print OSD
    button.pack()

def NmapIPv6():
    ipstring="sudo nmap -6 "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="IPv6 Scan")
    IPv6 = os.system(ipstring)
    print IPv6
    button.pack()
 
def NmapSpoofing():
    macadd = raw_input(" Please Enter Attacking MAC ADDRESS: ")
    ipstring="sudo nmap --spoof-mac "+macadd
    filewin =Toplevel(window)
    button = Button(filewin, text="Ping, SYN Stealth Scan, TCP Port Scan")
    macattack = os.system(ipstring)
    print macattack
    button.pack()

def NmapAggressive():
    ipstring="sudo nmap -A "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Aggressive Scan")
    Aggressive = os.system(ipstring)
    print Aggressive
    button.pack()

def NmapConnection():
    ipstring="sudo nmap -sT "+ipVar
    filewin =Toplevel(window)
    button = Button(filewin, text="Connection Detection")
    Connect = os.system(ipstring)
    print Connect
    button.pack()
   
menubar = Menu(window)
tsharkmenu = Menu(menubar, tearoff=0)
tsharkmenu.add_command(label="Version Of Tshark", command=Tshark)
tsharkmenu.add_command(label="Install Tshark", command=TsharkInstall)
tsharkmenu.add_command(label="Set Up Tshark", command=TsharkSetup)
tsharkmenu.add_command(label="Network Adapters List", command=TsharkNetworkAdapter)
tsharkmenu.add_command(label="Network Monitor Any Network", command=TsharkAny)
tsharkmenu.add_command(label="Network Monitor Ethernet Only", command=TsharkEth)
tsharkmenu.add_command(label="Specifics In Traffic Request", command=TsharkSpecs)

tsharkmenu.add_separator()

tsharkmenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Tshark", menu=tsharkmenu)
nmapmenu = Menu(menubar, tearoff=0)

nmapmenu.add_separator()

nmapmenu.add_command(label="Ping, SYN Scan", command=Nmap)
nmapmenu.add_command(label="Ping Scan Only", command=NmapPing)
nmapmenu.add_command(label="Syn Scan Only", command=NmapSyn)
nmapmenu.add_command(label="Connection Scan", command=NmapConnection)
nmapmenu.add_command(label="UDP Port Scan", command=NmapUDP)
nmapmenu.add_command(label="All Port Scan", command=NmapPort)
nmapmenu.add_command(label="Version Dectection", command=NmapVersion)
nmapmenu.add_command(label="OS Detection", command=NmapOS)
nmapmenu.add_command(label="Aggressive Scan", command=NmapAggressive)
nmapmenu.add_command(label="IPv6 Scan", command=NmapIPv6)
nmapmenu.add_command(label="Mac Spoofing", command=NmapSpoofing)

menubar.add_cascade(label="Nmap", menu=nmapmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)


window.mainloop()

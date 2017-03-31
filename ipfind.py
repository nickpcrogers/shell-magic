#!/usr/bin/env python3
import os
import subprocess
import sys

def is_local_ip(string,subnet='192.168.1'):
    """checks if "string" is an ip on "subnet" (the masked part of the IP) """
    return subnet in string

def get_last_byte(ip):
    """Return the last byte of an ip address"""
    return os.path.splitext(ip)[1].lstrip('.')

def main():
    """Print out free ip addresses on local subnet."""

    print("getting arp-scan output...")
    try:
        ip_info = subprocess.check_output(['arp-scan','--local']).decode().split()
    except subprocess.CalledProcessError:
        print("You need to be root for arp-scan.")
        sys.exit()


    used_ips = (word for word in ip_info if is_local_ip(word))
    used_idents = [int(get_last_byte(ip)) for ip in used_ips] #must not be generator
    free_idents = (i for i in range(1,255) if i not in used_idents)

    for i in free_idents:
        print(i)

if __name__=='__main__':
    main()


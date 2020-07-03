
""""
Create a file to add
                6 Devices (2 Cisco routers, 2 Cisco Switches & 2 Juniper routers)
                2 vlans,
                2 SVIs with IP addressing & router OSPF configuration

> Ensure the configuration is listed under each device's hostname and  is based on device type and vendor
> Use a CSV file to import the VLAN number, IP address, device type and vendor information

"""

import csv

with open ("net1devices.csv", "r") as f:
    read = csv.DictReader(f)
    for row in read:
        if row["Device Vendor"] == "Cisco" and row ["Device Type"] == "router":
            interface = row["Interface"]
            ip = row["ip address"]
            mask = row["Subnet Mask"]
            interface1 = row["Interface1"]
            ip1 = row["ip address1"]
            mask1 = row["Subnet Mask1"]
            print(row["Hostname"])
            print("config t")
            print(f"interface {interface}")
            print(f"ip address {ip} {mask}")
            print("!")
            print(f"interface {interface1}")
            print(f"ip address {ip1} {mask1}")
            print("end""\n")
        elif row["Device Vendor"] == "Juniper" and row ["Device Type"] == "router":
            interface = row["Interface"]
            ip = row["ip address"]
            mask = row["Subnet Mask"]
            print(row["Hostname"])
            print("configure")
            print(f"set interface {interface} family inet unit 0 family inet address {ip}{mask}")
            print(f"set protocols ospf area 0.0.0.0 {ip}")
            print(f"set protocols ospf interface {interface}")
            print("commit and-quit""\n")


import ipaddress


def ip_to_int32(ip="128.114.17.104"):
    print(int(ipaddress.IPv4Address(ip)))


ip_to_int32()
import ipaddress

def int32_to_ip(int32=2154959208):
    # your code here
    return str(ipaddress.IPv4Address(int32))

print(int32_to_ip())



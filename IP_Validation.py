"""
Task: IP Validation
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they:
 - consist of four octets, with values between 0 and 255, inclusive.
 - leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string, e.g. '123.45.67.89'
"""


def is_valid_IP(ip_str):
    ip_list = ip_str.split(".")
    if len(ip_list) != 4:
        return False
    for elem in ip_list:
        if not elem.isdigit() or int(elem) > 255 or (len(elem) > 1 and elem[0] == "0"):
            return False
    return True


# Test
print(f"Expected res: {True}. Current result: {is_valid_IP('127.1.1.0')}")
print(f"Expected res: {True}. Current result: {is_valid_IP('0.0.0.0')}")
print(f"Expected res: {True}. Current result: {is_valid_IP('0.34.82.53')}")
print(f"Expected res: {False}. Current result: {is_valid_IP('192.168.1.300')}")
print(f"Expected res: {False}. Current result: {is_valid_IP('192a.168.1.300b')}")
print(f"Expected res: {False}. Current result: {is_valid_IP('01.0.1.0')}")
print(f"Expected res: {False}. Current result: {is_valid_IP('123.456.789.0')}")
print(f"Expected res: {False}. Current result: {is_valid_IP('12.34.56 .1')}")
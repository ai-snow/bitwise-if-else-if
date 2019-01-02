# Array positiions (starting at 1)
x1 = 0b00000001
x2 = 0b00000010
x3 = 0b00000011

# Bit masks for corresponding array positions (y1 = bitmask for x1, etc)
y1 = 0b00100100
y2 = 0b01001100
y3 = 0b10010010

# Variable representing 255
m = 0b11111111

# Example input bit values (to be checked against bitmasks)
z1 = 0b00111100

# 'a' variables will be equal to 00000000 if z1 conforms to the corresponding bitmask (y values)
# otherwise, at least one bit will be 1
a1 = ((z1 & y1) | (y1 ^ m)) ^ m
a2 = ((z1 & y2) | (y2 ^ m)) ^ m
a3 = ((z1 & y3) | (y3 ^ m)) ^ m

# 'test_y' variables will be 1 (if 'a' is 00000000) or 0 (else)
test_y1 = (((a1 | (~a1 + 1)) >> 7) & 1) ^ 1
test_y2 = (((a2 | (~a2 + 1)) >> 7) & 1) ^ 1
test_y3 = (((a3 | (~a3 + 1)) >> 7) & 1) ^ 1

# 'flag_1' will be 11111111 if 'test_y1' is 1, otherwise 00000000
flag_1 = ((1 << 8) - 1) & (((test_y1 << 7) >> 7) - 1) ^ m
# 'flag_2' will be 11111111 if 'test_y1' is 0 and 'test_y2' is 1, otherwise 00000000
flag_2 = ((1 << 8) - 1) & (((((test_y1 ^ 1) & test_y2) << 7) >> 7) - 1) ^ m
# 'flag_3' will be 11111111 if 'test_y1' is 0 and 'test_y2' is 0 and 'test_y3' is 1, otherwise 00000000
flag_3 = ((1 << 8) - 1) & (((((test_y1 ^ 1) & (test_y2 ^ 1) & test_y3) << 7) >> 7) - 1) ^ m

# 'pos' will then be the position corresponding to 'z1'
pos = (
    (flag_1 & x1)
    | (flag_2 & x2)
    | (flag_3 & x3)
)

print(pos)

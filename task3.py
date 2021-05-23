import struct


def f31(bytecode):
    solve = {}
    bytecode = bytecode[5:]

    #-----_a1-a4_------
    solve['A1'] = struct.unpack('<q', bytecode[0: 8]) [0]
    solve['A2'] = struct.unpack('<q', bytecode[8: 16]) [0]
    solve['A3'] = struct.unpack('<q', bytecode[16: 24]) [0]

    #-------B-------
    lenght_b = struct.unpack('<H', bytecode[24: 26]) [0]
    adress_b = struct.unpack('<I', bytecode[26: 30]) [0] - 5

    B = []
    for i in range(adress_b,adress_b+lenght_b*28, 28):
        temp_struct = {}
        temp_adress = struct.unpack('<I', bytecode[i:i+4])[0]-5

        temp_struct['B1'] = struct.unpack('<H', bytecode[i: i+2]) [0]

        temp_struct['B2'] = struct.unpack('<i', bytecode[i+2: i+6]) [0]

        #-----C------
        C = {}
        C['C1'] = struct.unpack('<I', bytecode[i + 6: i + 10])[0]
        C['C2'] = struct.unpack('<f', bytecode[i + 10: i + 14])[0]
        C['C3'] = struct.unpack('<q', bytecode[i + 14: i + 22])[0]
        C['C4'] = struct.unpack('<B', bytecode[i + 22: i + 23])[0]
        C['C5'] = struct.unpack('<i', bytecode[i + 23: i + 27])[0]

        temp_struct['B3'] = C

        temp_struct['B4'] = struct.unpack('<b', bytecode[i+27: i+28]) [0]

        B.append(temp_struct)

    #------a4------
    solve['A4'] = B

    solve['A5'] = struct.unpack('<I', bytecode[30: 34]) [0]

    # -------D-------
    adress_d = struct.unpack('<I', bytecode[34: 38])[0] - 5

    D = {}
    D['D1'] = struct.unpack('<d', bytecode[adress_d: adress_d + 8])[0]
    D['D2'] = "".join([
        struct.unpack('<c', bytecode[adress_d + 8: adress_d + 9])[0].decode(),
        struct.unpack('<c', bytecode[adress_d + 9: adress_d + 10])[0].decode()
    ])
    D['D3'] = struct.unpack('<b', bytecode[adress_d + 10: adress_d + 11])[0]
    D['D4'] = struct.unpack('<I', bytecode[adress_d + 11: adress_d + 15])[0]
    D['D5'] = struct.unpack('<f', bytecode[adress_d + 15: adress_d + 19])[0]

    adress_e = struct.unpack('<I', bytecode[adress_d + 19: adress_d + 23])[0] - 5

    E = {}
    E['E1'] = struct.unpack('<I', bytecode[adress_e: adress_e + 4])[0]
    E['E2'] = struct.unpack('<B', bytecode[adress_e + 4: adress_e + 5])[0]

    lenght_float = struct.unpack('<H', bytecode[adress_e + 5: adress_e + 7])[0]
    adress_float = struct.unpack('<H', bytecode[adress_e + 7: adress_e + 9])[0] - 5

    float_array = []
    for i in range(adress_float, adress_float + lenght_float * 4, 4):

        float_array.append(struct.unpack('<f', bytecode[i: i + 4])[0])

    E['E3'] = float_array
    E['E4'] = struct.unpack('<f', bytecode[adress_e + 9: adress_e + 13])[0]
    E['E5'] = struct.unpack('<B', bytecode[adress_e + 13: adress_e + 14])[0]
    E['E6'] = list(struct.unpack('<ffff', bytecode[adress_e + 14: adress_e + 30]))
    E['E7'] = struct.unpack('<b', bytecode[adress_e + 30: adress_e + 31])[0]
    E['E8'] = struct.unpack('<B', bytecode[adress_e + 31: adress_e + 32])[0]

    D['D6'] = E

    solve['A6'] = D
    solve['A7'] = struct.unpack('<b', bytecode[38: 39])[0]
    solve['A8'] = struct.unpack('<Q', bytecode[39: 47])[0]

    return solve

print(f31(b'VLPZ\x81\x14!0\x82MJ\xc9\xf518?z\xc1p\x8f2\x15\xc6\x15\x14\xe0\x0b\x1c'
b'E\x02\x004\x00\x00\x002\xbe\xf7\xb9\x94\x00\x00\x00\x8b\x94e\x8b\xd6'
b'\xb0\x9e@6\t\xd4\x8f\\\xee|\x1d\xff\x13\x00\xe1\x95!?\x1e/W\x9cp\xac'
b'J\x1d\x0c\xcb\xc5S+B\xa0dM;\xe9c4l\xc1\x8drk\xd3>\x17\xff\n8-\xce-\x04#\xbb'
b"qV\xd7\x8c\x89\xde\xd6\xbe\x1f\x8d*?^\x01\x08y\x00\x02\x00l\x00h'L"
b'?\x05\xb6\xb7g\xbf\x8d\x86\xa4\xbdo\x7f\x81>\x9d\x02\xa9=P\xa6`\xbe5\x93'
b'\xde1\xc2\xbfmb\xf59 SK9\x03\x06\xbft\x00\x00\x00'
)=={'A1': -735975367341235948,
'A2': 3643254599847983153,
'A3': 4979868345002477077,
'A4': [{'B1': 54281,
'B2': 2095996047,
'B3': {'C1': 1310493,
'C2': 0.631193220615387,
'C3': 2110688975035772702,
'C4': 12,
'C5': 726910411},
'B4': 66},
{'B1': 25760,
'B2': 1676229453,
'B3': {'C1': 2378263604,
'C2': 0.41292911767959595,
'C3': 301123443712786199,
'C4': 35,
'C5': -682200645},
'B4': -116}],
'A5': 3120021042,
'A6': {'D1': -0.14214689434037364,
'D2': 'mb',
'D3': -11,
'D4': 1263738937,
'D5': -0.5234866738319397,
'D6': {'E1': 2030567774,
'E2': 0,
'E3': [-0.4196665585041046, 0.6662158370018005],
'E4': 0.7974762916564941,
'E5': 5,
'E6': [-0.9051469564437866,
-0.08033476024866104,
0.2529253661632538,
0.08252451568841934],
'E7': 80,
'E8': 166}},
'A7': -117,
'A8': 3909298958908482964})

print(f31((b'VLPZ\x81ey\xda\x00:\xa2\x00\x8e\x921\x8bK\xa3\xd7c4\x9ea\xe2\x88\x85\xcf\x81'
b'\xc3\x02\x004\x00\x00\x00~1\x14\xb4\x94\x00\x00\x00\xfd\xe7\x81\r\x16'
b'\xeb+\xe8\x92\xb5\xde\xb8~\x17\xde!\x95k\x85\x94{\xd1>g\xf9KhB\xf6J.\xb6Q'
b"^[\x1e?'\x7f\xc0\xe4\xd4\x15\x85\xd3\x16i\xad1`\xbfy\xf5\xb7\xfe\xf4}"
b'\xdd]\xea\xfb\xdfe~{\xcf\xfa$\xbfte\xe6>)\x1c\x92j\xe4\x02\x00l'
b'\x00\x1f\xdb\x08\xbe\xa2vL^\xbf\xc4\x86q\xbfd;/\xbf\xe8\xdb#?$A'
b'\x06\x98\x1c\x92\x10r\xe4?wt^c\xb1\xc7_\xc4\xa8z\xbft\x00\x00\x00')
)=={'A1': -8214387350317663899,
'A2': 3775098009013662098,
'A3': -4358974791883791970,
'A4': [{'B1': 57013,
'B2': -568885576,
'B3': {'C1': 2238420257,
'C2': 0.40914595127105713,
'C3': 3335749239099357543,
'C4': 182,
'C5': 509304401},
'B4': 63},
{'B1': 32551,
'B2': 366273728,
'B3': {'C1': 1763103621,
'C2': -0.8757579922676086,
'C3': 6763700706579314041,
'C4': 234,
'C5': 2120605691},
'B4': 123}],
'A5': 3021222270,
'A6': {'D1': 0.6389239171737706,
'D2': 'wt',
'D3': 94,
'D4': 1606922595,
'D5': -0.979137659072876,
'D6': {'E1': 1787960361,
'E2': 228,
'E3': [-0.6444520354270935, 0.4499927759170532],
'E4': -0.13364838063716888,
'E5': 162,
'E6': [-0.8683542013168335,
-0.943462610244751,
-0.684499979019165,
0.6400742530822754],
'E7': 36,
'E8': 65}},
'A7': -3,
'A8': 10585759212821643751})

class C32:
    def __init__(self):
        self.state = 'A'

    def hoard(self):
        states = {
            'A': [0, 'B'],
            'B': [2, 'C'],
            'D': [5, 'E'],
            'E': [7, 'B'],
            'F': [9, 'G']
        }
        try:
            return_value = states[self.state][0]
            self.state = states[self.state][1]
            return return_value
        except KeyError:
            raise RuntimeError

    def base(self):
        states = {
            'C': [3, 'D'],
            'E': [6, 'F']
        }
        try:
            return_value = states[self.state][0]
            self.state = states[self.state][1]
            return return_value
        except KeyError:
            raise RuntimeError

    def rev(self):
        states = {
            'A': [1, 'G'],
            'C': [4, 'C'],
            'E': [8, 'E']
        }
        try:
            return_value = states[self.state][0]
            self.state = states[self.state][1]
            return return_value
        except KeyError:
            raise RuntimeError


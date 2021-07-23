base_chrs = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
chrsdic = dict(zip(base_chrs, range(64)))


def encode(text: str, encoding='ASCII'):
    src = text.encode(encoding)
    ret = bytearray()
    r = 0
    for i in range(0, len(src), 3):
        block = src[i:i+3] 
        if len(block) < 3:
            r = 3 - len(block)
            block += b'\x00' * r 
        num = int.from_bytes(block, 'big')
        for j in range(4):
            k = (4-j-1)*6
            c = (num >> k) & 0x3f
            ret.append(base_chrs[c])

    for i in range(1, r+1):
        ret[-i] = int.from_bytes(b'=', 'big')

    return bytes(ret).decode(encoding)
 
 
def decode(text: str, encoding='ASCII'):
    src = text.encode(encoding)
    ret = bytearray()
    for i in range(0, len(src), 4):
        block = src[i:i+4]
        tmp = 0x00
        cnt = 0
        for j in range(4):
            index = chrsdic.get(block[-j-1]) 
            if index is not None:
                tmp += index << j*6
            else: 
                cnt += 1
        num = tmp.to_bytes(3, 'big')       
        ret.extend(num) 

    for k in range(cnt):
        ret.pop()

    return bytes(ret).decode('ASCII')

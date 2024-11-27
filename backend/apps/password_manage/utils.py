def str_to_bin(sstr):
    return ''.join([str(bin(ord(i)))[2:].rjust(8, '0') for i in sstr])


def bin_to_str(listt: str) -> str:
    return ''.join([chr(int(i, 2)) for i in listt])


def main(key, passwd, mode):
    key = str_to_bin(key).ljust(128, '0')
    K, C, c = '', '', 1
    is_key: int = sum([1 for i in passwd if not (i == '1' or i == '0')])

    if is_key == 0:
        try:
            x, y, z = key[:41], key[41:87], key[87:128]

            while len(K) != len(passwd):
                k = int(x[-1]) ^ int(y[-1]) ^ int(z[-1])
                x_n, y_n, z_n = [x[13], x[-1], x[-2], x[-3]], [y[-1], y[-2]], [z[-1], z[-2], z[-3]]
                x_n = eval('^'.join(x_n))
                x = str(x_n) + x[:-1]
                y_n = eval('^'.join(y_n))
                y = str(y_n) + y[:-1]
                z_n = eval('^'.join(z_n))
                z = str(z_n) + z[:-1]
                K += str(k)
                c += 1

            C = ([str(int(passwd[i]) ^ int(K[i])) for i in range(len(K))])

            if mode == 's':
                return '_'.join([str(hex(int(''.join(C[i:i + 8]), 2)))[2:] for i in range(0, len(C), 8)])

            if mode == 'd':
                return bin_to_str([''.join(C[i:i + 8]) for i in range(0, len(C), 8)])

        except Exception as m:
            return m

    else:
        print('Ключ введён неверно!')


def shifr(key, passwd):
    mode = 's'
    passwd = str_to_bin(passwd)
    return main(key, passwd, mode)


def deshifr(key, passwd):
    mode = 'd'
    passwd = ''.join([bin(int(i, 16))[2:].rjust(8, '0') for i in passwd.split('_')])
    return main(key, passwd, mode)

def permute(input_bits, permutation):
    return [input_bits[i] for i in permutation]

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def split(bits):
    mid = len(bits) // 2
    return bits[:mid], bits[mid:]

def s_box(input_bits, sbox):
    row = int(f"{input_bits[0]}{input_bits[3]}", 2)
    col = int(f"{input_bits[1]}{input_bits[2]}", 2)
    return [int(x) for x in f"{sbox[row][col]:02b}"]

def fk(bits, subkey):
    left, right = split(bits)
    expanded_right = permute(right, [3, 0, 1, 2, 1, 2, 3, 0])
    xor_result = [bit ^ k for bit, k in zip(expanded_right, subkey)]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    s0_result = s_box(xor_result[:4], s0)
    s1_result = s_box(xor_result[4:], s1)
    p4 = permute(s0_result + s1_result, [1, 3, 2, 0])
    left = [l ^ p for l, p in zip(left, p4)]
    return left + right

def generate_keys(key):
    p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    p8 = [5, 2, 6, 3, 7, 4, 9, 8]
    key = permute(key, p10)
    left, right = split(key)
    left, right = left_shift(left, 1), left_shift(right, 1)
    key1 = permute(left + right, p8)
    left, right = left_shift(left, 2), left_shift(right, 2)
    key2 = permute(left + right, p8)
    return key1, key2

def sdes_encrypt(plaintext, key):
    ip = [1, 5, 2, 0, 3, 7, 4, 6]
    ip_inv = [3, 0, 2, 4, 6, 1, 7, 5]
    k1, k2 = generate_keys(key)
    plaintext = permute(plaintext, ip)
    result = fk(plaintext, k1)
    left, right = split(result)
    result = right + left
    result = fk(result, k2)
    ciphertext = permute(result, ip_inv)
    return ciphertext

if __name__ == "__main__":
    key_input = input("Enter a 10-bit key: ")
    plaintext_input = input("Enter an 8-bit plaintext: ")

    key = [int(bit) for bit in key_input]
    plaintext = [int(bit) for bit in plaintext_input]

    if len(key) != 10 or len(plaintext) != 8:
        print("Invalid input lengths.")
    else:
        ciphertext = sdes_encrypt(plaintext, key)
        print("Ciphertext:", ''.join(map(str, ciphertext)))

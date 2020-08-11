import string
import copy

from PA import strxor


def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c


CTS = [
    '315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b1634'
    '9c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553'
    'ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb'
    '36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a1'
    '9b159610b11ef3e',
    '234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b0'
    '7df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132'
    'eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa'
    '76eb7b4ab24171ab3cdadb8356f',
    '32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b0'
    '7df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527'
    'dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb',
    '32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a0'
    '29056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f457543'
    '2c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca'
    '670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c140'
    '4e1315a1010e7229be6636aaa',
    '3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe5680'
    '8c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562'
    'e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa'
    '065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070',
    '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a1'
    '9d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472'
    'e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aeb'
    'c66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0'
    'cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be8'
    '7a59c355d25f8e4',
    '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b0'
    '1c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d2'
    '98e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf'
    '261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582'
    'afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb'
    '6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce',
    '315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce5680'
    '1d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132'
    'ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f'
    '276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3',
    '271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e0'
    '4d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132'
    'ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa'
    '270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081'
    'ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027',
    '466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed395'
    '98005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3'
    'b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83',
]

target = '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aa' + \
    'c650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef1' + \
    '21336cb85ccb8f3315f4b52e301d16e9f52f904'

decoded_cts = [ct.decode('hex') for ct in CTS]
MSGS = [['0'] * (len(s) / 2) for s in CTS]
s_key = ['0'] * 1024  # in char
accepted_char = string.ascii_letters + ' '


def xor_ith_ct_with_other_cts(i, cts):
    result = []
    for index, ct in enumerate(cts):
        if index != i:
            result.append((index, strxor(cts[i], ct)))
    return result


# Part 1: space hint
for ct_index, ct in enumerate(decoded_cts):
    ct_analysis = xor_ith_ct_with_other_cts(ct_index, decoded_cts)
    ct_analysis.append(('key', ct))
    min_length = min([len(x[1]) for x in ct_analysis])
    for i in range(min_length):
        ith_char = [(x[0], x[1][i]) for x in ct_analysis]
        letter_count = \
            [m[1] in string.ascii_letters for m in ith_char].count(True)
        if letter_count >= 5:
            print 'Good Start!'
            if len(set([m[1] for m in ith_char])) <= 1:
                print 'Ooops!!'
            else:
                MSGS[ct_index][i] = ' '
                for j, char in ith_char:
                    if j == 'key':
                        s_key[i] = strxor(char, ' ')
                    else:
                        MSGS[j][i] = strxor(char, ' ')

# Part 2: auto trial and tribulation
max_ct_length = max([len(x) for x in decoded_cts])
for i in range(max_ct_length):

    for msg_index, msg in enumerate(MSGS):
        print "FULL MSG {}: {}".format(msg_index, ''.join(msg))

    max_key = ''
    max_key_count = 0
    result = []

    # Running trial
    for key_in_int in range(256):
        key = chr(key_in_int)
        temp_result = []
        for ct_index, ct in enumerate(decoded_cts):
            if i < len(ct):
                temp_result.append((ct_index, strxor(ct[i], key)))
        accept_letter_count = \
            [m[1] in accepted_char for m in temp_result].count(True)

        if accept_letter_count > max_key_count:
            max_key = key
            max_key_count = accept_letter_count
            result = copy.deepcopy(temp_result)

    s_key[i] = max_key
    for msg_index, result_char in result:
        MSGS[msg_index][i] = result_char


# Part 3: Fix keys
while True:
    for msg_index, msg in enumerate(MSGS):
        print "FULL MSG {}: {}".format(msg_index, ''.join(msg))

    byte = raw_input("Which byte would you like to fix? Or (D)jump to decrypt target")
    while not byte.isdigit() and byte.upper() != 'D':
        if int(byte) > max_ct_length:
            print "Wrong number!"
        else:
            print "Not a number!"
        byte = raw_input("Which byte would you like to fix? Or (D)jump to decrypt target")

    if byte.upper() == 'D':
        break

    print "Current states for byte {}:".format(byte)
    byte_num = int(byte)

    for msg_index, msg in enumerate(MSGS):
        if byte_num < len(msg) + 2:
            print "PART MSG {}: {}".format(msg_index, msg[max(0, byte_num - 2):byte_num + 3])

    for msg_index, msg in enumerate(MSGS):
        print "FULL MSG {}: {}".format(msg_index, ''.join(msg))

    fix_option = raw_input(
        "(R)Run trial for byte {}/(B) Choose another byte/(S)show MSG, key: ".format(byte_num))
    fix_option = fix_option.upper()
    while fix_option not in ['R', 'B', 'D']:
        if fix_option == 'S':
            show_index = raw_input("Enter 0 ~ 9 to display current msg, or k to display current key: ")
            if show_index.lower() == 'k':
                print ''.join(s_key).encode('hex')
            elif show_index in '0123456789' and len(show_index) == 1:
                print ''.join(MSGS[int(show_index)])
            else:
                print "Wrong index!"
        else:
            print "Wrong option!"
        fix_option = raw_input(
            "(R)Run trial for byte {}/(B) Choose another byte/(S)show MSG, key: ".format(
                byte_num))
        fix_option = fix_option.upper()

    if fix_option == 'R':

        # Running trial
        for key_in_int in range(256):
            key = chr(key_in_int)
            key_in_hex = hex(key_in_int)
            temp_result = []
            for ct_index, ct in enumerate(decoded_cts):
                if byte_num < len(ct):
                    temp_result.append((ct_index, strxor(ct[byte_num], key)))
            accept_letter_count = \
                [m[1] in accepted_char for m in temp_result].count(True)

            if len(temp_result) > 2:
                threshhold = 0.7
            else:
                threshhold = 0.3

            if accept_letter_count >= len(temp_result) * threshhold:
                for msg_index, tmp_result in temp_result:
                    MSG = MSGS[msg_index]
                    if byte_num == 0:
                        part_tmp_MSG = [tmp_result, MSG[1], MSG[2]]
                    elif byte_num == 1:
                        part_tmp_MSG = [MSG[0], tmp_result, MSG[2], MSG[3]]
                    else:
                        part_tmp_MSG = MSG[byte_num - 2:byte_num] + [tmp_result] + MSG[byte_num + 1:byte_num + 3]
                    print "Temp MSG {}: {}".format(msg_index, part_tmp_MSG)

                key_correct = raw_input("Is key {} correct for byte {}?(Y)/(N)".format(key_in_hex, byte_num))
                key_correct = key_correct.upper()
                while key_correct not in ['Y', 'N']:
                    print "Wrong option!"
                    key_correct = raw_input("Is key {} correct for byte {}?(Y)/(N)".format(key_in_hex, byte_num))
                    key_correct = key_correct.upper()

                if key_correct == 'Y':
                    s_key[byte_num] = key
                    for msg_index, tmp_result in temp_result:
                        MSGS[msg_index][byte_num] = tmp_result
                    break
                elif key_correct == 'N':
                    continue

    elif fix_option == 'B':
        continue


# Part 4: Try decrypt target
combined_s_key = ''.join(s_key)
target_msg = strxor(target.decode('hex'), combined_s_key)
print target_msg

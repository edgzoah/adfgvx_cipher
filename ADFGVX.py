def getStr(str):
    t = []
    for i in str:
        if i not in t and i != ' ': t.append(i)
    return t

def ADFGVX_encrypt(text, key, column_key):
    text = 'sram'.upper()
    key = 'cinamorde'.upper()
    column_key = '51324'.upper()
    cos = 'ADFGVX'
    cos_len = len(cos)
    table = [[' ', 'A', 'D', 'F', 'G', 'V', 'X']]
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


    text = ''.join(getStr(text))
    column_key = ''.join(getStr(column_key))

    text_with_alp = text
    for i in alp:
        if i not in text:
            text_with_alp += i
    for i in range(cos_len):
        ok = cos[i] + text_with_alp[i*cos_len:(i+1)*cos_len]
        ok = [ok[j:j+1] for j in range(0, len(ok), 1)]
        if len(ok) < cos_len:
            ok += alp[len(ok):7]
            alp = alp[cos_len:]
        table.append(ok)

    step1 = ''

    for i in key:
        for j in range(7):
            for k in range(7):
                if table[j][k] == i and j != 0 and k != 0 and i != ' ':
                    step1 += cos[j-1] + cos[k-1]


    ciphered_table = []

    col_len = len(column_key)

    for i in range(len(step1)//col_len):
        ciphered_table.append(step1[i*col_len:(i+1)*col_len])

    if len(step1)%col_len != 0:
        ciphered_table.append(step1[-(len(step1)%col_len):])


    step2 = ''
    sorted_column_key = sorted(column_key)
    for i in range(col_len):
        for j in range(len(ciphered_table)):
            try:
                step2 += ciphered_table[j][column_key.index(sorted_column_key[i])]
            except IndexError:
                pass


    return step2


def ADFGVX_decrypt(msg, key, column_key):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    cos = 'ADFGVX'
    cos_len = len(cos)
    table = [[' ', 'A', 'D', 'F', 'G', 'V', 'X']]
    msg = msg.upper()
    key = ''.join(getStr(key.upper()))
    column_key = ''.join(getStr(column_key.upper()))

    column_len = len(msg)//len(column_key)
    columns = []
    for i in range(len(column_key)):
        columns.append(msg[i*column_len:(i+1)*column_len])
    
    new_columns = [[] for i in range(len(columns))]
    sorted_column_key = sorted(column_key)
    for i in range(len(columns)):
        new_columns[column_key.index(sorted_column_key[i])] = columns[i]

    step1 = ''
    for i in range(len(columns[0])):
        for j in range(len(columns)):
            step1 += columns[j][i]

    text_with_alp = msg
    for i in alp:
        if i not in msg:
            text_with_alp += i
    
    table = [[' ', 'A', 'D', 'F', 'G', 'V', 'X']]
    for i in range(cos_len):
        ok = cos[i] + text_with_alp[i*cos_len:(i+1)*cos_len]
        ok = [ok[j:j+1] for j in range(0, len(ok), 1)]
        if len(ok) < cos_len:
            ok += alp[len(ok):7]
            alp = alp[cos_len:]
        table.append(ok)
    decrypted_text = ''

    for i in range(len(step1)//2):
        decrypted_text += table[cos.index(step1[i*2])+1][cos.index(step1[i*2+1])+1]

    return decrypted_text.lower()
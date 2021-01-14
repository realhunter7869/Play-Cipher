CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))

import string

def encrypt(sent):
    
    for letter in string.punctuation:
        sent = sent.replace(letter, '')
        
    sent = sent.replace(" ", '')
    sent = sent.upper()
    sent = sent.replace("J", 'I')
    
    lst = []
    
    while len(sent) > 0:
        lst.append(sent[:2])
        sent = sent[2:]
        
    if len(lst[-1]) == 1:
        lst[-1] += 'X'
        
    for item in lst:
        if item[0] == item[1]:
            lst[lst.index(item)] = item[0] + 'X'
        
    en = ''
        
    for item in lst:
        for i in range(len(CIPHER)):
            for j in range(len(CIPHER[0])):
                if CIPHER[i][j] == item[0]:
                    it0 = (i, j)
                if CIPHER[i][j] == item[1]:
                    it1 = (i, j)
        #print(it0, it1)
        
        # Same
        # if it0[0] == it1[0] and it0[1] == it1[1]:
        #     en += CIPHER[it0[0]][it0[1]] + 'X'
        #     continue
        #print(en)
        # Row condition
        if it0[0] == it1[0]:
            try:
                en += CIPHER[it0[0]][it0[1] + 1] + CIPHER[it1[0]][it1[1] + 1]
            except:
                try:
                    en += CIPHER[it0[0]][0] + CIPHER[it1[0]][it1[1] + 1]
                except:
                    en += CIPHER[it0[0]][it0[1] + 1] + CIPHER[it1[0]][0]
            continue
        
        # Column condition
        elif it0[1] == it1[1]:
            try:
                en += CIPHER[it0[0] + 1][it0[1]] + CIPHER[it1[0] + 1][it1[1]]
            except:
                try:
                    en += CIPHER[0][it1[1]] + CIPHER[it1[0] + 1][it1[1]]
                except:
                    en += CIPHER[it0[0] + 1][it0[1]] + CIPHER[0][it1[1]]
            continue
        
        
        # Rectangular condition
        else:
            en += CIPHER[it0[0]][it1[1]] + CIPHER[it1[0]][it0[1]]
            
        #if it0[1] == it1[1]:
        #    en += CIPHER[it0[0]][it0[1]] + CIPHER[it0[0]][it0[1]]
    
    #print(en)
    #print(lst)
    return en
    
def decrypt(sent):
    lst = []
    
    while len(sent) > 0:
        lst.append(sent[:2])
        sent = sent[2:]
    
    en = ''
        
    for item in lst:
        for i in range(len(CIPHER)):
            for j in range(len(CIPHER[0])):
                if CIPHER[i][j] == item[0]:
                    it0 = (i, j)
                if CIPHER[i][j] == item[1]:
                    it1 = (i, j)
        #print(it0, it1)
        
        # Same
        # if it0[0] == it1[0] and it0[1] == it1[1]:
        #     en += CIPHER[it0[0]][it0[1]] + 'X'
        #     continue
        #print(en)
        
        # Row condition
        if it0[0] == it1[0]:
            try:
                en += CIPHER[it0[0]][it0[1] - 1] + CIPHER[it1[0]][it1[1] - 1]
            except:
                try:
                    en += CIPHER[it0[0]][4] + CIPHER[it1[0]][it1[1] - 1]
                except:
                    en += CIPHER[it0[0]][it0[1] - 1] + CIPHER[it1[0]][4]
            continue
        
        # Column condition
        elif it0[1] == it1[1]:
            try:
                en += CIPHER[it0[0] - 1][it0[1]] + CIPHER[it1[0] - 1][it1[1]]
            except:
                try:
                    en += CIPHER[4][it1[1]] + CIPHER[it1[0] - 1][it1[1]]
                except:
                    en += CIPHER[it0[0] - 1][it0[1]] + CIPHER[4][it1[1]]
            continue
        
        
        # Rectangular condition
        else:
            en += CIPHER[it0[0]][it1[1]] + CIPHER[it1[0]][it0[1]]
            
        #if it0[1] == it1[1]:
        #    en += CIPHER[it0[0]][it0[1]] + CIPHER[it0[0]][it0[1]]
    
    #print(en)
    #print(lst)
    return en

print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))

import sys
input = sys.stdin.readline

need = ['a', 'e', 'i', 'o', 'u']

def check(password):
    has_vowel = False
    for v in need:
        if v in password:
            has_vowel = True
            break
    if not has_vowel:
        return False

    vowel_count = 0
    consonant_count = 0

    for ch in password:
        if ch in need:
            vowel_count+=1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        if vowel_count == 3 or consonant_count == 3:
            return False

    for i in range(1,len(password)):
        if password[i] == password[i-1]:
            if password[i] != 'e' and password[i] != 'o':
                return False

    return True


while True:
    password = input().strip()
    if password == "end":
        break
    if check(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")


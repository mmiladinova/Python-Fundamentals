import re

n = int(input())

for _ in range(n):
    message = input()

    pattern = r'^([\$\%])[A-Z][a-z]{2,}\1: (\[\d+\]\|){3}$'
    result = re.match(pattern, message)

    if result is None:
        print(f"Valid message not found!")
    else:
        msg = result[0]
        text_pattern = r'[a-zA-Z]{3,}'
        res_text = re.findall(text_pattern, msg)
        text = res_text[0]

        regex_pattern = r'[0-9]+'
        res_num = re.findall(regex_pattern, msg)
        a = int(res_num[0])
        b = int(res_num[1])
        c = int(res_num[2])
        decrypted = chr(a) + chr(b) + chr(c)

        final_text = f'{text}: {decrypted}'
        print(final_text)

path = input().split('\\')
file_name = ''

for i in path:
    if '.' in i:
        file_name = i

file, extension = file_name.split('.')

print(f'File name: {file}')
print(f'File extension: {extension}')

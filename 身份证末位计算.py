param = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
last_character = ['1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2', '1']
n, index = 0, 0

while n < 17:
    ipt = input('enter a number:')
    index += int(ipt) * param[n]
    n += 1

index %= 11

print('The last:', last_character[index])

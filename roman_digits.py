number = temp_num = int(input('Type a number: '))

rom_num = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


if __name__ == '__main__':
    def convertToRoman(number):
        result = []
        for x in range(len(num)):
            while number >= num[x]:
                    result.append(rom_num[x])
                    number -= num[x]
        x += 1
        return result
    
    for y in convertToRoman(number):
        print(y, end='')

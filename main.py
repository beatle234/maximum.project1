#есть строка aabbccdd. нужно посчитать количество каждой из букв
#множество - список уникальных значений(ффвв - фв)

#def strconter(s):
#    for symbol in set(s): #отвечает за перебор искомых значений
#        counter = 0
#        for sub_symbol in s: #отвечает за подсчет количества искомого символа в строке
#            if sub_symbol == symbol:
#                counter += 1
#        print(symbol, counter)

#strconter('aabcd')

#или

# def strconter(s):
#     syms_counter = {}
#     for symbol in s:
#         syms_counter[symbol] = syms_counter.get(symbol, 0) +1
#
#     for symbol, count in syms_counter.items():
#         print(symbol, count)
#
# strconter('hello world')

def checkPalindrome(n):
    centr = len(n)//2
    for i in range(centr):
        if n(i)!=n[len(n)-i]:
            return False
    return True

print(checkPalindrome('лепсспел'))



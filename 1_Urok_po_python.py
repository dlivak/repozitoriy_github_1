import requests
import flask


print('Задачи на циклы и оператор условия')

# -------------------------------------------------------------------------------------
print('Задача 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована')
for i in range(1,6):
	print(str(i), "0" *i, sep = ') ')



# -------------------------------------------------------------------------------------   
print('Задача 2. Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.')


number_1 = int (input('Введите первую (любую) цифру из 10: '))
while number_1 >9:
	number_1 = int (input('Неверно. Введите первую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_2 = int (input('Введите вторую (любую) цифру из 10: '))
while number_2 >9:
	number_2 = int (input('Неверно. Введите вторую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_3 = int(input('Введите третью (любую) цифру из 10: '))
while number_3 > 9:
	number_3 = int(input('Неверно. Введите третью цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_4 = int(input('Введите четвертую (любую) цифру из 10: '))
while number_4 > 9:
	number_4 = int(input('Неверно. Введите четвертую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_5 = int(input('Введите пятую (любую) цифру из 10: '))
while number_5 > 9:
	number_5 = int(input('Неверно. Введите пятую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_6 = int(input('Введите шестую (любую) цифру из 10: '))
while number_6 > 9:
	number_6 = int(input('Неверно. Введите шестую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_7 = int(input('Введите седьмую (любую) цифру из 10: '))
while number_7 > 9:
	number_7 = int(input('Неверно. Введите седьмую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_8 = int(input('Введите восьмую (любую) цифру из 10: '))
while number_8 > 9:
	number_8 = int(input('Неверно. Введите восьмую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_9 = int(input('Введите девятую (любую) цифру из 10: '))
while number_9 > 9:
	number_9 = int(input('Неверно. Введите девятую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

number_10 = int(input('Введите десятую (любую) цифру из 10: '))
while number_10 > 9:
	number_10 = int(input('Неверно. Введите десятую цифру из 10. Это должна быть любая цыфра от 0 до 9: '))

result1 = (number_1*10) + number_2
result2 = (result1 * 10) + number_3
result3 = (result2 * 10) + number_4
result4 = (result3 * 10) + number_5
result5 = (result4 * 10) + number_6
result6 = (result5 * 10) + number_7
result7 = (result6 * 10) + number_8
result8 = (result7 * 10) + number_9
x = (result8 * 10) + number_10

ishchem = 5

qqqq =0
wwww =0
eeee =0
rrrr =0
tttt =0
yyyy =0
uuuu =0
iiii =0
oooo =0
pppp =0

if number_1 == ishchem:
	qqqq = 1
if number_2 == ishchem:
	wwww = 1
if number_3 == ishchem:
	eeee = 1
if number_4 == ishchem:
	rrrr = 1
if number_5 == ishchem:
	tttt = 1
if number_6 == ishchem:
	yyyy = 1
if number_7 == ishchem:
	uuuu = 1
if number_8 == ishchem:
	iiii = 1
if number_9 == ishchem:
	oooo = 1
if number_10 == ishchem:
	pppp = 1
print(('Значит ищем в этом числе:'), (x), ('количество цифр:'), (ishchem))
#print (qqqq, wwww, eeee, rrrr, tttt, yyyy, uuuu, iiii, oooo, pppp)

opa = qqqq + wwww + eeee + rrrr + tttt + yyyy + uuuu + iiii + oooo + pppp
                                                                    
print(('В даном числе нашлось'), (opa), ('таких цыфр(ы).'))

#rezultat = qqqq+wwww+eeee+rrrr+tttt+yyyy+uuuu+iiii+oooo+pppp
#print(rezultat)


# -------------------------------------------------------------------------------------   
print('Задача 3. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')

sum = 0

for i in range(1,101):
     sum+=i
print(('Ответ: сумма ряда чисел от 1 до 100 равна '), sum)



# -------------------------------------------------------------------------------------   

print('Задача 4. Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')


i = 1*2*3*4*5*6*7*8*9*10
print(('Ответ. Произведение чисел от 1до 10 равно: '), (i))




# -------------------------------------------------------------------------------------   
print('Задача 5  Вывести цифры числа на каждой строчке. ') 



www = int (input('Введите число: '))

# print(www %10, www//10)

while www>0:
	print(www%10)
	www = www//10


 

# -------------------------------------------------------------------------------------   
print('Задача 6 Найти сумму цифр числа.')

a = int(input('Введите любое число (максимум десятизначное) в котором хотите найти сумму цифр: '))

ostatok1 = a//10
zifra1 = a%10
#print(ostatok1, zifra1)

zifra2 = ostatok1%10
ostatok2 = ostatok1//10
#print(ostatok2, zifra2)

zifra3 = ostatok2%10
ostatok3 = ostatok2//10
#print(ostatok3, zifra3)

zifra4 = ostatok3%10
ostatok4 = ostatok3//10
#print(ostatok4, zifra4)

zifra5 = ostatok4%10
ostatok5 = ostatok4//10
#print(ostatok5, zifra5)

zifra6 = ostatok5%10
ostatok6 = ostatok5//10
#print(ostatok6, zifra6)

zifra7 = ostatok6%10
ostatok7 = ostatok6//10
#print(ostatok7, zifra7)

zifra8 = ostatok7%10
ostatok8 = ostatok7//10
#print(ostatok8, zifra8)

zifra9 = ostatok8%10
ostatok9 = ostatok8//10
#print(ostatok9, zifra9)

zifra10 = ostatok9%10     
ostatok10 = ostatok9//10
#print(ostatok10, zifra10)

x = zifra1 + zifra2 + zifra3 + zifra4 + zifra5 + zifra6 + zifra7 + zifra8 + zifra9 + zifra10

print(('Ответ: Сумма цыфр числа '), a, ('равна'), x, end='.')



# -------------------------------------------------------------------------------------




print('Задача 7 Найти производное цифр числа.')

n = int(input('Введите любое число в котором хотите найти производное цифр: '))

mult = 1
summa = 0
while n > 0:
	if n%10 != 0:
		mult = mult * (n%10)
	summa = summa + n%10
	n = n // 10

print("Сумма цифр:", summa)
print("Произведение значащих цифр:", mult)




#-------------------------------------------------------------------------------------
print('Задача 8 Дать ответ на вопрос: есть ли среди цифр числа 5?')
integer_number = int(input('Введите любое число в котором хотите узнать, есть ли в нем цыфра 5: '))

while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')


# -------------------------------------------------------------------------------------
print ('Задача 9. Найти максимальную цифру в числе')

n = int(input('Введите двузначное число, в котором хотите найти максимальную цифру: '))
mx = n % 10
n //= 10
while n > 0:
 	if n % 10 > mx:
 		mx = n % 10
 	n //= 10
 	print (mx)


# -----------------------------------------------------------------------------------
print ('Задача 10. Найти количество цифр 5 в числе')

zz1=0
zz2=0
zz3=0
zz4=0
zz5=0
zz6=0
zz7=0
zz8=0
zz9=0
zz10=0

a = int(input('Введите любое число (!Но не более десятизначного), в котором хотите узнать, количество цифр 5: '))
ostatok1 = a//10
zifra1 = a%10
#print(ostatok1, zifra1)
if zifra1==5:
	zz1=1
#print(zz)

zifra2 = ostatok1%10
ostatok2 = ostatok1//10
#print(ostatok2, zifra2)
if zifra2==5:
	zz2=1

zifra3 = ostatok2%10
ostatok3 = ostatok2//10
#print(ostatok3, zifra3)
if zifra3==5:
	zz3=1

zifra4 = ostatok3%10
ostatok4 = ostatok3//10
#print(ostatok4, zifra4)
if zifra4==5:
	zz4=1

zifra5 = ostatok4%10
ostatok5 = ostatok4//10
#print(ostatok5, zifra5)
if zifra5==5:
	zz5=1

zifra6 = ostatok5%10
ostatok6 = ostatok5//10
#print(ostatok6, zifra6)
if zifra6==5:
	zz6=1

zifra7 = ostatok6%10
ostatok7 = ostatok6//10
#print(ostatok7, zifra7)
if zifra7==5:
	zz7=1

zifra8 = ostatok7%10
ostatok8 = ostatok7//10
#print(ostatok8, zifra8)
if zifra8==5:
	zz8=1

zifra9 = ostatok8%10
ostatok9 = ostatok8//10
#print(ostatok9, zifra9)
if zifra9==5:
	zz9=1

zifra10 = ostatok8%11
ostatok10 = ostatok8//11
#print(ostatok9, zifra9)
if zifra10==5:
	zz10=1

rrr = zz1+zz2+zz3+zz4+zz5+zz6+zz7+zz8+zz9+zz10
print(('Ответ: В числе'), a, ('найдено'), rrr, ('цыфр (ы) 5.'))
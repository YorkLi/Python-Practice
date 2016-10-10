def function1():
	first_number = int(input("請輸入第一個數字:"))
	second_number = int(input("請輸入第二個數字:"))
	operation_number = input("請輸入運算符號:")

	while True :
		if operation_number == "+":
			answer = first_number + second_number
			break
		elif operation_number == "-":
			answer = first_number - second_number
			break
		elif operation_number == "*":
			answer = first_number * second_number
			break
		elif operation_number == "/":
			answer = first_number / second_number
			break
		else:
			print("請輸入正確的運算符號")
			operation_number = input("請輸入運算符號:")
	print("你輸入的是 : "+str(first_number)+" , "+str(second_number)+" ,運算符號為"+operation_number)
	print("答案為"+str(answer))

def function2():
	number = int(input("請輸入一個數字:"))
	answer=1
	for i in range(number,0,-1):
		answer = answer * i
	print("答案為"+str(answer))


def main():
	while True :
		select=int(input("請選擇一個功能 : (1)輸入二個整數四則運算的運算器 (2)輸入一個整數值,並計算它的階層乘積 (3)離開 "))
		print("你選擇的是 : ["+str(select)+"]")
		
		
		if select == 1 :
			function1()
		elif select == 2 :
			function2()
		elif select == 3 :
			print("Bye~")
			break
		else:
			print("請輸入正確數字!")

main()

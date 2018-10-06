password = 'a123456'
i = 3
while True:
	pWord = input('請輸入密碼: ')
	if pWord == 'a123456':
		print('登入成功!') 
		break
	else:
		i -= 1
		if i == 0:
			break
		print('密碼錯誤! 還有', i, '次機會')
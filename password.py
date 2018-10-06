password = 'a123456'
i = 3
while i > 0:
	i -= 1
	pWord = input('請輸入密碼: ')
	if pWord == 'a123456':
		print('登入成功!') 
		break
	else:
		
		if i > 0:			
			print('密碼錯誤! 還有', i, '次機會')
		else:
			print('密碼錯誤! 沒機會嘗試了! 要鎖帳號了啦!')
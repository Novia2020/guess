import random
start = input('你想要的起始值是: ')
end = input('你想要的結束值是: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1 # count += 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		print('你猜了第', count, '次')
		break
	elif num > r:
		print('你的答案比較大')
	elif num < r:
		print('你的答案比較小')
	print('你猜了第', count, '次')


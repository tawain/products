# 二維清單 2dimensional
products = []
while True:
	name = input('輸入商品名稱：')
	if name == 'q':
		break
	price = input('輸入商品價格：')
	products.append([name, price])
print(products)

for p in products:
	print(p)
	print(p[0])
	print(p[0], '的價格是', p[1])

# 字串可做加法、乘法
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w') as f: # r(read)讀取模式/w(write)寫入模式
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # ,做區隔；\n換行符號
		#f寫入str + str + str + str
# open一定要有close，with是python自動close的功能。




	


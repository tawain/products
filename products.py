# 二維清單 2dimensional
products = []
while True:
	name = input('輸入商品名稱：')
	if name == 'q':
		break
	price = input('輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

products[0][0] # 大清單的第0位、小清單的第0位


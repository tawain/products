import random
import os # 載入operating system/作業系統

def read_file(filename):
	products = []
		# 讀取檔案
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # continue和break一樣，只能寫在迴圈裡。
			# continue就是跳到下一迴圈的意思。
			# 跳過continue之後的迴圈裡面的程式碼，從頭開始一次新迴圈。
			name, price = line.strip().split(',') 
		# strip除掉，除掉換行符號/n。
		# split切割，字串line一遇到'，'就切割。
		# split切割完的結果是清單。
			products.append([name, price])
	return products

# 讓使用者輸入
# 二維清單 2dimensional
def user_input(products):
	while True:
		name = input('輸入商品名稱：')
		if name == 'q':
			break
		price = input('輸入商品價格：') # price還是字串、下一行轉成整數int
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# 印出商品價格
def print_products(products):
	for p in products:
		print(p)
		print(p[0])
		print(p[0], '的價格是', p[1])

# 字串可做加法、乘法
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: # r(read)讀取模式/w(write)寫入模式
		f.write('商品,價格\n') 
		# 寫入和讀取都牽扯到編碼(encoding)。所以加入encoding='utf-8'。
		# 沒有這行也沒變亂碼。可能因為不是用excel開csv，所以沒亂碼的問題。詳見講座64
		for p in products:
			f.write(str(p[0]) + ',' + str(p[1]) + '\n') # ,做區隔；\n換行符號
			#f寫入str + str + str + str
	# open一定要有close，with是python自動close的功能。
	# +-法只能字串＋字串或整數＋整數、所以要再把整數int轉換成字串str

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):# 確認檔案存在與否
		print('找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

# refactor 重構


import os # operating system(作業系統模組)

#讀取檔案
products= []
if os.path.isfile('products.csv'): #os.path.isfile()檢查檔案在不在
	print('yes')
	with open('products.csv', 'r') as f :
		for line in f:
			if '商品, 價格' in line:
				continue
			name, price =line.strip().split(',') #用.split(',')做分隔 = , .strip()除換行符號=(\n)
			products.append([name, price])
	print(products)

else:
	print('no')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input('請輸入商品價格: ')
	p = [] #p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f: #encoding = 'utf-8'解決亂碼問題
	f.write('商品, 價格\n') #加入程式碼寫欄位
	for p in products:
		f.write(p[0]+ ',' + p[1] + '\n')
from openpyxl import Workbook


wb = Workbook()
wb['Sheet'].title = 'One rusult'
sh1 = wb.active


file_csv = 'result/results_product_urlEndFileTwo.csv'
with open(file_csv,'r',encoding='utf-8') as f:
	lines = f.readlines()
	quantity_lines = len(lines)
	for i in range(quantity_lines):
		list_result = lines[i].split(' | ')
		sh1[f'A{i+1}'] = list_result[0]
		sh1[f'B{i+1}'] = list_result[1]
		sh1[f'C{i+1}'] = list_result[2]
		sh1[f'D{i+1}'] = list_result[3]
		sh1[f'E{i+1}'] = list_result[4]
		sh1[f'F{i+1}'] = list_result[5]
		sh1[f'G{i+1}'] = list_result[6]
		sh1[f'H{i+1}'] = list_result[7]
		sh1[f'I{i+1}'] = list_result[8]


	wb.save('resultThree.xlsx')
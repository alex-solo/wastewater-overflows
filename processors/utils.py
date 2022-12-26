import re

def extract_val_from_volume(string):
	number_arr = re.findall(r'\d+\.\d+', string)
	if number_arr:
		num = number_arr[0]
		if 'thousand litres' in string:
			return str(float(num) / 1000)
		elif 'million litres' in string:
			return num
	else:
		return ''

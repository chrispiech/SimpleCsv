from simplecsv import SimpleCsv

def main():
	main_csv = SimpleCsv('example_data/test.csv')
	other_csv = SimpleCsv('example_data/other.csv')

	merged_csv = merge(main_csv, other_csv)
	print(merged_csv)

def merge(a_csv, b_csv):
	a_dict = a_csv.to_dict('Name')
	b_dict = b_csv.to_dict('Name')
	merged = SimpleCsv()
	merged.set_col_names(merge_column_names(a_csv, b_csv))
	for key in a_dict:
		datum_a = a_dict[key]
		if key in b_dict:
			datum_b = b_dict[key]
			# this is python fancy way to merge dictionaries
			# ** is called the "unpacking" operator
			merged_datum = {**datum_a, **datum_b}
			merged.add_row(merged_datum)
		else:
			merged.add_row(datum_a)
	return merged

def merge_column_names(a_csv, b_csv):
	"""
	I generally don't want repeated column names
	"""
	new_cols = a_csv.get_col_names()
	for new_col in b_csv.get_col_names():
		if new_col != 'Name':
			new_cols.append(new_col)
	return new_cols


if __name__ == '__main__':
	main()
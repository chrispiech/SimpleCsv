
import csv
import copy

"""
This is a very useful class for Chris, and others who might
work with CSV data often. The key data structure to know about
is that each row is naturally stored as a dictionary where
column names are keys as opposed to a list.

Here are the assumptions made:
  If a row has missing elements, fill in with ''
  If a row has extra elements, ignore them
  All value types are strings!

  If you get a datum, you may modify it but the csv cols will
     not be impacted

"""

MISSING_VALUE = ''

class SimpleCsv:

	def __init__(self, file_name = None, has_header = True):
		if not file_name:
			self.col_names = []
			self.rows = []
			return

		reader = csv.reader(open(file_name))
		first_line = next(reader)
		self.rows = []

		if has_header:
			self.col_names = first_line
		else:
			n = len(first_line)
			# ['col 1', 'col 2', 'col 3' ... ]
			self.col_names = ['col ' + str(i) for i in range(n)]
			# we still need to process the first row
			datum = self._make_datum(first_line)
			self.rows.append(datum)
		for row in reader:
			datum = self._make_datum(row)
			self.rows.append(datum)

	def __str__(self):
		result_str = ''
		result_str += self._header_str() + '\n'
		for row in self.rows:
			result_str += self._row_str(row) + '\n'
		return result_str.rstrip()

	def __iter__(self):
		self._iter_index = 0
		return self

	def __next__(self):
		if self._iter_index >= len(self.rows):
			raise StopIteration
		next_row = self.rows[self._iter_index]
		self._iter_index += 1
		return next_row

	def __len__(self):
		return len(self.rows)

	################################################
	#                Candidates!                   #
	################################################

	def save(self, file_path):
		writer = csv.writer(open(file_path, 'w'))
		writer.writerow(self.col_names)
		for datum in self.rows:
			out_row = self._row_list(datum)
			writer.writerow(out_row)

	def to_dict(self, key_col_name):
		result = {}
		for datum in self:
			key = datum[key_col_name]
			result[key] = datum
		return result

	def get_col_names(self):
		return copy.deepcopy(self.col_names)

	def set_col_names(self, col_names):
		self.col_names = col_names

	def add_col_name(self, new_name):
		self.col_names.append(new_name)

	def add_row(self, row_dictionary):
		self.rows.append(row_dictionary)

	################################################
    #                Helpers                       #
	################################################

	def _make_datum(self, row_list):
		datum = {}
		for i in range(len(self.col_names)):
			col_name = self.col_names[i]
			value = MISSING_VALUE
			if i < len(row_list):
				value = row_list[i]
			datum[col_name] = value
		return datum

	def _row_list(self, datum):
		result_list = []
		for col_name in self.col_names:
			value = MISSING_VALUE
			if col_name in datum:
				value = datum[col_name]
			result_list.append(value)
		return result_list

	def _row_str(self, datum):
		result_str = ''
		for col_name in self.col_names:
			value = MISSING_VALUE
			if col_name in datum:
				value = datum[col_name]
			result_str += value + '\t'
		return result_str.rstrip()

	def _header_str(self):
		result_str = ''
		for value in self.col_names:
			result_str += value + '\t'
		return result_str.rstrip()
def is_line_valid(line):
	bracket_cntr = 0
	for b in line:
		if b == '(':
			bracket_cntr += 1
		else:
			bracket_cntr -= 1
		if bracket_cntr < 0:
			return False
	return bracket_cntr == 0

print('YES' if is_line_valid(input()) else 'NO')

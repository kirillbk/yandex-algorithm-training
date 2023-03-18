# 15. Поврежденный XML

from string import ascii_lowercase
from re import fullmatch


def is_xml_valid(xml: str) -> bool:
	if fullmatch(r'(<\/*[a-z]+>)+', xml) is None:
		return False

	tags = list()
	l = r = 1

	while l < len(xml) and r < len(xml):
		while xml[r] != '>':
			r += 1
		tags.append(xml[l:r])
		l = r + 2
		r += 3

	stack = list()

	for tag in tags:
		if tag.startswith('/'):
			if not stack or stack[-1] != tag[1:]:
				return False
			stack.pop()
		else:
			stack.append(tag)

	if stack:
		return False
	return True


def solution(xml: str) -> str:
	for i in range(len(xml)):
		for char in ascii_lowercase + '<>/':
			modified_xml = xml[:i] + char + xml[i+1:]
			if is_xml_valid(modified_xml):
				return modified_xml

	return ''


print(solution(input()))

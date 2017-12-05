def reverse(string):
	if string == "":
		return string
	return reverse(string[1:]) + string[0]

reverseString = reverse("abcd")
print(reverseString)
string = "a"
print(string[5])
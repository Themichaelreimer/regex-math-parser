import re

binary_operators = [r'\^', r'\*', r'\/', r'\+', r'\-']

digit_pattern = r'\-?\d+'
operator_pattern = r'[{}]'.format(''.join(r'{}'.format(op) for op in binary_operators))  # When I print this the chars look double escaped
operation_pattern = r'({0})({1})({0})'.format(digit_pattern,operator_pattern)
bracket_pattern = r'(\({}\))'.format(operation_pattern)

binary_patterns = [r'({0})({1})({0})'.format(digit_pattern,op) for op in binary_operators]
patterns = [bracket_pattern, *binary_patterns] # Each pattern in this list is in BEDMAS and in BEDMAS order

def eval(input:str) -> int:
	for pattern_index, pattern in enumerate(patterns):
		operator = binary_operators[pattern_index-1] if pattern_index>0 else None
		# Hacky do while loop
		while(True):

			search = re.search(pattern, input)
			if not search:
				break
			# Operator is none if the operation is brackets
			if not operator:
				partial_result = brackets(search.group(0))
			elif operator == r'\^':
				partial_result = exp(search.group(1),search.group(3))
			elif operator == r'\*':
				partial_result = mul(search.group(1),search.group(3))
			elif operator == r'\/':
				partial_result = div(search.group(1),search.group(3))
			elif operator == r'\+':
				partial_result = add(search.group(1),search.group(3))
			elif operator == r'\-':
				partial_result = sub(search.group(1),search.group(3))
			else:
				break
			import re

binary_operators = [r'\^', r'\*', r'\/', r'\+', r'\-']

digit_pattern = r'\-?\d+'
operator_pattern = r'[{}]'.format(''.join(r'{}'.format(op) for op in binary_operators))  # When I print this the chars look double escaped
operation_pattern = r'({0})({1})({0})'.format(digit_pattern,operator_pattern)
bracket_pattern = r'(\({}\))'.format(operation_pattern)

binary_patterns = [r'({0})({1})({0})'.format(digit_pattern,op) for op in binary_operators]
patterns = [bracket_pattern, *binary_patterns] # Each pattern in this list is in BEDMAS and in BEDMAS order

def eval(input:str) -> int:
        for pattern_index, pattern in enumerate(patterns):
                operator = binary_operators[pattern_index-1] if pattern_index>0 else None
                # Hacky do while loop
                while(True):

                        search = re.search(pattern, input)
                        if not search:
                                break
                        # Operator is none if the operation is brackets
                        if not operator:
                                partial_result = brackets(search.group(0))
                        elif operator == r'\^':
                                partial_result = exp(search.group(1),search.group(3))
                        elif operator == r'\*':
                                partial_result = mul(search.group(1),search.group(3))
                        elif operator == r'\/':
                                partial_result = div(search.group(1),search.group(3))
                        elif operator == r'\+':
                                partial_result = add(search.group(1),search.group(3))
                        elif operator == r'\-':
                                partial_result = sub(search.group(1),search.group(3))
                        else:
                                break

                        start,end = search.span()
                        input = input[:start] + str(partial_result) + input[end:]
                        print(input)

        result = re.search(digit_pattern,input)
        if result:
                return int(result.group(0))

def brackets(input:str) -> int:
        return eval(input[1:-1])

def exp(a:str,b:str) -> int:
        return int(a)**int(b)

def mul(a:str, b:str) -> int:
        return int(a)*int(b)

def div(a:str, b:str) -> int:
        return int(a)/int(b)
			start,end = search.span()
			input = input[:start] + str(partial_result) + input[end:]
			print(input)

	result = re.search(digit_pattern,input)
	if result:
		return int(result.group(0))
			
def brackets(input:str) -> int:
	return eval(input[1:-1])
	
def exp(a:str,b:str) -> int:
	return int(a)**int(b)

def mul(a:str, b:str) -> int:
	return int(a)*int(b)

def div(a:str, b:str) -> int:
        return int(a)/int(b)

def add(a:str, b:str) -> int:
        return int(a)+int(b)

def sub(a:str, b:str) -> int:
        return int(a)-int(b)

eval("1+(2*3)")

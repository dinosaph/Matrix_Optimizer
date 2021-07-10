
# A given SOLID_A matrix
SOLID_A = [
[
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1] 
],
[
	[ 1, 1, 1, 1, 1],
	[ 0, 1, 1, 1, 1],
	[ 0, 1, 1, 1, 1],
	[ 0, 1, 1, 1, 1],
	[ 0, 1, 1, 1, 1] 
],
[
	[ 1, 1, 1, 1, 1],
	[ 0, 1, 1, 1, 1],
	[ 0, 0, 1, 1, 1],
	[ 0, 0, 1, 1, 1],
	[ 0, 0, 1, 1, 1] 
],
[
	[ 1, 1, 1, 1, 1],
	[ 0, 1, 1, 1, 1],
	[ 0, 0, 1, 1, 1],
	[ 0, 0, 0, 1, 1],
	[ 0, 0, 0, 1, 1] 
]]

# A given SOLID_B matrix
SOLID_B = [
[
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1] 
],
[
	[ 1, 1, 1, 0, 0],
	[ 0, 1, 1, 0, 0],
	[ 0, 0, 1, 0, 0],
	[ 0, 0, 0, 1, 1],
	[ 1, 0, 0, 0, 1] 
],
[
	[ 1, 0, 0, 0, 0],
	[ 0, 1, 0, 0, 0],
	[ 0, 0, 1, 0, 0],
	[ 0, 0, 0, 1, 1],
	[ 1, 0, 0, 0, 1] 
],
[
	[ 1, 0, 0, 0, 0],
	[ 0, 1, 0, 0, 0],
	[ 0, 0, 1, 0, 0],
	[ 0, 0, 0, 1, 1],
	[ 1, 0, 0, 0, 1] 
]]

# Main running section
added = 0
excess = 0
if (__name__ == "__main__"):
	# Parsing layer by layer
	for b_layer in range(len(SOLID_B)):
		# Parsing line by line
		for b_line in range(len(SOLID_B[b_layer])):
			# Parsing element by element
			for b in range(len(SOLID_B[b_layer][b_line])):
				#print(b_layer, b_line, b)
				aa = SOLID_A[b_layer][b_line][b]
				bb = SOLID_B[b_layer][b_line][b]
				# if elements are different, SOLID_B element gets changed as needed
				if (aa != bb):
					if (aa == 0):
						excess += 1
						SOLID_B[b_layer][b_line][b] = 0
					elif (aa == 1):
						added += 1
						SOLID_B[b_layer][b_line][b] = 1
	print("* Added blocks:", added)
	print("* Excess blocks:", excess)
	final_change = added - excess
	print("* Optimization - minimum blocks to add:", final_change)
	

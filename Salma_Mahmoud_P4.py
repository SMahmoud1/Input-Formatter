#------------------------------------------------------------------------------
#Student Name: Salma Mahmoud/ Assignment: Project 4/ Date: 11/05/2012
#------------------------------------------------------------------------------
#Honor Code Statement: I received no assistance on this assignment that 
#violates the ethical guidelines set forth by professor and class syllabus.
#------------------------------------------------------------------------------
#References: Class Powerpoints, Textbook
#------------------------------------------------------------------------------
#Comments: N/A
#------------------------------------------------------------------------------
#Pseudocode: 
#BEGIN
#	print "1 - Format Table"
#	print "2 - Word Wrap"
#	print "3 - Receipt Maker"
#	option = integer input "Enter an option"
#	choose = true
#	while choose is true
#		if option input = 1
#			rows=integer input "How many rows? "
#			columns= integer input "How many columns? "
#			data = []
#			row2 = []
#			for x in the range of rows
#				for i in range of columns
#					row append input "Input data"
#				data append row
#				row = []
#			data_length = []
#			for i in range length data[0]
#				'length' = length data [0][i]
#				for j in range length data
#					if length data [j][i] less than 'length'
#						'length' = length data[j][i]
#				data_length append integer length
#			align = []
#			for x in range of columns
#				print "L - Left"
#				print "R - Right"
#				print "C - Centered"
#				alignemt=input "What alignment do you want?"
#				align append alignment
#				if align="L"
#					print format x to the right
#				elif align="R"
#					print format x to the right
#				elif align="C"
#					print format x to the right
#				else
#					print "Invalid input. Try again!"
#					alignment = input "What alignment so you want?"
#			print()
#			print "L - Left"
#			print "R - Right"
#			print "C - Centered"
#			align= input "Which alignment would you like? "
#
#		elif option input = 2
#			width= integer input "How wide should the output be? "
#			text_input = ""
#			while length 'text' not= 0
#				text_input=text_input + (" " + text)
#				text=input "Write new text. "
#			text_list=text_input split(" ")
#			print(text_list)
#			for x in text
#				if text_list = width
#					print
#
#		elif option input = 3
#			item_name=[]
#			price=[]
#			items=integer input "How many items will there be? "
#			for x in range 'items'
#				item_name append input "Item name: "
#				price append input "Price: "
#			for x in range length 'item_name'
#				length2 =3- - length 'item_name[x]'
#				print string item_name[x] + {:.>{l}} format('%.2f% price[x],l=length2
#		else:
#			print "Invalid input. Please try again."
#			option=integer input "Enter an option. "
#END
#------------------------------------------------------------------------------

print("1 - Format Table")
print("2 - Word Wrap")
print("3 - Receipt Maker")
option=int(input("Enter an option. "))
choose=True
while choose:
	if option==1:
		row=int(input("How many rows do you want? "))
		columns=int(input("How many columns would you like? "))
		data=[]
		row2=[]
		for x in range(row):
			for i in range(columns):
				row2.append(input("Input data "))
			data.append(row2)
			row2=[]
		data_length = []
		for i in range(len(data[0])):
			length = len(data[0][i])
			for j in range(len(data)):
				if len(data[j][i]) > length:
					length = len(data[j][i])
			data_length.append(int(length)) 
		align=[]
		for x in range(columns):				
			print("L - Left")
			print("R - Right")
			print("C - Center")
			alignment=input("What alignment do you want? ")
			align.append(alignment)
		for i in range(columns):
			for j in range(columns):
				if align[j]=="L" or "l": 
					print("{:<{x}}".format(data[i][j],x=data_length[j]), end="\t")
				elif align[j]=="R" or "r":
					print("{:>{x}}".format(data[i][j],x=data_length[j]), end="\t")
				elif align[j]=="C" or "c":
					print("{:^{x}}".format(data[i][j],x=data_length[j]), end="\t")
				else:
					print("Invalid input. Try again! ")
					alignment=raw_input("What alignment do you want?")
			print()
	elif option==2:
		width=int(input("How wide should the output be? "))
		text_input=""
		text=raw_input("Input your text. ")
		while len(text)!=0:
			text_input+=" "+text
			text=raw_input("Write new text. ")
		text_list=text_input.split(" ")
		print(text_list)
		for x in text:
			if text_list=width
				print("|{:>30}|".format(text_list, x=width), end="|")
	elif option==3:
		item_name=[]
		price=[]
		items= int(input("How many items will there be? "))
		for x in range(items):
			item_name.append(raw_input("Item name: "))
			price.append(float(input("Price: ")))
		for x in range(len(item_name)):
				length2= 30-len(item_name[x])
				print(str(item_name[x])+"{:.>{l}}".format("%.2f"%(price[x]), l = length2))
		print("-------------------------------")
		total=sum(price)
		print("Total."+"{:.>{l}}".format("%.2f"%(total), l = length2))
	else:
		print("Invalid input. Please try again.")
		option=int(input("Enter an option. "))

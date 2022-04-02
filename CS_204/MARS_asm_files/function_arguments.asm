.data 
	message: .asciiz "hey"
.text 
	main:	
		# store 50 in arg register $a1, 100 in $a1
		addi $a1, $zero, 50 
		addi $a2, $zero, 100
		
		jal addNumbers
		jal printInt
		
		b exit 
		
	addNumbers:	
		# add args 1 and 2, store sum in $v1, $v1 is for return values 
		add $v1, $a1, $a2 
		jr $ra 
		
	printInt:
		# li print_int sys command
		li $v0, 1 
		# load $v1 into arg address 0, add zero
		addi $a0, $v1, 0
		syscall
		
		jr $ra
	
	exit:
		li $v0, 10 
		syscall
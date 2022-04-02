# while loop with arrays
# while loops and arrays go hand in hand
.data
	# declare an rray for five integers, 5 x 4 = 20 bytes
	myArray: .space 20
	newLine: .asciiz "\n"
	
.text 
	main:
		# add integers into registers
		addi $s0, $zero, 100
		addi $s1, $zero, 200
		addi $s2, $zero, 300
		addi $s3, $zero, 400
		addi $s4, $zero, 500
	
		# index = $t0 
		addi $t0, $zero, 0 
		
		# store 100 into index 0
		sw $s0, myArray($t0)
			# increment index
		    addi $t0, $t0, 4 
		# store 200 into index 1
		sw $s1, myArray($t0)
			# increment index
	  	  addi $t0, $t0, 4
	  	# store 300 into index 2, etc.
		sw $s2, myArray($t0)
	  	  addi $t0, $t0, 4
	  	sw $s3, myArray($t0)
	  	  addi $t0, $t0, 4
	  	sw $s4, myArray($t0)
	  	  
		# reset index to zero
		addi $t0, $zero, 0 
	
	while: 
		# if index is 20 (index 5), exit 
		beq $t0, 20, exit 
		
		# load item from array
		lw $t6, myArray($t0)
		
		li $v0, 1
		move $a0, $t6 
		syscall
		
		# print new line
		li $v0, 4 
		la $a0, newLine
		syscall
		
		# increment index
		addi $t0, $t0, 4
		
		# repeat while loop until exit condition is met
		j while 
	    
	exit: 
		li $v0, 10
		syscall 
	
	
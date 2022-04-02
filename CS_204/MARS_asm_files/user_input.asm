.data 

.text 
	main: 
		jal getUserInput
		
		b exit 

	getUserInput:
		# get the input, li$v0 5 is read_int
		li $v0, 5
		syscall

		# move the input
		move $t0, $v0

		# display the input
		li $v0, 1
		move $a0, $t0
		syscall
		
		jr $ra

	exit:
		li $v0, 10 
		syscall 
	
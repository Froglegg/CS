.data
	message: 
		.asciiz "Branch 1: numbers equal"
	message2: 
		.asciiz "Branch 2: numbers not equal"
.text
	main:
		addi $t0, $zero, 20
		addi $t1, $zero, 20 
		
		beq $t0, $t1, branch_1 
		bne $t0, $t1, branch_2
		
		b exit
		
	branch_1:
		li $v0, 4 
		la $a0, message 
		syscall 
		
		b exit 
	branch_2:
		li $v0, 4 
		la $a0, message2
		syscall 
		
		b exit
	exit:
		#syscall to end program
		li $v0, 10 
		syscall

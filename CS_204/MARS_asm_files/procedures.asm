.data
	message: 
		.asciiz "Hello! \nThis is a message.\n"
	age:
		# a word is 32 bits, or 4 bytes, and in MIPS
		# you have a word, which is the basic unit of 
		# the architecture (x86, remember that 86 is a call back to 
		# Intel's 8086 style line of processors, x64 is actually 64bit 
		# architecture, or 8 byte architecture)
		# Words are stored in main memory (RAM)
		.word 69
		
.text
	main:
		# this will jump to displayMessage and set $ra to 
		# program counter (return address)
		jal displayMessage
		
		# do more stuff
		jal displayInteger
		
		b exit 
		
	displayMessage:
		li $v0, 4
		la $a0, message 
		syscall
		
		# whenever making a function, use jump register $ra, 
		# this will go back to the place it was called
		jr $ra
	displayInteger: 
		# system code 1 is print_int
		li $v0, 1
		# load word, not load address, into argument register, $a0
		lw $a0, age
		syscall
		
		jr $ra
		
	exit:
		#syscall to end program
		li $v0, 10 
		syscall

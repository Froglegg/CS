 # $v registers are for function returns 
 # $a registers are for function arguments
 
 # $t and $s registers work the same, its just conventional to use them in this way:
 
 # $t temporary caller saved registers, when calling a function,
 # these should not be garunteed to stay the same after a function return 
 # similar to let or var in JavaScript
 
 
 # $s callee saved registers; when calling a function,
 # these should remain the same after the function return
 # similar to const in JavaScript. 
 # The idea is to save and restore $s registers after a function call, garuntee they stay the same
 
 # $sp is the stack pointer
 # use this to store saved registers between function calls
 # must first allocate bytes (subtract from stack) before adding to stack
 .data 
 	# data in RAM
 	newLine: .asciiz "\n"
 	
 .text
 	main:
 		addi $s0, $zero, 10 
 		
 		# this will increase the value by 30, print inside the function
 		jal increaseMyRegister
 		
 		# print new line 
 		li $v0, 4 
 		la $a0, newLine 
 		syscall 
 		
 		# and then it's going to print 10, the original value, to follow convention
 		# load print_int function
 		li $v0, 1
 		# move saved register 0 into argument 0 and fire syscall
 		move $a0, $s0 
 		syscall
 		
 		b exit 
 	
 	increaseMyRegister:
 		# allocate a byte for integer to stack
 		# add immediately to stack pointer the stack pointer -= 4 bits
 		addi $sp, $sp, -4
 		
 		# save the (word) value in $s0 to the first location in the stack pointer 0($sp)
 		# offset() has to be a multiple of four, at least a byte
 		# here, we use offset 0($sp) because only one slot has been allocated, so position $($sp) is open
 		sw $s0, 0($sp)
 		
 		# add 30 to value in register
 		addi $s0, $s0, 30
 		
 		# print new value in function
 		li $v0, 1 
 		move $a0, $s0
 		syscall
 		
 		# load word in $s0 from RAM, set $s0 to top stack position, which is the old value
 		lw $s0, 0($sp)
 		# restore (pop) allocated byte(s) from stack
 		addi $sp, $sp, 4
 		
 		# return to main
 		jr $ra
 	exit:
 		li $v0, 10 
 		syscall 
# declare global so programmer can see actual addresses.
.globl welcome
.globl f_to_c_prompt
.globl c_to_f_prompt
.globl fahrenheitSumText
.globl celsiusSumText
.globl choice

#  Data Area
.data
welcome:
	.asciiz " This program converts Celsius to Fahrenheit \n\n"

choice:
    .asciiz " Type 1 and hit enter to convert from f to c,\n else type 0 to convert from c to f: "

c_to_f_prompt:
	.asciiz " Enter an integer Celsius temperature: "
	
f_to_c_prompt:
	.asciiz " Enter an integer Fahrenheit temperature: "

fahrenheitSumText: 
	.asciiz " \n F = "

celsiusSumText: 
	.asciiz " \n C = "

coldText:
	.asciiz "\nBrrrr!!!\n"

hotText:
	.asciiz "\nIt's SWELTERING!\n"
zero_as_float:
	.float 0.0
scalar_1_float:
	.float 1.8
scalar_2_float:
	.float 32.0 
	
#Text Area (i.e. instructions)
.text

main:
	# load float operands into coprocessor registers
	lwc1 $f4, zero_as_float
	lwc1 $f6, scalar_1_float 
	lwc1 $f8, scalar_2_float 
	 
	# Display welcome
	li $v0, 4
	la $a0, welcome
	syscall
	
	# jump and link to c_or_f choice prompt, which saves choice of 1 or 0 in $s0 register
    	jal c_or_f
    	
    	# conditional branches
	beqz $s0, c_to_f
	bnez $s0, f_to_c

    	
c_or_f:
	# prompt for choice
	li $v0, 4
	la $a0, choice
	syscall 
	
	# get the input
	li $v0, 5
	syscall

	# save choice of 1 or 0 to $s0 register
	move $s0, $v0
	
	# return to program counter
	jr $ra
	
        
c_to_f:
	# prompt for input 
	li $v0, 4
	la $a0, c_to_f_prompt
	syscall 
	
    	# read in and store float to $f0, floating point subprogram return register
    	li $v0, 6
    	syscall
    	
    	# floating point arithmetic
	# $f0 was our previous functions return value, $f6 is a scalar operand, etc.
	# here, we are storing the results of these functions to $f12 cumulatively
	# end result is ((C * 1.8) + 32) stored to float register $f20, which is preserved across calls
	mul.s $f12, $f0, $f6
	add.s $f20, $f12, $f8
	
	j display_fahrenheit
	
f_to_c:
	# display prompt
	li $v0, 4
	la $a0, f_to_c_prompt
	syscall 
	
	# take float input, goes into float return $f0
    	li $v0, 6
    	syscall
    	
    	# formula is (F - 32) / 1.8
	sub.s $f12, $f0, $f8
	div.s $f20, $f12, $f6
	
	j display_celsius

display_fahrenheit: 
	
	li $v0, 4 
	la $a0, fahrenheitSumText 
	syscall 
	
    	# display float stored in $f20, fahrenheit value
    	li $v0, 2 
    	add.s $f12, $f4, $f20
    	syscall
	
	b exit 
	
display_celsius:
	li $v0, 4 
	la $a0, celsiusSumText 
	syscall 
	
	# display float stored in $f20, celsius value
    	li $v0, 2 
    	add.s $f12, $f4, $f20
    	syscall
	
	b exit 

exit: 
	li $v0, 10
	syscall 
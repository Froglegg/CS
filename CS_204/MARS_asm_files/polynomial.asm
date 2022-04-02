#Evaluate the expression: 4x^2 - 8x + 2

.data
prompt:	.asciiz "Enter an input for x to evaluate 4x^2 - 8x + 2: "
output:	.asciiz	"The output is "
isPositiveString: .asciiz "The result is positive"
isNegativeString: .asciiz  "The result is negative" 

.text
main:	

	li	$v0,	4	#output the prompt for user
	la	$a0,	prompt
	syscall

	li	$v0,	5	#input the number and save it to $s0
	syscall
	move 	$s0,	$v0

	#square the input
	#lw	$t0, ($s0)
	mul	$t0, $s0, $s0

	#multiply by 4
	mul	$t0, $t0, 4

	#multiply input by -8
	#lw 	$t2, ($s0)
	mul 	$t2, $s0, -8

	#add it all
	add	$t0, $t0, $t2
	add	$t0, $t0, 2
	move 	$s2, $t0

	li	$v0,	4	#print the output label
	la	$a0,	output
	syscall

	li	$v0,	1	#output the number that was entered
	move	$a0,	$s2	#could also use lw $a0, $s0. Pseudo code
	syscall

	jal printNewLine 
	bltzal $s2, isNegative 
	bgezal $s2, isPositive

	b exit 

printNewLine: 
	li	$v0, 	0xB	
	#print newline, 0xB = 11 
	#which is the system call to print a single character   
	la	$a0, 	1010	#0xA is the newline char
	syscall
	
	jr $ra 
	

isPositive: 
	li $v0, 4
	la $a0, isPositiveString 
	syscall 
	
	jr $ra

isNegative: 
	li $v0, 4
	la $a0, isNegativeString 
	syscall 
	
	jr $ra

exit: 
	li $v0, 10 
	syscall 


# Introduction to pointers to C
In a typical memory architecture, each byte of memory has an address in RAM.

When a variable is declared, memeory is allocated according to the data type.

Computer has a lookup table for variables, with variable name, type, and address

int - 4 bytes
char - 1 byte
float - 4 bytes

The address of a variable consists of an adress and an offset based on type, capturing the next n addresses

Pointers: variables that store the address of another variable, declared with the unary operator *, called the dereference operator
```
int *p;
```
The unary operator &, or address of operator, returns the address of a variable
```
p = &a;
```

If we put an asterisk point in front of a pointer, e.g., `**p`, this will dereference and return the value at the pointer.
```
int a;
int *p;
p = &a;
a = 5;
print(*p) // returns 5
```


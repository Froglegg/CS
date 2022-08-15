# pointers to pointers
A pointer to a pointer is declared like so:
```
int x = 5;
int *p;
p = &x;
// set x to 6
*p = 6;
// declare a pointer to a pointer using double asterisks **
int **q;
q = &p
```
We can go on like this, declaring pointers to pointers to pointers...
```
int ***r;
r = &q // q is int** type;
```


#include <stdbool.h>
#include <stdio.h>
// identifiers that begin with an underscore and a cap letter or another underscore are
// reserved keywords
_Bool flag1 = 0;
// we should just include bool type and use bool as that's becoming standard
bool flag2 = false;
// the C language defines three character types: char, signed char, and unsigned char
// used to represent character data, char is used for standard characters / basic
// execution set of characters the 'wide' type defines a wider character set type, for
// international users, use the wchar_t type
char some_char = 'A';              // evalues to ascii 65
signed char signed_char = 'a';     // evaluates to ascii int 97
unsigned char unsigned_char = 'a'; // evaluates to ascii int 97
// numerical types include various int types, enum and float
// int
short int short_int = 2;
int some_regular_int = 69420;
long int long_int = 6942069420;
long long int long_long_int = 694206942069420;
//  enums that aren't given defaults have first item defaults of 0, and then += 1 for
//  each one after
enum day { sun, mon, tues, wed, thu, fri, sat };
// specify first value will fill in all the others with += 1
enum month { jan = 1, feb, mar, apr, may, jun, jul, aug, sept, oct, nov, dec };
// you can also specify all values in an enum
enum cardinal_directions { north = 0, east = 90, south = 180, west = 270 };
// floats
float some_float = 1.423;
double some_double = 5.694206969;
long double long_double = 420.6969696969696969696969;
// void type is a weird type. Used to indicate a funciton that doesn't return anything,
// or as a sole parameter in a function that doesn't take any arguments
void some_func(void) { printf("I don't take no args or return anything"); }

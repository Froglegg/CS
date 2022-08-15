# Character arrays and pointers
When we talk about character arrays in C, we want to talk about strings. Character arrays are used to store strings.

1. How to store strings
- character array must be large enough to store the string (size >= # of characters in the string + 1 null terminating \0 character)
- the last character must be a null terminating character (\0), so that the function knows that the string has finished in a character array. All functions expect strings to be terminated by a null character

2. Arrays and pointers are different types that are used in a similar manner

3. Arrays are always passed to functions by reference



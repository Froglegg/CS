# Pointers as function returns
A pointer is just another data type, it just stores the address of another data type, so it is quite possible for a function to return a pointer.

However, you can get into trouble if you call functions between initializing a variable for an argument and a call by reference function that returns a pointer. You may get a garbage value when you try to dereference the returned pointer.

This is because the address was deallocated in the function called between the initialization of the variables and the call by reference function.

If for whatever reason, you want to return pointers from a function, use a static or global declaration for your variables, so that the memory does not get deallocated within an intermediary stack frame.
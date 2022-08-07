# Executables
The last phase in the compilation process, the link phase, takes the object code for
all of the tranlsation units in the program and links it together to form a final
executable.

This can be an executable a user can run like a .out file or .exe, a library, or a
more specialized program such as a device driver or firmware image (machine code to be
burned onto a ROM). Linking allows you to seperate your code into distinct source files that can be compiled independently, which helps you build reusable components.

## Libraries
Libraries are executable components that cannot be executed independently. Instead, you can incorporate a library into exectuable programs via a header file. E.g., the C standard library <stdlib.h>.

Libraries are linked into your application and can be either static or dynamic. A static library, also known as an archive, incoprorates its machine or object code directly into the resulting executable, which means that a static library is often tired to a specific release of the program. Because a static library is incorporated at link time, the contents of the static library can be further optimized for your progam's use of the library, which means that unused library code can be stripped from the final executable.

Dynamic libraries, or shared libraries, is an executable w/o startup routines. It can be pacakged with the exectuable or instsalled separately but must be available when the exceutable calls a function provided by the dynamic library. Many modern OS will load the dynamic library code into memory once (e.g., Windows compiles dynamic link library .dll files as index and compiled code of shared libraries) and share it across all the applications that need it. You can replace a dynamic library with different versions as necessary after your application has been deployed. Letting the library evolve separately from an application comes with its own set of benefits and risks, however the benefit of dynamic libraries outweigh the drawbacks in most situations.



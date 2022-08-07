# GCC and Clang compiler flags
Use compiler options to maximize diagnostics to help you eliminate as many defects as possible
- D_FORTIFY_SOURCE=2 (detect runtime buffer overflows)
- fpie -w1, -pie (needed to disable full ASLR [address space layout randomization] for executables)
- fpic -shared (disable text relocations for shared libraries)
- g3 (generate abundant debugging information)
- O2 (optimize code for speed/space efficiency)
- Wall (turn on recommended compiler warnings)
- Werror (turn warnings into errors)
- std=c17 (specify langauge standard)
- pedantic (issue warnings demanded by strict conformance to the standard)


# Steps taken to create and link static library
1. create isprime.c, driver.c and isprime.h (public interface for static library) files and code
2. run the following:
```
clang -c -std=c17 -Wall -Wextra -pedantic -Werror isprime.c -o bin/isprime.o
clang -c -std=c17 -Wall -Wextra -pedantic -Werror driver.c -o bin/driver.o
```
using clang to compile both the C source files into object files placed into a /bin directory
3. Create an archive (static library) with the following:
```
ar rcs bin/libPrimalityUtilities.a bin/isprime.o
```
the r option replaces existing files, c option creates the archive, and the s option writes an object-file index into the archive (which is equivalent to running the `ranlib` command). This creates a single archive file that's structured to allow retrieval of the orgiinal object files used to create the archive, similar to a compressed tarball or ZIP file. By convention, static libraries on Linux systems are prefixed with `lib` and end in `.a`
4. Link the driver object file to the `libPrimalityUtilities.a` static library (archive) to produce an executable called `primetest` by running the following command:
```
clang bin/driver.o -Lbin -lPrimalityUtilities -o bin/primetest
```
The -L flag instructs the linker to look in the local bin directoyry for libraries to link, and the -l flag instructs the linker to link the `libPrimalityUtilities.a` library to the executable output. **Omit the `lib` prefix and the `.a` suffix becuase the linker adds them implicitly**
5. You can now run the primetest program that uses the static library to test long long unsigned integers like so `./bin/primetest 42069`
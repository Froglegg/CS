# Pre-processors
The preprocessor is the part of the C compiler that runs at an early phase of
compilation and transforms the source code beofre it's translated, such as inserting code from one file (typically a header file) into another (typicaly a source file)

The preprocessor also allows you to specify that an identifier should be automatically subsituted by a source code segment during macro expansion

## The compilation process
The compilation process consists of a pipeline of 8 phases:

Phase 1: Character Mapping
Phase 2: Line splicing
Phase 3: Tokenization
Phase 4: **Preprocessing**
Phase 5: Character-set mapping
Phase 6: String concatenation
Phase 7: Translation
Phase 8: Linkage

The preprocessor runs before the source code is translated into object code by the translator. This allows the preprocessor to modify the source code written by the user before its operatored on by the translator. Consequently, the preprocessor has a limited amount of semantic information about the program being compiled (doesn't know about functions, variables, or types), but only has information on basic elements, such as header names, identifiers, ltierals, and punctuation characters. These basic elements are called "tokens", and are the smallest elements of a computer program that have meaning to a compiler.

The preprocessor operates on **preprocessing directives** that you include in the source code to program the behavior of the preprocessor, for example:
```
#include
#define
#if
```
These directives cause hte preprocessor to take an action and alter the code before it goes to translation. You can view preprocessed output files using command line args like `clang other-options -E -o output_file.i source.c`


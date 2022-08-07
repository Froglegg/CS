## Linkage
Linkage is a process that controls whether an interface is public or private and determines whether any two identifiers refer to the same entity. C provides three kinds of linkage: external, internal, or none.

When a declaration has external linkage, identifiers referring to that declaration all refer to the same entity (such as a function or object) everywhere in the program.

When a declaration has internal linkage, identifiers only refer to the same entity within the translation unit containing the declaration. If two translation units refer to the same internal linkage identifier, they refer to different instances of the entity.

If a declaration has no linkage, it is a unique entity in each translation unit.

The linkage of a declaration is either explicitly declared or implicitly implied. If you declare an entity at file scope without explicitly speficifyin `extern` or `static`, it is implicitly given external linkage. Identifiers with no linkage incude function params, block scope identifiers declared without an `extern` storage class specifier, or enumeration constants.

E.g.,
```
static int i; // i is declared with explicit internal linkage
extern void foo(int j){
    // foo is declared with explicit external linkage
    // j has no linkage because it is a parameter
}
```

Declaring an identifier with the `static` storage class specifier gives internal linkage only to file scope entities. Declaring it at block scope creates an identifier with no linkage, but it does give the variable static storage duration (entire execution time of the program).

The identifiers in your public interface should have exeternal linkage so that they can be called from outside their translation unit, while the identifiers that are implementation details should be declared with internal or no linkage.

A common approach to achieiving this is to declare your public interface functions in a header file using the `extern` storage specifier, and define the public interface functions in a source file in a similar manner.

However, within the source file, all declarations that are implementation details should be explicitly declared static to keep them private, accessible to just that source file.

A good practice is that file scope entities that don't need to be visible outside the file should be declared as static, which limits the pollution of the global namespace and decreases the chances of surprising interactions between translation units.




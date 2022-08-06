# Principals of componentization
## coupling and cohesion
- low coupling and high cohesion is desirable
- cohesion: measure of the commonality between elements of a programming interface, for example, a header file that has functions that do several different / unrelated things has low cohesion, while a header file that has functions that are all related (e.g., all related to string manipulation) has high cohesion.
- coupling: measure of the interdependency of programming interfaces, for example, a tightly coupled header file can't be included by itself in a program, instead, in must be included with other header files in a specific order. When interfaces are tightly coupled, modifying program behavior becomes difficult, because changes can have a ripple effect across the system.

By separating your program logic into distinct, highly cohesive components, you make it easier to reason about the components and test the program.

## Code re-use
encapsulate logic that you might repeat more than once in a function, DRY.

## Data abstraction
Reussable sotware component that enforeces a clear separation between the public interface and implementation details. The public interface for each data abstraction includes the data-type definitions, function declarations, and constant definitions required by the users of the data abstraction and is placed in header files. Implementation details, and any private util functions, are hidden within a source file, or a header file that's separate from the public inteface headers.

## Opaque types
Opaque (or private) data types are those expressed using an incomplete type, such as a forward-declared sturcture type. An incomplete type is a type that describes an identifier but lacks information needed to determine the size of objects of that type or their layout.
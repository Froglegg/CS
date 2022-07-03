// frequently, a value in one type (e.g., float) must be represented in another (e.g.,
// int). Values can be implicitly or explicity converted from one type to another.

// You can use the `cast` operator to perform explicit conversions.
// to perform a cast, place the type name in parens just before the expression

// implicit conversion, also known as 'coercion', occurs automatically when e.g.,
// operations are performed on mixed types
// The rules concerning implicit conversion depend on integer conversion rank, integer
// promotions and usual arithmetic conversions. These concepts determine when and how
// conversions are implicitly performed.

int main(void) {
  int si = 5;
  short ss = 8;
  // cast si to long type, this is garunteed to be a safe cast because it is from a
  // smaller type to a larger
  long sl = (long)si;
  // cast the sum of ss and ll to unsigned short
  // result of this conversion might not be equal to the original value, because we are
  // casting a larger type to a smaller type
  unsigned short us = (unsigned short)(ss + sl);
}

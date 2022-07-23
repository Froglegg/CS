#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool safediv(int dividend, int divisor, int *quotient) {
  // test for null pointer
  if (!quotient)
    return false;
  // test for signed integer overflow
  if ((divisor == 0) || ((dividend == INT_MIN) && (divisor == -1)))
    return false;
  *quotient = dividend / divisor;
  return true;
}

void printgrade(unsigned int marks) {
  if (marks >= 90) {
    // int puts(const char *str) writes a string to stdout
    puts("YOUR GRADE: A");
  } else if (marks >= 80) {
    puts("YOUR GRADE: B");
  } else {
    puts("YOU FAILED, NEED AT LEAST A B");
  }
}

void print_grade_switch(unsigned int marks) {
  // integer promotions are performed on the controlling expression
  // i.e., if the result is a float then it is converted into an integer
  // e.g., 95/10 = 9.5 is promoted to integer 9, essentially ignoring the float point
  switch (marks / 10) {
  case 10:
  case 9: {
    puts("YOUR GRADE: A");
    break;
  }
  case 8: {
    puts("YOUR GRADE: B");
    break;
  }
  default: {
    puts("YOU FAILED");
  }
  }
}

typedef enum { Savings, Checking } AccountType;
void assignInterestRate(AccountType account) {
  double interest_rate;
  switch (account) {
  case Savings: {
    interest_rate = 3.2;
    break;
  }
  case Checking: {
    interest_rate = 1.3;
    break;
  }
  default: {
    // abort program execution and come out directly from place of call
    abort();
  }
  }
  printf("Interest rate = %g\n", interest_rate);
}

int main(void) {
  int div = 100;
  int divisor = 25;
  int quotient;
  bool is_safe = safediv(div, divisor, &quotient);
  if (is_safe) {
    // use braces in conditionals as whitespace and indentation is meaningless to the
    // compiler
    printf("%d\n", quotient);
  }

  printgrade(50);
  print_grade_switch(80);
  assignInterestRate(Savings);
  assignInterestRate(Checking);

  return 0;
}
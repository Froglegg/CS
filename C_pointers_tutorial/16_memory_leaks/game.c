#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int cash = 100;
void Play(int bet) {
  // delcaring a variable on the heap vs a stack coudl cause a memory leak if you don't
  // free the variable char C[3] = {'j', 'k', 'q'};
  char *C = (char *)malloc(3 * sizeof(char));
  C[0] = 'j';
  C[1] = 'k';
  C[2] = 'q';
  printf("shuffling\n");

  srand(time(NULL));
  for (int i = 0; i < 5; i++) {
    int x = arc4random() % 3;
    int y = arc4random() % 3;
    int temp = C[x];
    C[x] = C[y];
    C[y] = temp;
  }
  int playerGuess;
  printf("What's the guess?\n");
  scanf("%d", &playerGuess);
  if (C[playerGuess - 1] == 'q') {
    cash += 3 * bet;
    printf("%s\n", C);
    printf("\nYou win! cash is now %d", cash);
  } else {
    cash -= bet;
    printf("%s\n", C);
    printf("\nYou lose! cash is now %d", cash);
  }
  free(C);
}

int main(void) {
  int bet;
  while (cash > 0) {
    printf("\nplace bet:");
    scanf("%d", &bet);
    if (bet == 0 || bet > cash)
      break;
    Play(bet);
  }
  return 0;
}
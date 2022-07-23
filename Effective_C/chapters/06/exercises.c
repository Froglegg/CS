#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void print_error(int errnum) { printf("%s", strerror(errnum)); }

int main(void) {
  //   print_error(4);
  DIR *open_directory = opendir("./test_dir");

  if (open_directory == NULL) {
    puts("Unable to read directory");
    return (1);
  } else {
    puts("Directory is opened!");
  }
  closedir(open_directory);

  return (0);
}

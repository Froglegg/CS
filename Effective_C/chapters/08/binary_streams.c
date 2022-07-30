#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct sigrecord {
  int signum;
  char signame[10];
  char sigdesc[100];
} sigrecord;

int write_binary_to_file(void) {

  int status = EXIT_SUCCESS;
  FILE *fp;
  sigrecord sigrec;
  // open file in binary write mode
  // assignment to fp variable can occur within if statement itself
  if ((fp = fopen("signals.txt", "wb")) == NULL) {
    fputs("Cannot open file\n", stderr);
    return EXIT_FAILURE;
  }

  sigrecord sigrec30 = {30, "USR1", "user-defined signal 1"};
  sigrecord sigrec31 = {31, "USR2", "user-defined signal 2"};
  size_t size = sizeof(sigrecord);
  // fwrite operates on a binary stream
  // it writes up to nmemb elements of size bytes from ptr to (FILE)stream
  if (fwrite(&sigrec30, size, 1, fp) != 1) {
    fputs("Cannot write sigrec30 to signal.txt\n", stderr);
    status = EXIT_FAILURE;
    goto close_files;
  }

  if (fwrite(&sigrec31, size, 1, fp) != 1) {
    fputs("Cannot write sigrec31 to signal.txt\n", stderr);
    status = EXIT_FAILURE;
    goto close_files;
  }

close_files:
  if (fclose(fp) == EOF) {
    fputs("Failed to close file\n", stderr);
    status = EXIT_FAILURE;
  }
  return status;
}

int read_binary_from_file(void) {
  int status = EXIT_SUCCESS;
  FILE *fp;
  sigrecord sigrec;
  size_t size = sizeof(sigrecord);
  // open in read binary mode
  if ((fp = fopen("signals.txt", "rb")) == NULL) {
    fputs("Cannot open file\n", stderr);
    return EXIT_FAILURE;
  }
  // set file position indicator to the start of the second signal in signals.txt
  // the first signal is at position 0 in the file, and each subsequent signal is at an
  // integer multiple of the size of the structure
  if (fseek(fp, size, SEEK_SET) != 0) {
    fputs("fseek failed", stderr);
    status = EXIT_FAILURE;
    goto close_files;
  }
  // call fread to read the data from the binary file into the structure referenced by
  // &sigrec similar to fwrite, fread reads up to one element, whose size is specified by
  // size, from the steam pointed to by fp.
  // the file position indicator is advanced by the number of characters succesfully read
  if (fread(&sigrec, size, 1, fp) != 1) {
    fputs("Cannot read", stderr);
    status = EXIT_FAILURE;
    goto close_files;
  }

  printf("Signal\n number = %d\n name = %s\n descrption = %s\n\n", sigrec.signum,
         sigrec.signame, sigrec.sigdesc);

close_files:
  fclose(fp);
  return status;
}

int main(void) {
  int write_status = write_binary_to_file();
  int read_status = read_binary_from_file();
  if (write_status == EXIT_SUCCESS && read_status == EXIT_SUCCESS) {
    return EXIT_SUCCESS;
  }
  return EXIT_FAILURE;
}
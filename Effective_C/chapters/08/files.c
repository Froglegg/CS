#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

void test_file_stuff(void) {
  // open file for read, write, etc.
  FILE *test_file_read = fopen("./test.txt", "r");
  // closing file flushes buffer stream
  fclose(test_file_read);

  // open file to write characters
  FILE *test_file_write = fopen("./test.txt", "w");
  // fputc write x char (ascii code 120) to stream
  fputc(120, test_file_write);
  fputc(120, stdout);
  // fputs function put string to steam
  fputs("I am groot \n", test_file_write);
  // puts writes directly to stdout
  fputs("I am groot\n", stdout);
  puts("I am groot as well\n");
  fclose(test_file_write);

  // use fseek to navigate through an open file
  FILE *open_file = fopen("./test.txt", "r");
  // SEEK_END is end of file, SEEK_SET is beginning, SEEK_CUR moves file pointer to
  // given location
  // here, we are telling fseek to go to the end of file
  fseek(open_file, 0, SEEK_END);
  // ftell gives the current file position of the given stream in long bytes
  long unsigned len = ftell(open_file);
  // initialize string to store file data with length of file
  char test_fgets[len];
  // reset cursor to beginning of file
  fseek(open_file, 0, SEEK_SET);
  // fgets to read file contents into string
  fgets(test_fgets, len, open_file);
  puts("CONTENTS OF TEST.txt:");
  puts(test_fgets);
  fclose(open_file);

  // the fflush function delivers any unwritten data for a stream to the host environment
  // to be written to a file
  // fflush()
};

int file_position_stuff(void) {
  // file position indicator descirbes where int he file the stream is currently reading
  // or writing
  // when you open a file, the indicator is positioned at file's start.
  // you can position the indicator elsewhere.
  // use fseek to set file position indicator (cursor) and ftell to return the long int
  // bytes offset
  FILE *fp = fopen("test_2.txt", "r");
  // fopen returns a null pointer if it fails
  if (fp == NULL) {
    fputs("Cannot read file, \n", stderr);
    return EXIT_FAILURE;
  }
  // fseek returns nonzero only for a request that cannot be satisfied
  if (fseek(fp, 0, SEEK_END) != 0) {
    fputs("SEEK to end of file failed\n", stderr);
    return EXIT_FAILURE;
  }
  long int fpi = ftell(fp);
  // on failure, ftell returns -1L and an implementation defined errno
  if (fpi == -1L) {
    // perror returns custom string and then implementation defined error to stderr
    perror("TELL error");
    return EXIT_FAILURE;
  }
  printf("file position = %ld\n", fpi);
  // fclose returns EOF if any errors were detected
  if (fclose(fp) == EOF) {
    fputs("Failed to close file\n", stderr);
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}

int file_position_stuff_2(void) {
  // fgetpos and fsetpos are newer functions
  FILE *fp = fopen("test_2.txt", "w+");
  if (fp == NULL) {
    fputs("Cannot read file, \n", stderr);
    return EXIT_FAILURE;
  }
  // use file position type fpos_t to declare position variables
  fpos_t pos;
  // use fgetpos to get current file poisition within file
  if (fgetpos(fp, &pos) != 0) {
    perror("get position");
    return EXIT_FAILURE;
  }
  // write some text to the file
  if (fputs("abcdefg", fp) == EOF) {
    perror("Canot write to file: ");
    return EXIT_FAILURE;
  }
  // then restore file position indicator to the address of the value stored in pos
  if (fsetpos(fp, &pos) != 0) {
    perror("set position");
    return EXIT_FAILURE;
  }
  // retrieve and print file position
  long int fpi = ftell(fp);
  if (fpi == -1L) {
    perror("TELL error");
    return EXIT_FAILURE;
  }
  printf("file position = %ld\n", fpi);
  // write again, this will overwrite if the position was reset
  if (fputs("0123456789", fp) == EOF) {
    perror("puts error: ");
    return EXIT_FAILURE;
  }
  if (fclose(fp) == EOF) {
    fputs("Failed to close file\n", stderr);
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}

int temp_files(void) {
  // temp files are often used as an interprocess communication mechanism or for
  // temporarily storing information out to disk to free up RAM.
  // use TMPDIR environment variable to specify the location of global temp directories
  char str[] = "Hello World";
  int i = 0;
  // use tmpfile or tmpnam to create temp files
  // tmpfile() function is defined in the “stdio.h” header file.
  // The created temporary file will automatically be deleted after the termination of
  // program. It opens file in binary update mode i.e., wb+ mode.
  FILE *tmp = tmpfile();
  if (tmp == NULL) {
    puts("Unable to create temp file");
    return EXIT_FAILURE;
  }

  puts("Temporary file is created\n");
  while (str[i] != '\0') {
    // put chars from string up until null \0 to tmp file
    fputc(str[i], tmp);
    i++;
  }

  // rewind() function sets the file pointer
  // at the beginning of the stream.
  rewind(tmp);
  // while not end of file
  while (!feof(tmp))
    // put char from tmpfile to stdout
    putchar(fgetc(tmp));

  return EXIT_SUCCESS;
}

int main(void) {
  // test_file_stuff();
  // file_position_stuff();
  // file_position_stuff_2();
  temp_files();
  return 0;
}
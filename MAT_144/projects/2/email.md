Dropbox created for second programming project due before midnight on November 20th, 2021.

There are 120 permutations containing the string "ABC". Your job is to find them or "filter" them out. (Use "filter" in Python or Racket, or "Cases" or "Select" in Mathematica) and then return the list, and don't forget to print out the list so I can view your results.

If you're using Python you should begin your assignment using the Python class file I emailed to the class. The algorithm I used in the file is sufficient for the assignment, although very slow for permuting large lists. But "ABCDEFG" is not a large or very long list of characters. By the way, in Python to convert a string to a list of characters, all that is needed is to use the "list" function. list("ABCDEFG") returns ["A", "B", "C", "D", "E", "F", "G"].

Then you can do this:

p = Permutations(["A", "B", "C", "D", "E", "F", "G"], 7) in order to find the permutations.

You are NOT interested in a permutation with repetition for this particular problem! In the context of this particular problem, such repetition makes no sense at all.

Therefore, the list you want to look at (using my Python class file) is contained in the instance variable, p.permutations_without_repetition.

Then you must manipulate that list so that it contains ONLY those sublists that contain the string "ABC" (in that order, "B" right after "A", and "C" right after "B").

This project really isn't that hard. If you need to, read some of the material in Chapter 6 in order to learn whatever background information you think you need in order to complete the assignment. You should have plenty of time to complete this assignment, especially since I'm getting you started with a Python class file I wrote specifically to help you out.

Good luck with this assignment! It should be fun and interesting for you. By the way, these exercises in string and list manipulations are very important in the area of BioInformatics, where researchers have to work with extremely long gene sequences. Gene sequences are composed of four nucleotides, "A" for adenosine, "C" for cytosine, "G" for guanine and finally "T" for thymine. Therefore, the "alphabet" of genetics contains only 4 characters or "letters". Gene sequences can be extremely long, containing thousands upon thousands of different permutations of those 4 letters! Extremely interesting stuff! It's worth learning about.

Be well & study hard!

Best,

Mr. Lewit

Dear discrete students,

In a previous email I wrote that there are 720 answers to the second programming project. But then in another email I wrote there are 120 answers. 720 was a typo! I just did the problem myself (using Python, but you will get the same results if you use Mathematica or Racket) and my solution contained 120 possible strings containing "ABC".

In my Python class file, I actually compute permutations using the idea of a Cartesian product. Probably not the fastest and most efficient way of doing this, but for the second programming project this approach should be efficient enough and fast enough to get the job done. The Big-O of my algorithm is n! Therefore, please don't use my class file to permute very large lists. You'll either run out of computer memory, or you'll have to wait several days for an answer!!!

Best of luck with this programming assignment. It's really not that hard to do.

Cheers,

Mr. Lewit

Dear discrete math students,

Let's streamline things a bit for the second programming project. I'm going to take a problem Ch. 6 of your textbook, on pg. 431. The problem reads thusly:

How many permutations of the letters "ABCDEFG" contain the string "ABC"?

The book tells us that the answer is 720, right? And...yes it is! Your job for the second programming assignment is to print out those 720 permutations. You CAN use Racket to do this, but for most of you I think that's going to be a little too challenging. This problem is actually not hard at all if you're using Mathematica. If you insist on using Python, you'll have to be somewhat creative. Please resist the temptation to import a package or module that does all the work for you! Where's the fun in that?

For those of you who are loyal fans of Python (and that's most of you!) I am attaching my permutations.py file that should make this assignment much easier for you to do.

For example, in your Python shell, do the following (just an example):

from permutations import \*

p = Permutations(["A", "B", "C", "D"], 4)

for perm in p.permutations_with_replacement:

     print(perm)

for perm in p.permutations_without_replacement:

     print(perm)

See the difference between the two permutations? For the problem above you'll need to focus your attention on the permutation that does not have repetition. It's really not that hard. You just need to write your own filter function that filters out any list where the letters "A", "B", and "C" appear as a consecutive block. And of course, you have to write your name at the top of the .py file, and then just submit the file to me using the dropbox in your course shell--the dropbox that I will create for you within the next few days. Or...do this yourself using Racket! Or...use Mathematica if you prefer. But for most of you it might be much easier to use Python since the majority of you have already done some Python programming, either in another course or on your own.

Best of luck with the assignment. It's really not that hard. I also suggest doing some reading in Chapter 6 if you're not that familiar with the mathematical concepts of combinations and permutations.

Best,

Mr. Lewit

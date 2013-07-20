This is a (failing) submission to http://www.spoj.com/problems/PALIN/

It needs to run faster.

All the people winning on here are using C and C++.
 Python needs to step up and show what it can do.

--------------
Currently, palin2.py is the fastest.
  Looks like most of the speed issues stem from the conversion from strings to lists for slicing and reversing 'syntax sugar'.

  Also, I cast to long to increment, which is also probably eating time.

----

  I want to dive deep into the python long implementation (in C).  
  I believe it's simply a linked list duck-typed like a number

  If so, I should easily be able to mash something together to create a class that has:
  1) The addition (increment) feature of a long
  2) The slicing features of a list

  I also REFUSE! (OMG!) to look at other people's solutions just yet.
   ---that's what I do at work all day, can't I just tackle something and pretend I'm the first one trying to solve it?


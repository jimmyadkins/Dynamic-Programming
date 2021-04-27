# Dynamic-Programming

## Scenario 1: Increasing Sequences
#### You are given a list of numbers, such as:
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20 | 15 | 30 | 28 | 33 | 32 | 18 | 26 | 41 | 37 | 50 | 29 |

#### and you wish to find a non-contiguous sequence of numbers that are in the same order as the list, but in which the numbers are in increasing order. 
For example:

(15, 33, 41, 50) is such a sequence.
(20, 30, 33, 41, 50) is also such a sequence.
(20, 15, 28, 32) is not such a sequence, because the numbers aren't increasing.
(15, 18, 20, 26) is not such a sequence, because the numbers aren't in the same order as the source list.

#### In particular, you wish to find the length of the longest such sequence and what that sequence is. (There may be more than one at this length, so any one of these sequences is sufficient.) In this example, the maximum length is 5, and the program I wrote to test this returned (15, 18, 26, 37, 50), although the sequence (20, 30, 33, 41, 50) shown above is also an answer.

#### Here's another example for you: 
for the source list (36, 13, 78, 85, 16, 52, 58, 61, 63, 83, 46, 19, 85, 1, 58, 71, 26, 26, 21, 31), the longest sequence is 8 long, and an example is (13, 16, 52, 58, 61, 63, 83, 85)

## Scenario 2: Palindromes

#### Unless you are suffering from Aibohphobia, you probably remember that we did an example with recursion last year in which you determined whether a string was a palindrome (e.g., "tot" or "abba" or "racecar" or "amanaplanacanalpanama") or not. In this case, we will take a long string (e.g., "ibidonatacocatonebaylasttuesday") and attempt to find the longest palindrome within the string (in this case, it is "tacocat," which has a length of 7.)

#### I am giving you a file containing a much longer string, a modified version of a selection from Alice in Wonderland, called "Alice.txt." It is a little less than ten thousand characters long. You are to find the length of the longest palindrome in this text (and what that palindrome is….)

##### At 642 characters long: 'TWINKLETWINKLELITTLEBATHOWIWONDERWHATYOUREATYOUKNOWTHATSONGPERHAPSIVEHEARDSOMETHINGLIKEITSAIDALICEITGOESONYOUKNOWTHEHATTERCONTINUEDINTHISWAYUPABOVETHEWORLDYOUFLYLIKEATEATRAYINTHESKYTWINKLETWINKLEHERETHEDORMOUSESHOOKITSELFANDBEGANSINGINGINITSSLEEPTWINKLETWINKLETWINKLETWINKLEANDWENTONSOLONGTHATTHEYHADTOPINCHITTOMAKEITSTOPPOTSTIEKAMOTTIHCNIPOTDAHYEHTTAHTGNOLOSNOTNEWDNAELKNIWTELKNIWTELKNIWTELKNIWTPEELSSTINIGNIGNISNAGEBDNAFLESTIKOOHSESUOMRODEHTEREHELKNIWTELKNIWTYKSEHTNIYARTAETAEKILYLFUOYDLROWEHTEVOBAPUYAWSIHTNIDEUNITNOCRETTAHEHTWONKUOYNOSEOGTIECILADIASTIEKILGNIHTEMOSDRAEHEVISPAHREPGNOSTAHTWONKUOYTAERUOYTAHWREDNOWIWOHTABELTTILELKNIWTELKNIWT'

## Scenario 3: Road Trip!

#### You are going on a long trip. You start on the road at mile marker 0. Along the way, there are n hotels, at mile markers a1 < a2 <...<an, where each ai is measured from the starting point. The only places you are allowed to stop at are at these hotels, but you can choose which of the hotels you stop at. You must stop at the final hotel (at distance an), which is your destination.

#### You'd ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing of the hotels). If you travel x miles during a day, the penalty for that day is (200 - x)2. You want to plan your trip so as to minimize the total penalty - that is, the sum, over all travel days, of the daily penalties. Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.

#### For example, consider hotels at the following locations:
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 175 | 215 | 280 | 400 | 450 | 560 | 640 | 780 | 820 | 1000 | 1060 | 1140 | 1190 | 1260 | 1350 |

#### We want to find out what is the least penalty for a trip from mile post 0 to the hotel #15, at mile post 1350? (And where should you stop to get there?)

#### The solution to this example is penalty = 4050. You should stop at hotels 2, 5, 7, 9, 10, 13, and 15.

## Question 4: Collatz (no coding required)

#### You may remember that we considered the Collatz Conjecture during the AP class last year. This is the one that says that for any positive integer, x, if we repeatedly follow the rule:
##### if x is even, x → x/2; otherwise, x → 3x + 1
##### we will eventually arrive at x == 1, and the "Collatz number" is the number of steps it takes to arrive at 1. 

#### You could probably write a method to determine the Collatz number for a positive integer using a "while" loop. You could also do it with a recursive method. But would a dynamic programming method work even better? Explain why, or why not.


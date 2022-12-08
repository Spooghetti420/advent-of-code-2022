# Advent of Code 2022 Solutions
Here are my solutions to the [Avent of Code 2022](https://adventofcode.com/2022) puzzles. So far we're a week in, and the puzzles are lovely fun and leisurely to boot :) What remains to see is just how fun they're gonna get!
Please don't look at the solutions to any problems you haven't already solved, if only because it would ruin your
own fun of solving them. But of course, if you want to use these if you get stuck, please feel welcome! :)

Merry Christmas!
```
    _\/_
     /\
     /\
    /  \
    /~~\o
   /o   \
  /~~*~~~\
 o/    o \
 /~~~~~~~~\~`
/__*_______\
     ||
   \====/
    \__/
```

## About
What is Advent of Code? It's an annual puzzle gauntlet laid out like an advent calendar, with challenges unlocking
with each day leading up to the 25th, and the goal is to collect all 50 stars. They're unlocked by clearing
the two stages made available on each day: one golden star fruit for beating the first part, and, once the second
has thusly been unlocked, you can get another one by beating the second part of the problem.
This year, it's said that the elves need 50 star fruit to snack on so that they can deliver all the presents. :)

The only problem—that's all the stars there are! So, in order to feed the elves, we'll have to take the plunge and code as hard as we can. I'll be doing my best for the elves this year, and I hope you will as well!
Good luck to any fellow challengers. I don't know quite how complex of solutions lie in wait of us, but I'm ready at
any rate!

## Log
Here I'll keep track of all the days of the calendar until the very end. Stay tuned.

### Day 1
Today was quite nice. We were asked to inspect a list of calorie data, laid out in a text file,
with each elf in the group reporting every food item in their inventory by number of calories.
Each elf's inventory was then separated from the others by a newline; we then needed to add up each elf's totals
and find (in part 1) the #1 amount of calories that any elf has, and then in part 2, the top 3 amounts.
It turns out that everyone's input data is different, so we can't all share the same answers. :')
I must confess, I've thought of a much more elegant solution only after the fact, but this one's good enough...!

### Day 2
The elves have started a rock-paper-scissors tournament, and one kind-hearted, prophetic soul passed us a sheet
that contained all of our opponents' future moves, along with what responses to play to avoid looking suspicious
in winning all the time. In part 1, we just had to calculate what score we would get by playing according to plan,
with +6 points for a win, +3 for a draw, 0 for a loss; and 1, 2, and 3 points for rock, paper, and scissors.
Then, in part 2, it's the same, but instead of X, Y, Z representing our response to play (against A, B, or C),
they now represent whether to Lose, Draw, or Win that round. I did both of these with a not-so-tidy dictionary,
but I'm sure there's a better way...
Oh, and I shortened my response from day 1. It's probably harder to read now, but the logic is much more organised.

### Day 3
Phew, this one was rather more complicated than the others, and it took a while to read and figure it out,
but as always, the explanations from the gentleman running the Calendar are superb, plus the examples helped so much.

Today's puzzle was carried by the set, because sets allowed all the common elements of two groups, for example, to
be easily calculated. We had to find (in part 1) which element was duplicated across two halves of a row of items
(the two compartments of a rucksack), and then (in part 2) which item was used as a badge for each group of 3.

For both of them, the lovely set brought it home for us. I just calculated the intersection of the two halves
for part 1, and then the intersection of the three elves' inventories for each group of 3 for part 2.

The "priority" system number to every letter in the alphabet, but this part was nicely easy. a=1, b=2, ... A=27, ... Z=52.

### Day 4
My dear enemies, this is a declaration of war! I've uncorked the heinous & wicked sauce, the dreaded and maligned,
the iniquitous, object-oriented programming! May God curse my wretched soul, for I have objectified the sublime elves
in solving today's problem. In addition, I also declare to all rivals: my routine has adjusted to the toils of code,
and I am adopting the Amish grind of early rising to get to the W first. Mind: I've set a precedent of waking up
no later than 5:30 in order to read in peace, so this is no idle threat!!

I hope you can forgive my slightly violent tendencies today... anyway, as to the solution. The question was to find
how many elves' clean-up work overlapped with each other. Basically, their work was divided into regions (1, 2, 3),
etc., and was represented as a string like `2-4,6-8`, representing a pairing of elves: here, the first would clean up 
regions 2, 3, and 4, and the second—6, 7, and 8. Part (i) was to find the number of pairs that were totally overlapping
with one another, i.e. one was contained within the other (or they were the same). Part (ii), then, was to get the
number of overlaps at all. These both just needed us to think about what the overlap meant in each case, and so I
translated both cases into just 2 if-statements. I hope you can understand the comments that I wrote for each one...!
Sorry if they're rather poorly explained, though...

### Day 5
Well, gee.. that was suddenly a rather large spike...! Yes, the difficulty went way up today, but I still managed.
The data was in a _very_ awkward format, and so I ended up making several helper functions for just that.
But let's talk concrete stuff here: the puzzle was about moving crates, given a large pile to start with,
and some instructions about "how many crates to move, from which pile, and where to". First, we needed to read in
the piles of crates (I did it in a bunch of lists), and then process all the instructions as asked of us.
This was all rather complicated, so I did almost all of the work in just two functions: `load_crates`, and `move_crate`,
which I later had to split into `move_crate_9000` and `move_crate 9001`...
Anyway, the load_crates function would load in the data as a list of lists (each sublist is a pile of crates, i.e. just single-letter strings), as well as give back the instructions as a list of "Move" objects that I created;
they are just to store the parameters of the move instructions, like where to move stuff from and where to.
The move_crate function would then move crates, according to one instruction at a time. Finally, I made a function
to build up the string that represents the top of each pile, which is the answer format they were going for today.
Doesn't the main code look quite pretty?
Only 4 lines to summarise 95! :')

### Day 6
Cool, this was a fun one. I naturally woke up 5 minutes before the release, and I managed to complete the puzzle
within only 7 minutes! But... even still, that effort was only good enough for #3953 worldwide. Ahhh, the struggle!

Well, anyway, the puzzle was lovely today. The input data was much lovelier than yesterday's, since it consisted of
just a single stream of alphabetic characters, apparently all lowercase too. The elves needed to find two message
headers: a "start-of-packet" marker, and a "start-of-message" marker; the first is a sequence of 4 unique characters,
whereas the second is 14 unique characters. At first, I was quite worried of how to solve this, but fortunately,
once again most of the work was kindly burdened by the set. I kept a running counter that run from 0 to the end,
extracting substrings of length 4 (and/or 14), and then asked: is the set of characters in this substring
of length 4 / 14? If so, we return, if not, the loop continues.
Luckily, this is pretty much it. I just called the function to do this, once with the parameter 4, and once with 14,
and the problem is solved. All in all, much easier than yesterday, somehow...!

Thus, the world continues to turn, without my having earnt a single global star... ;-;

### Day 7
Oh my, today's puzzle took me a while... About 1h30m for this one! And, I'm sorry to say, my code for this one is no
sight for sore eyes. I know mine are sore, and my solution is certainly no good to behold. But, we got it done, which
is what matters :)

The question today was an interesting one, with a file-system-like prompt, making us reconstruct a file hierarchy
using a series of command outputs from `ls` and `cd`. Well, that part was alright (a number of bugs ensued, but were
squashed); but the _next_ part! What woes it gave me, because I could only see one way to solve the problem, using
recursion, and I kept making some silly mistakes... All we needed to do was sum the sizes of the directories of
less than a certain size, for part i, and then find the smallest directory we can delete to free up space for the
new update for part ii.
Tragically, this took such a long time that I can't say I'm proud of my standings for today... That said,
the problem was a toilsome mental exercise as ever, for which I'm very grateful!

### Day 8
Things are definitely getting harder, but at least I can say I enjoyed today's puzzle a good bit.
The trouble this time was my stubbornness is writing any good code, and I tried to write all of it in
effectively one massive for-loop, with more nested for-loops... when I finally went and tried to refactor it,
it worked! Who'da thunk?

And so we come to today's description... it was about a bunch of trees in a forest,
where each tree is represented by a digit (0-9) for its height. Then, we needed to find all trees which are
visible from the outside of the forest, i.e. they were taller than the other trees around them in at least
one direction. (This part got me, which is why I needed the rewrite.) Once that had been done, we needed to calculate
the "scenic score" of a tree, which was the _product_ of all the numbers of trees in each direction around it that
it is visible from. It's a little complicated, but the [page for today](https://adventofcode.com/2022/day/8#part2) describes it quite well...

The problem was solved with just a few loops, really. I couldn't say it's awfully perfect, but it's honest work :P
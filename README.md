# Advent of Code 2022 Solutions
Here are my solutions to the [Avent of Code 2022](https://adventofcode.com/2022) puzzles. So far we're a good 13 days in, and the puzzles are lovely fun ~~and leisurely to boot~~ (Well, I can't deny that they're fun, but they've certainly gotten rather hard of late!) :) What remains to see is just how fun they're still gonna get!
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

### Day 9
Alrighty, it was another nice one today, although I really must've spent a good deal longer on this one than
I ought to have. Today's puzzle was about a rope, with a "head" and a "tail", where the head is moved manually,
and the tail is assumed to follow according to some rules. In the first part, there was only one tail,
and we just had to track how many squares it ever landed on, whereas for the second part, there were 9 tails,
each of which attached to the first, and we had to track the squares that only the very end of the tail ever landed on.
This time around I'm please with my solution :) (if anything because I didn't overkill it with classes!)!

At any rate, a fine one it was today, and I'm glad the Expedition is advancing on its way. We reach the double-digits
tomorrow...!

### Day 10
Good stuff, today's puzzle was about CPU instructions and cycles, with luckily only 2 instructions to have to
simulate, `noop` and `addx` (which adds something to the single x-register). The first asks us to multiply
some different values together, and the second part to render an image by treating the x-register as the position
of a 3-wide sprite. If the CRT (cathode-ray-tube) is current scanning a part of the screen where the sprite resides,
we draw a #, else we draw a dot. The advent of the double digits came with a gentle foot off the gas, which I must
give thanks for!

### Day 11
Wow, today's problem involved quite a lot of data: it was about monkeys who had stolen our goods and were now
merrily throwing them around between themselves. Their throwing was based on how worried we are about the items
they're holding, and the challenge was to figure out how many times each monkey would pass an item to the others
across 20 turns of throwing. With each round, our "worry level" for each item tended to go upwards, but for part
one, this was no concern and we could easily just coutnt the monkeys' throw counts based on a simulation of their
throws. The worry levels were tamped down as well by the fact that they were divided by 3 at each iteration.

BUT, in part 2, there was suddenly a rather more monstrous problem than has been seen in previous parts:
the number of rounds would go up to 10,000 instead of 20, and the division-by-3 constrain would be revoked,
leaving us with gargantuan numbers so gruesomely large, they wouldn't compute for hours on my computer. (NB: I did not actually try this ;) ) Each monkey would determine which other monkey to pass to depending on a fixed and unique number
for each monkey: a modulus, e.g. 17, 23, etc., and for each item: if the item's worry level is divisible by the modulus,
it gets passed to monkey A, otherwise to monkey B (A and B are arbitrary other monkeys).

Here's where the cruelty begins, though: we have to figure out a solution ourselves! Up until now, amendments to the
problem have always been constructive, where we were effectively told what to do and just had to give it a go.
But now, there was no hint at all as to what to do, besides that it was apparently doable...
I'd like to share my idea for this part...! The essence is that if any of the worry-values are divisible by 23, 17,
etc., then they will still be divisible even if we modulo by 23*17\*... etc.
So, at the beginning the process was to calculate the LCM (lowest common multiple) of the monkeys' moduli,
and then modulo by that whenever a monkey wanted to pass it on. I at first was struggling with other modulo-based
approaches that didn't really make much sense, like modding by each respective monkey's modulus before passing on,
etc., and it was horribly thought-wracking to arrive at this final conclusion...

All in all, this part marks the hardest difficulty transition I think we've seen this year, and I'm guessing
this won't be a one-off. Please prepare for further mind-boggling in future instalments!

### Day 12
Yayy! Got a decent outcome on this one, and it wasn't awfully painstaking... only a little embarrassed at how long it
took me to make a 2D list... But anyway, today's problem involved a mountainous terrain, which we needed to scale.
We could only move up 1 unit of height at a time, though, and the problem was to find the shortest path.
Well, well, well! What do we know about the shortest path? Dijkstra's algorithm or its vaguely more advanced analogue, A* are perfect candidates for finding the path, as long as we generate the right graph for them to work on.
I can hardly do well to explain these algorithms, but they basically compute the shortest path from a starting point to
an ending point, given that each each point they know what neighbours a point has. To find this out, I just checked
for each point on the mountain, for all four of its principal neighbours, whether they're not too steep (at most, 
1 tile higher), and if not, then that's a neighbour :)

With the neighbours for each node properly accounted for, I now needed a distance function; luckily, since we know
the position of each point on the grid, this can be calculated as the difference in x- and y-coordinates of the
points (using Pythagoras' theorem). I use A* with both the distance and heuristic functions as a straight-up
Euclidean distance between two points. All the setup now out of the way, I just run the program on the huge map,
with the known start and end, and got my answer!

Finally, the next step was to find the shortest path from ANY point with height 1 (the lowest possible height on the
mountain) to the end. If I'm not mistaken, there's a cleverer way to manage this by performing Dijkstra's algorithm
only twice, but the simpler-to-understand method is just to calculate it 2500 times for each possible candidate :'P
Sometimes, it's not even possible to reach the end, in which case my algorithm throws an error; but, if so, I just
ignore it and move on. This inexcusable inelegance is certainly a visual & conceptual blight on my program,
but oh well... For each cell with height 1, I calculate the shortest distance using A*. I then just track the lowest
of these over the course of the loop. And so we're done!

### Day 13
Here we had a problem to do with "packets", a.k.a. lists with either more lists or integers inside them.
We had to create a new function to tell whether two packets are ordered, and then find out which pairs of packets
are ordered within the input, in order to interpret the elves' distress signal!
There was a fairly simple algorithm to do here, but unfortunately, for lack of reading, I was unable to figure out
the bugs in my code for a considerable while... at least when that was done, our next easy task was to use this
function just to sort all the packets in order, which went very smoothly since a bubble sort ;) did the trick nicely.

I went about it with a recursive algorithm, but I'm sure it could've been cleaner than this. Anyway, I'm happy there
wasn't much code to write today. :P

### Day 14
I ought to keep this one short, since I'm so late posting this it's infringing on my arrangements...! Today's
puzzle was like those mobile games that let you play with sand: we simulate falling sand grains with solid surfaces,
kind of using a cellular automaton sort of simulation. I personally kept a grid which represented the state of each
square; the input data informed which cells became walls, and then the course of the simulation determines which
cells become occupied by sand. In part 1, there was no floor, so eventually the particles would drop out into the
abyss, and we had to determine when this would happen; I just repeatedly updated a particle until it fell way below the bottom of the 2D grid I was using, and then read off the number of iterations that had run; similarly, for part
2, we had to track how many turns it took for the sand (with the sandbox now having a floor) to clog up the
sand-spawning hole.

I saw an interesting solution on YouTube which featured solid tiles as part of a `set`, and sand was repeeatedly
simulated one grain at a time until it found a place to solidify before being added to the set of solid tiles.
The coordinates of each solid tile were represented in the set, so at each loop the current grain of sand could use
these known coordinates to compare against the locations it wished to move to at each update.
This was quite a clean solution, but it didn't much occur to me. I thought it would be too slow and hard to work
in case part 2 required a harder simulation than just solid and vacant... but I really ought to learn they don't
bump it up quite so much in difficulty between parts as that...
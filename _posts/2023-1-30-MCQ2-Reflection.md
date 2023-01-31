---
toc: true
layout: post
description: Reflection from Collegeboard MCQ \#2
categories: [T1, Notes, Week 3, markdown, post]
title: Collegeboard MCQ \#2 Reflections
author: Evan Aparri
show_tags: true
comments: true
---
# MCQ Test #2 Results and Reflection
> Results: 45/50

## Corrections

**Q8: Laptop being borrowed from a school library**
![]({{site.baseurl}}/images/q8-mcq2.png)
I didn't read that two answers should have been chosen, so I ended up choosing only one option. D is another correct option because if a laptop hasn't been returned, the value of borrows and returns is not equal, so it would display an odd number. If a laptop is not currently borrowed, the value of borrows and returns would be equal, so it would display an even number.

**Q12: Controlling an elevator in a building**
![]({{site.baseurl}}/images/q12-mcq2.png)
I think I got overwhelmed by the different statements and the Boolean expressions within Boolean expressions. In order for the elevator to move, if `(onFloor1 AND callTo2)` or `(onFloor2 AND callTo1)` is true, then the elevator moves regardless if the other Boolean expression is true or false. The situation when this occurs is if the elevator is on floor one and is called to floor two and also when the elevator is on floor 2 and called to floor 1. It doesn't move when the elevator is on the same floor it is called to.

**Q17: selection equivalent to Boolean expression**
![]({{site.baseurl}}/images/q17-mcq2.png)
C is incorrect because if `val2` was false then in the option I chosen `result` would be true but that is not the case because in the first condition, it was said that if `val1` was not true it would go to the else statement, so `val1` must have been false. But in the given statement, if give the previous statements, `result` would not be able to be true since it needs two trues for an AND Boolean expression to be true. D is correct because it says makes it so that if `val1` is false then `result` is false which matches the given statement. The nested condition also shows that if `val2` was not true then `result` would be true which also matches the given statement.

**Q30: use drawCircle to draw figure on a coordinate grid**
![]({{site.baseurl}}/images/q30-mcq2.png)
Once again I didn't read that two answers should have been chosen, so I ended up choosing only one option. I need to ensure in the future to read how many options should be chosen. B is also a correct option because it starts from the smallest circle, and each time the iteration repeats, its radius and y-value increases by one, which matches the graphed circles given.

**Q50: ASCII character with hexidecimal**
![]({{site.baseurl}}/images/q50-mcq2.png)
I guessed on this question because I forgot how to read hexidecimal. Reviewing and looking it up, this questions is much easier than I thought. Hexidecimal counts from 0-9 then A-F before going onto the next digit, so base 16. So hexidecimal 56 translated to decimal can be found by multiplying 5 by 16 to get 80 then adding 6 to get 86 which corresponds to V on the table.

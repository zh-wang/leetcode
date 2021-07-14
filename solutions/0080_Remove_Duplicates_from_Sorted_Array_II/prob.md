Problem:
Follow up for “Remove Duplicates”: What if duplicates are allowed at most twice?

For example, Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn’t matter what you leave beyond the new length.

Thoughts:
The most straight forward way is to modify the version I solution, adding a flag to indicate if an element has appeared once.

There could be a better solution that is a little simpler in code, but it has the same running complicity of O(n).


Status: published
Author: Ben Chuanlong Du
Date: 2014-01-09 23:40:44
Title: Tips on Pig
Slug: pig-tips
Category: Computer Science
Tags: programming, big data, Pig, Hadoop, tips
Modified: 2019-05-09 23:40:44

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 
## Tips

1. Pig uses `--` (at the beginning of lines) to comment out lines.
	It also support C-style comment, i.e., using `/* ... */`

2. Filter out records that you don't want before you do expensive transformations 
	such as joining, crossing, etc.

3. Pig uses single quotes instead of double quotes for strings.

4. prefer filtering and then joining rather than joining and then filtering

5. Use dot/period to access fields when use aggregation functions,
	otherwise, use double colons (::) to access fileds/columns.
	but this is wierd

6. -p or -param

## Common Mistakes

1. forget to assign relation to a name

2. use lower case of functions

3. use double quotes for strings

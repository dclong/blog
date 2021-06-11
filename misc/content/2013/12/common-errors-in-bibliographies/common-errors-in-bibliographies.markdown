UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2016-07-13 00:09:02
Slug: common-errors-in-bibliographies
Title: Common Errors in Bibliographies
Category: Research
Tags: research, LaTeX, bibliography, error
Modified: 2016-07-13 00:09:02

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 


Adopted from <http://www.ece.ucdavis.edu/~jowens/biberrors.html>.

## First: Issues in text: how to cite properly.

Citations as words: Huge pet peeve: Using citations as words. 
van Leunen: "Brackets are not words. 
A bracketed number is just a pointer, not a word. 
Never, ever, use a bracketed number as if it were the name of an author or a work." (p. 20). 
So instead of "A similar strategy is described in [15]."), 
use instead "A similar strategy is discussed by AuthorOne et al. [15]". 
The way you can get this right in your head is considering a journal 
that does citations as superscripts (like the old Graphics Hardware style). 
It looks really stupid to say "A similar strategy is discussed by 15." 
I don't like this particular style for citation, 
but it does make sure citations aren't used as words.

Citing with LaTeX: When writing citations in LaTeX, do them in this form:

text text text~\cite{Foo:2000:BAR}

The ~ means non-breaking space (which is what you want—
you don't want a linebreak between the text and the citation).

Also, do

\cite{AuthorOne:2000:ABC,AuthorTwo:2002:DEF}

instead of

\cite{AuthorOne:2000:ABC}\cite{AuthorTwo:2002:DEF}.

Always alphabetize grouped citations so they appear in numerical order (instead of [8, 6, 10], 
arrange the citations so it looks like [6, 8, 10]). 
\usepackage{cite} supposedly puts them in proper order for you automatically (!) 
and also changes [1,2,3,4,6] to [1–4,6] which is handy.

Shortcite: Use \shortcite when appropriate. 
\shortcite is used in sentences like "AuthorOne discusses this point 
further in her dissertation [AuthorOne 2002]." 
It looks silly to put AuthorOne's name twice. 
Instead, use \shortcite{AuthorOne:2002:AOT}, 
which makes the sentence "AuthorOne discusses this point further in her dissertation [2002]." 
Of course this only makes sense if you are using a citation format 
that lists author name / year (like Siggraph or most dissertation formats).

I always use \shortcite in my text even when my bib style doesn't support it, 
in which case I use the following fix in my LaTeX preamble (this defines \shortcite if it's not already defined, otherwise it has no effect):

\providecommand{\shortcite}[1]{\cite{#1}}

If you don't have this command, you'll see an error like:

! Undefined control sequence.
l.123 ...blah blah Author1 and Author2~\shortcite {Author1:1999:ABC} blah...

Sorting your references: If at all possible, arrange your reference list in alphabetical order by author's last name. Going in cited order is much less useful to readers of your paper. The only reason I've heard that cited-order is useful is in a survey article where nearby (and presumably related) citations from the paper are next to each other in the bibliography. I don't find this argument particularly compelling.

Next: issues with bibliographies (your .bib file). Big picture: Don't trust the digital library to give you a perfect .bib file. Both ACM and IEEE (as well as many others) screw up bibliography entries in delightfully creative ways.

Names: Make the names in the bibliography match what is printed on the paper. If the paper has First M. Last as the author, put that in your bibliography. If it has initials, use those. If it has crazy umlauts and accents, use those too. If it has initials, make sure they are separated by spaces: use J. D. Owens rather than J.D. Owens. The latter leads bibtex to believe the first name is J.D. with no middle name/initial. (And then if your bibstyle abbreviates first names, you'll just get the initial J. without the middle initial, since bibtex doesn't think you have a middle name.)

For hyphenated names with the second half uncapitalized (Wu-chun Feng, Wen-mei Hwu), put the hyphen and second half in brackets: Wu-{chun} Feng, Wen{-mei} Hwu.

Capitalization in titles: Just like with authors, the capitalization on titles in your bibtex file should match what's on the paper. The bib style should enforce capitalization, not your bibliography—your bib should faithfully represent what's printed on the paper.

Also, make sure, in your BibTeX file, that you properly bracket {} words in titles that must be capitalized, like GPU or PDE, or proper names. Example (the “Loop” should always be capitalized since it's a last name):

@inproceedings{Bischoff:2000:THI,
author = "Stephan Bischoff and Leif P. Kobbelt and Hans-Peter Seidel",
title = "Towards Hardware Implementation Of {L}oop Subdivision",

You don't have to do this with venues (or anything else), just the title.

Resist the temptation to double-brace the entire title as a manner of course: {{Title Title with Title}}. This guarantees your title will always be capitalized. But many bib styles downcase all titles, in which case your title will stick out like a sore thumb. Instead, just put your title in single-braces or quotes and let the bib style do the right thing.

(What is the right thing? In the US, publishers capitalize most words in titles [title case]; in the UK, publishers use the same capitalization rules as normal sentences [sentence case]. [Wikipedia link.] Markus Kuhn's thoughts on the subject are congruent with mine, that sentence case is preferable from an information-theoretic point of view, but in practice, authors should follow the conventions of their publication venue.)

If the title is in all-caps, I usually rewrite it in title case.

[ Capitalisation in BibTeX, from the TeX FAQ ]

Venues: Both ACM and IEEE screw up venue names in different ways. Here's how IEEE formatted a recent venue name in a recent paper of mine:

booktitle={Intelligent Vehicles Symposium (IV), 2011 IEEE},

Never use the ACM or IEEE digital library's citations without fixing them. For some reason the First Society of Computing and the World's Largest Professional Association for the Advancement of Technology have zero interest in making their capitalization correct. For instance, the first paper I ever wrote, according to ACM, has the following title and booktitle:

title = {Polygon rendering on a stream architecture},
booktitle = {HWWS '00: Proceedings of the ACM SIGGRAPH/EUROGRAPHICS workshop on Graphics hardware},

when the paper has the major words in the title capitalized, and “workshop” and “hardware” should both be capitalized in the booktitle. I often review papers where citations have been taken directly from ACM with bizarre capitalization particularly in the booktitle. Fix these before you submit a paper.

Months: Include the month of publication in your bibliographies (simply for your own records: when you have two papers talking about a similar idea, one in January and one in November of the same year, maintaining the month lets you determine which came first.

Always use three-letter abbreviations without quotes for months. These are built into bibtex. They allow the bib style to actually know what month it is, so the bib style can enforce a consistent style across all citations (1/2012? Jan. 2012? January 2012? Januar 2012 [foreign language]?).

month = mar, % most common - single month
month = jun # "\slash " # jul, % two months
month = "18~" # dec % day/month

Digital libraries often get these wrong (IEEE uses month={june}).

Pages: Always include pages if pages are available. Ranges of pages use the en-dash to separate them (that's two dashes): 35--49. Some non-printed proceedings only assign a paper number, so for those I typically see (and use) something like 12:1--12:10, where 12 is the paper number and the paper has 10 pages.

Also, if the bib source says that your paper starts on page 1, double-check it. Make sure that it doesn't list every paper in the conference/journal starting on page 1 (like the rocket scientists at IPDPS 2009 who decided it would be a good idea to assign neither page numbers nor paper IDs [example]). It's a little embarrassing when you cite two papers in your article and they both start on page 1 of the same conference. (Usually, you should figure out the paper number n in the conference and use n:1--n:10. If you can't make your page numbers unique, leave them out entirely.)

DOIs: DOIs uniquely identify a paper. Even if your style doesn't use them, you should record them in your bibtex file. Store them as the numbers only (DOIs have the format http://dx.doi.org/numbers/numbers; store the part after http://dx.doi.org/ only). Bibliography tools seem to use this format predominantly.

URLs: If you're putting a URL into your bibliography, wrap it in \url{} (and put \usepackage{url} in your LaTeX preamble) so it wraps nicely. If you add a DOI with a doi tag, you don't need to add the DOI as url as well.

Let's see where digital libraries get these things wrong! Corrections are in blue.

IEEE:
@INPROCEEDINGS{5940539,
author={Glavtchev, V. and Muyan-Ozcelik, P. and Ota, J.M. and Owens, J.D.},
author = {Vladimir Glavtchev and P{\i}nar Muyan-{\"{O}}z{\c{c}}elik and Jeffery M. Ota and John D. Owens},
booktitle={Intelligent Vehicles Symposium (IV), 2011 IEEE},
booktitle = {Proceedings of the 2011 IEEE Intelligent Vehicles Symposium},
title={Feature-based speed limit sign detection using a graphics processing unit},
title = {Feature-Based Speed Limit Sign Detection Using a Graphics Processing Unit},
year={2011},
month={june},
month=jun,
volume={},
number={},
pages={195 -200},
pages={195--200},
doi={10.1109/IVS.2011.5940539},
ISSN={1931-0587},
}

Problems with IEEE: Did not use the names that were printed on the paper; did not put accents on proper characters; did not separate first initial and middle initial with a space; venue title is strangely wrapped around with the comma; did not capitalize paper title as it was on the paper; did not use bibtex month abbreviations; did not use en-dash to separate out page numbers.

ACM:
@inproceedings{Davidson:2011:RPC:1964179.1964185,
author = {Davidson, Andrew and Owens, John D.},
title = {Register packing for cyclic reduction: a case study},
title = {Register Packing for Cyclic Reduction: A Case Study},
booktitle = {Proceedings of the Fourth Workshop on General Purpose Processing on Graphics Processing Units},
series = {GPGPU-4},
year = {2011},
isbn = {978-1-4503-0569-3},
location = {Newport Beach, California},
pages = {4:1--4:6},
articleno = {4},
numpages = {6},
url = {http://doi.acm.org/10.1145/1964179.1964185},
doi = {http://doi.acm.org/10.1145/1964179.1964185},
doi = {10.1145/1964179.1964185},
acmid = {1964185},
publisher = {ACM},
address = {New York, NY, USA},
}

Problems with ACM: Did not capitalize paper title as it was on the paper; added a URL that's redundant with the DOI; did not store DOI as numbers only. Notable: On this paper, ACM got the venue capitalization correct!

Also see Dan Wallach's thoughts on the matter.

John Owens | Last updated 08/11/2013 22:39:14.


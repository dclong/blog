UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-11-13 00:02:08
Slug: convert-latex-to-word
Author: Ben Chuanlong Du
Title: Convert LaTeX to Word
Category: Software
Tags: html, LaTeX, Office, software, Word
Modified: 2016-07-13 00:02:08

`pandoc` is a general purpose tool for converting between different type of documents, 
however, 
it is not good at converting LaTeX code to word.
`tex4ht` is a better tool for converting LaTeX code to word. 
The following are instructions to use `tex4ht` to convert LaTeX to word.

1. Compile your LaTeX code. 
Make sure that there are no error messages. 
Do not remove the temporary files produced when compiling your LaTeX code, 
as they are required by the `tex4ht` command. 

2. Convert your LaTeX code to html document using the following command.

        mk4ht mzlatex you_latex_doc.tex

3. Open the html document using office tools (Microsoft Word, LibreOffice Writer, AbiWord, etc).

4. Save a copy of the html document to the right format you want. 

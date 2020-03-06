Status: published
Date: 2020-01-07 10:00:53
Author: Benjamin Du
Title: Extracting PDF pages using the Python Package PyPDF2
Slug: python-pdf-pypdf2
Category: Computer Science
Tags: programming, Python, PyPDF2, PyPDF, example, PDF, extract pages


The Python package PyPDF2 can be used to extract pages from a PDF file.
The function `extract_pages` below is a wrapper over PyPDF2 
which makes it even easier to extract pages from a PDF file.

    :::python
    def extract_pages(file: str, subfiles: Mapping[str, Sequence[int]]) -> None:
        """Extract pages from a PDF file and write into sub PDF file.
        :param file: The raw PDF file to extract pages from.
        :param subfiles: A dictionary specifying sub PDF files 
        and the corresponding list of pages from the raw PDF file.
        """
        fin = open(file, 'rb')
        reader = PdfFileReader(fin)
        for file, indexes in subfiles.items():
            _extract_pages(reader, indexes, file)
        fin.close()


    def _extract_pages(
        reader: PdfFileReader, indexes: Sequence[int], output: str
    ) -> None:
        """A helper function for extract_pages.
        :param reader: A PdfFileReader object.
        :param indexes: Index (0-based) of pages to extract.
        :param output: The path of the sub PDF file to write the extracted pages to.
        """
        writer = PdfFileWriter()
        for index in indexes:
            writer.addPage(reader.getPage(index))
        with open(output, 'wb') as fout:
            writer.write(fout)

Below is a concrete example of using the function `extract_pages`
to extract pages from the PDF file`scan.pdf` into 3 sub PDF files 
`tod.pdf` (pages 0-3), `loi.pdf` (page 4) and `cia.pdf` (pages 5-15).

    :::bash
    subfiles = {
      'tod.pdf': range(4),
      'loi.pdf': [4],
      'cia.pdf': range(5, 16)
    }
    extract_pages('scan.pdf', subfiles)

The above functions are included in 
[dsutil.pdf](https://github.com/dclong/dsutil/blob/dev/dsutil/pdf.py).

## References

https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python

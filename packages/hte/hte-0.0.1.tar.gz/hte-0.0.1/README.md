# historical-text-extraction (hte)
Package to extract text from historical documents. The package is written for personal use.


## Installation

The development version from [GitHub](https://github.com/) with:

``` bash
pip install git+ssh://git@github.com/eirikberger/hte.git
```
Note that it is nessecary with a SSH key for this approach to work. 

## Using it

Import the package

``` python
from hte import digitize
```

The basic setup is the following:

``` python
# Define class
book = digitize.Book("data/finnmark_1968.pdf", "books")

# Run methods on the class
book.CreateFolderStructure()
book.PdfImport(page_info=False, from_page=21, to_page=263)
book.Split(multiple_columns=True)
book.RunOCR(type="splits", export_image=False)
book.CombineCleanGroup(ocr_grouping=True, group_type='norway')
book.RegexStructure("norway")
```

Make sure to install the correct language package for Tesseract. 

``` bash
# Check languages already installed: 
tesseract --list-langs

# Languages available for installation
apt-cache search tesseract-ocr

# Install the Norwegian language pack
sudo apt-get install tesseract-ocr-nor
```

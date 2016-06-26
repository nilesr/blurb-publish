# Pdf Reformatter

Takes a dual pdf and turns it into a format acceptable to blurb.com for magazine distribution. 

# Usage

It's as simple as

    pdftocairo -png [yourpdf].pdf
    python3 test2.py
    img2pdf --dpi 156 *-2.png -o final.pdf

Ok so maybe not really.

You must open one of the images and verify its resolution, as well as the dimensions of the smallest image with an aspect ratio of 0.766666667 that could contain it. Put those dimensions in `size` in test2.py

After running test2.py, you need to open one of the images ending in -2.png (or just use the size you found in the last step), and determine the number of pixels per inch needed to make the image 8.625 x 11.25 inches. I recommend a calculator for this one

Finally, just use that dpi with img2pdf to merge the images into the final pdf you're going to upload to blurb. Unfortunately the --dpi option was removed from img2pdf, however if you download and install the last version on github it will still work. To do that

    git clone https://github.com/josch/img2pdf
    cd img2pdf
    git co 06d90eea154629213a529fb0cae3f832d225c0e8 # As of the time of writing, this is the head of master, but just to future-proof everything...
    sudo python3 setup.py install
    cd ..
    rm -rf img2pdf

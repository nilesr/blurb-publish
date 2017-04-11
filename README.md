# Pdf Reformatter

Takes a dual pdf and turns it into a format acceptable to blurb.com for magazine distribution. 

# Usage

It's as simple as

    convert -density 300 [yourfile].pdf [yourfile]-%03d.png
    python3 test2.py
    img2pdf --dpi 156 *-2.png -o final.pdf

Ok so maybe not really.

Pick any "density" to render the pdf at, the general concensus is that you shouldn't print anything at under 300 dpi. 300 dpi looks fine from 10-12 inches away. Larger dpis will take longer and take more ram. I tried one at 600 dpi and it would oom crash until I had loaded 30 gigabytes of swap. I canceled it when it didn't complete in an hour

After exporting as an image, you must open one of the images and verify its resolution, as well as identify the dimensions of the smallest image with an aspect ratio of 0.766666667 that could contain it. Put those dimensions in `size` in test2.py

After running test2.py, you need to open one of the images ending in -2.png (or just use the size you found in the last step), and determine the number of pixels per inch needed to make the image 8.625 x 11.25 inches. I recommend a calculator for this one

Finally, just use that dpi with img2pdf to merge the images into the final pdf you're going to upload to blurb. Unfortunately the --dpi option was removed from img2pdf, however if you download and install the last version on github it will still work. To do that

    git clone https://github.com/josch/img2pdf
    cd img2pdf
    git co 06d90eea154629213a529fb0cae3f832d225c0e8 # As of the time of writing, this is the head of master, but just in case..
    sudo python3 setup.py install
    cd ..
    rm -rf img2pdf

Run your img2pdf command with the corrent dpi, but DOUBLE CHECK THE OUTPUTED PDF! I've had cases where the third page gets transposed to the 20th page, etc... because shell globbing doesn't always work as you expect

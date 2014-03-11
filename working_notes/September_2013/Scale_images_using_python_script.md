 **Scale_images_using_python_script**

* For scaling jpeg image files in bulk, there is a python script from this link

http://united-coders.com/christian-harms/image-resizing-tips-every-coder-should-know/
 
import Image, os, sys
for filename in sys.argv[1:]:
    img = Image.open(filename).resize( (200,200) )
    out = file(os.path.splitext(filename)[0]+"_thumb.jpg", "w")
    try:
        img.save(out, "JPEG")
    finally:
        out.close()

* It is only some 8 lines of code, but doing huge job. Another important think to learn is use of finding and regex to feed the files into python script. This is the find and python feeder code to make the script work on all the files inside a directory.

find . -regex .*jpg | xargs python resize.py


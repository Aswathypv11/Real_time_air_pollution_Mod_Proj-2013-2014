**Adding_font_in_Ubuntu_12.04**
To add font

* move the ttf file into the folder `usr/share/fonts/ttf`
* then remove fonts cache by `rm -f /usr/share/fonts/*fonts.cache-1`
* then create the cache again `sudo fc-cache`
* that's it, added ttf can be seen in all the text editors.

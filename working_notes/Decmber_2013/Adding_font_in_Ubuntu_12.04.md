 **Adding_font_in_Ubuntu_12.04**
To add font
1. move the ttf file into the folder usr/share/fonts/ttf
2. then remove fonts cache by
    rm -f /usr/share/fonts/*fonts.cache-1
3. then create the cache again
    sudo fc-cache

the added ttf can be seen in all the text editors.

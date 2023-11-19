💬 :term:`FAQ`
=============================

After connecting everything and turning on the |Product|, the power :term:`LED` doesn't turn on, why?
    The power :term:`LED` has a solderable jumper, this means that unless you applied some soldering lead on the pads it won't be enabled.
    This is done for avoiding unnecesary standby :term:`LED`s powered on all the time.

    However, if you soldered the jumper, the board is connected correctly and you cannot see the power :term:`LED` on, disconnect the power immediately.
    Please check all the connections and measured with a multi-meter the resistance between 3V3 and :term:`gnd` in any port (:math:`I^2C` or Serial).
    If the resistance is close to zero you have a short circuit somewhere in your board, please check your connections and any soldering you've made
    If the problem persist reach :ref:`support`

Can I upload ESPHome directly from the Home Assistance setup running on my Raspberry Pi?
    Yes you can, and actually this is one of the simplest and more effective way to upload ESPHome.

Can I upload firmware through the USB-C?
    Yes, the ESP32-S2 includes a full-speed USB On-The-Go (OTG) interface to enable USB communication.

Can I upload firmware through the Serial bus?
    Yes you can, however this is only recommended if you have troubles using the USB port and you are familiar with the procedure.

I want to use the :term:`IIC` port for expanding the possibilities, how can I do it?
    Once you have located the sensor that you want to connect to the :term:`IIC` port, check that is compatible with the 3.3V power supply from the |Product|. 
    If this is the case, just connect it directly, power the board and update the firmware!

When I try to compile the given YAML and upload it into the board I get some error messages saying that I miss some files (Audiowide.ttf, icon-map.h, etc). How to fix it?
    Just the configuration YAML file isn’t enough and you might get an error asking for missing items (the fonts and the images). The reason is because
    on the configuration we are asking for some files (the fonts that you want for the digits or the icons and the background image with the gauge, for example).
    
    Therefore you need to upload into the folder with the configuration YAML file the required files. I strongly suggest to use Visual studio code and just drag and 
    drop the items according to the structure mentioned on the :ref:`esphome` programming section.

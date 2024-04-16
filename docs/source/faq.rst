💬 :term:`FAQ`
=============================

Can I upload ESPHome directly from the Home Assistance setup running on my Raspberry Pi?
    Yes you can, and actually this is one of the simplest and more effective way to upload ESPHome.

Can I upload firmware through the USB-C?
    Yes, the ESP32-S2 includes a full-speed USB On-The-Go (OTG) interface to enable USB communication.

Can I upload firmware through the Serial bus?
    Yes you can, however this is only recommended if you have troubles using the USB port and you are familiar with the procedure.

I have CT clamps that gives me the output in voltage instead of current (100A:1V), is it still compatible?
    Yes, you just have to desolder the burden resistor close to the connector of the channel you want to use. 

Am I obtaining the accurate measure of power consumption?
    Strictly speaking, no; what you're obtaining is the **apparent** power. The real or true power of a circuit considers the phase (power factor). 
    As we are solely monitoring the current and assuming a constant voltage, we cannot factor in the phase shift between voltage and current. 
    Consequently, what we can calculate is the apparent power. Nevertheless, unless you have robust inductive loads at home, such as powerful motors, 
    the power factor tends to be close to unity, resulting in a very close alignment between the measurement of apparent power and real power.
    If you want to understand more about the differences between True, Apparent and Reactive power have a look at this `article <https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/>`_ 

I want to use the :term:`IIC` port for expanding the possibilities, how can I do it?
    Once you have located the sensor that you want to connect to the :term:`IIC` port, check that is compatible with the 3.3V power supply from the |Product|. 
    If this is the case, just connect it directly, power the board and update the firmware!

When I try to compile the given YAML and upload it into the board I get some error messages saying that I miss some files (Audiowide.ttf, icon-map.h, etc). How to fix it?
    Just the configuration YAML file isn’t enough and you might get an error asking for missing items (the fonts and the images). The reason is because
    on the configuration we are asking for some files (the fonts that you want for the digits or the icons and the background image with the gauge, for example).
    
    Therefore you need to upload into the folder with the configuration YAML file the required files. I strongly suggest to use Visual studio code and just drag and 
    drop the items according to the structure mentioned on the :ref:`esphome` programming section.

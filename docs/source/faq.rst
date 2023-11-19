💬 :term:`FAQ`
=============================

Can I upload ESPHome directly from the Home Assistance setup running on my Raspberry Pi?
    Yes you can, and actually this is one of the simplest and more effective way to upload ESPHome.

Can I upload firmware through the USB-C?
    Yes, the ESP32-S2 includes a full-speed USB On-The-Go (OTG) interface to enable USB communication.

Can I upload firmware through the Serial bus?
    Yes you can, however this is only recommended if you have troubles using the USB port and you are familiar with the procedure.

The readings from the CT clamps are very noisy and doesn't make any sense.
    Make sure the jack connectors are correctly plugged in. If the measurement is still noisy check other CT clamps in that same channel. 

I have CT clamps that gives me the output in voltage instead of current (100A:1V), is it still compatible?
    Yes, you just have to desolder the burden resistor close to the connector of the channel you want to use. 

Am I getting the real power consumption?
    Strictly talking no, you are getting the **aparent power**. The real (or true) power of a circuit, takes into account the phase (power factor). Since 
    we are only monitoring the current, and assuming a constant voltage, we cannot take into account the offset between voltage-current, and 
    therefore what we can compute is the aparent power. 
    However, and unless you have powerfull inductive loads at home (powerfull motors), the power factor will be close to the unity, making very close
    the measurement of the apparent power to the real power.
    If you want to understand more about the differences between True, Apparent and Reactive power have a look at this `article <https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/>`_ 

I want to use the :term:`IIC` port for expanding the possibilities, how can I do it?
    Once you have located the sensor that you want to connect to the :term:`IIC` port, check that is compatible with the 3.3V power supply from the |Product|. 
    If this is the case, just connect it directly, power the board and update the firmware!

When I try to compile the given YAML and upload it into the board I get some error messages saying that I miss some files (Audiowide.ttf, icon-map.h, etc). How to fix it?
    Just the configuration YAML file isn’t enough and you might get an error asking for missing items (the fonts and the images). The reason is because
    on the configuration we are asking for some files (the fonts that you want for the digits or the icons and the background image with the gauge, for example).
    
    Therefore you need to upload into the folder with the configuration YAML file the required files. I strongly suggest to use Visual studio code and just drag and 
    drop the items according to the structure mentioned on the :ref:`esphome` programming section.

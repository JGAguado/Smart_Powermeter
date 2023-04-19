:term:`FAQ`
=============================

After connecting everything and turning on the |Product|, the power :term:`LED` doesn't turn on, why?
    If the board is connected correctly and you cannot see the power :term:`LED` on, disconnect the power immediately.
    Please check all the connections and measured with a multi-meter the resistance between 3V3 and :term:`gnd` in any port (:math:`I^2C` or Serial).
    If the resistance is close to zero you have a short circuit somewhere in your board, please check your connections and any soldering you've made
    If the problem persist reach :ref:`support`

Can I upload ESPHome directly from the Home Assistance setup running on my Raspberry Pi?
    Yes you can, and actually this is one of the simplest and more effective way to upload ESPHome.

Can I upload firmware through the Serial bus?
    Yes you can, however this is only recommended if you have troubles using the USB port and you are familiar with the procedure.

I want to use the :term:`IIC` port for expanding the possibilities, how can I do it?
    Once you have located the sensor that you want to connect to the :term:`IIC` port, check that is compatible with the 3.3V power supply from the |Product|. 
    If this is the case, just connect it directly, power the board and update the firmware!

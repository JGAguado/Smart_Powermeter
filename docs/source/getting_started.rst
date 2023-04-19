Getting started
===============

Soldering 
----------
.. Important::
    Please note that some components in this board need to be soldered.

If you have never soldered or you want to improve your soldering techniques I recommend you 
the `Adafruit Guide To Excellent Soldering <https://learn.adafruit.com/adafruit-guide-excellent-soldering>`_

For better understanding where is located each component on the board check out the :ref:`pcb` layout 
with the interactive :term:`BOM`.

Powering
--------
The |Product| can be powered in two ways: through the USB-C (only for programming and testing purposes) **or** through the AC Input, but not simultaneously. 

.. Caution::
    Power the board only after making all the connections


AC Input
^^^^^^^^^^^^^
If your preffer not to use external power suplies you can mount the `HLK-2M05 Series <https://www.hlktech.com/en/Goods-39.html>`_, a 2W AC-DC step-down 
switching power supply module, ready to receive the 220V and deliver 5V (later on lowered to 3V3 for the ESP32 module)

.. Danger::
    If your are using the AC power **never touch the board while is powered**. 


I/O
-----------
The |Product| supports up to 6 independent *analog inputs* ready to read CT clamps (or probes):

.. _pinout:

.. list-table:: Pinout table
    :widths: 10 10 10 20
    :header-rows: 1

    * - GPIO
      - Input
      - Output
      - Name
    * - 1
      - ✅
      - ❌
      - Probe 0
    * - 2
      - ✅
      - ❌
      - Probe 1
    * - 3
      - ✅
      - ❌
      - Probe 2
    * - 4
      - ✅
      - ❌
      - Probe 3
    * - 5
      - ❌
      - ✅
      - Probe 4
    * - 6
      - ❌
      - ✅
      - Probe 5



Communications
-----------
In addition to the analog input mentioned before, there is also a direct connection to:

:term:`IIC` (:math:`I^2C`) bus:
^^^^^^^^
:SDA: *GPIO33*
:SCL: *GPIO34*

Serial bus:
^^^^^^^^^^^
:Tx: *TXD0*
:Rx: *RXD0*

Enclosure
---------
The |Product| has been designed to fit in the electronics enclosure LK-PLC01,
compatible with DIN rails and screws, and it is recommended for indoors only.

.. figure:: ../../Documentation/Images/SL_X4_1.png
    :align: center
    :figwidth: 300px

:External size: 115x90x40mm
:Material: ABS Plastic
:Color: Transparent cover, black or beige base
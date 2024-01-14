🏗️ Assembly
============================

Soldering 
----------
.. Important::
    Please note that some components in this board need to be soldered.

The |Product| comes as a set consisting on a :term:`SMD` pre-soldered board to which you will need to mount the following components:

* `HLK-2M05 <https://www.hlktech.com/en/Goods-39.html>`_ power module, a 2W AC-DC step-down switching power supply module :term:`THT` solderable.
* A 2-Pin 2mm-pitch screw terminal block, for the AC power imput, also :term:`THT` solderable.

.. Note:: 
  When buying the |Product| read the product description to make sure these two components are included, otherwise you might need to get them on your
  own.

.. figure:: images/getting_started/soldering.jpg
    :align: center
    :figwidth: 300px 

The soldering of these two components is quite fast, just make sure not to bend any of the power supply module pins. If you have never soldered or you want to improve your soldering techniques I recommend you 
the `Adafruit Guide To Excellent Soldering <https://learn.adafruit.com/adafruit-guide-excellent-soldering>`_

Assembly
--------
Once the board is fully soldered, it's time to mount the e-paper display (in case you are using this accessory to display real-time information):

1. Open the clamp connector, by smoothly pulling up the tab.
2. Introduce the e-paper :term:`FPC` with the exposed pads facing down (against the PCB)
3. Close the clamp connector
4. Bend carefully the e-paper's :term:`FPC` in a way that the panel rests over the PCB. Add a very small piece of double-side tape on the rear to fix it.

.. image:: images/getting_started/e-paper.jpg
    :width: 100%

Last but not least, it is highly recommended to mount the |Product| on an enclosure (like the suggested :ref:`enclosure`) to prevent unintended contacts between the bottom 
side of the board (since the hig-voltage pins are exposed).
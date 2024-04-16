Smart Powermeter
###############

.. raw:: html
        
    <iframe src="_static/carousel.html" style="width: 100%; height: 300px; border: none;"></iframe>


Welcome to the documentation page of the |Product|, an electronic board based on the ESP32 with 
the target of monitoring the real-time consumption of AC sources.

It can be powered from a :math:`220 V_{AC}` source so it can be mounted on the electric cabinet in order to monitor your home electric consumption.

In addition it can support 2.9" black and white e-paper display, in order to 
provide graphic information about the measured consumption, as well as spent money or any info you want to show.


Change log
-----------

Applied changes with respect to previous release (V2R1):

- ✅ **Resistors replacement**. R3,6,9,12,15 10kOhm with 15kOhm for improving the current measured range.

- ✅ **Cuttable/solderable jumpers**. Allowing the disconnection of the burden resistor, connected by default.

- ✅ **Jack connectors replacement**: :term:`SMD` parts replaced with :term:`THT` for improved mechanical strenght. T&S instead of RRS (with solderable jumper for an optional RRS)

- ✅ **LED indicators**: Added two :term:`LED` indicators: Power and GPIO08. The power :term:`LED` indicator has a cuttable jumper. 


Contents
--------

:doc:`safety`
    How to operate and manipulate the |Product|.

:doc:`details`
    A deeper explanation on the systems of the |Product|.

:doc:`getting_started`
    First steps for configuring and working with the |Product|.

:doc:`design`
    Design files of the |Product|.

.. _support:

Technical support
-----------------

If you have technical problems or cannot find the information that you need in the provided documentation, 
please contact me directly:

:Author: |Author|
:Contact: |Email|

:Board: |Product|
:Version: |Version|
:Release: |Release|
:Date: |Date|


.. toctree::
   :maxdepth: 3
   :hidden:

   safety   
   details
   getting_started
   design   
   glossary
   faq 

💻 Programming
===============


There are two main programming methods supported and tested with the |Product|: 

 * ESPHome
 * Arduino

In both scenarios, and if you are using the USB port or the Serial port for programming it, you
will first need to enter the board into flashing mode: press and hold the *Flash* pushbutton
while you reset the board (pressing once the *Reset* pushbutton).

.. Caution::
    When flashing the board, make sure its only powered by the USB/Serial port.
    
ESPHome
---------
`ESPHome <https://esphome.io>`_ is a well known platform for programming ESP-based devices 
with a very little effort. It is configured via YAML files and supports a wide range of functionalities
and sensors.

.. Important::
    For using ESPHome, and all its funcionalities, you need to have a `Home Assistant <https://www.home-assistant.io>`_ instance running
    in the same network as your |Product|.

    
The |Product| comes raw, without any firmware by default, therefore, you will need to flash it for first time. There are many ways to flash 
your ESPHome device (`locally <https://esphome.io/guides/getting_started_command_line.html>`_, `ESPHome Web <https://web.esphome.io>`_), but 
the one I strongly recommend is the one through the `ESPHome Add-on for Home Assistant <https://esphome.io/guides/getting_started_hassio.html>`_:


1. Make sure your ESPHome Add-on for HA is up to date and working. 
2. Add a new device, enter the name you want (like *Smart-Powermeter*), and skip the next step.
3. Select the *ESP32-S2* as the device type, skip the last step (installation). You will have created a provisional first configuration YAML file.

.. figure:: images/getting_started/esphome_1.png
    :align: center
    :figwidth: 400px

4. Open the recently created file and replace the content with the example configuration ``smart-powermeter.yaml``

.. Note:: You might need to keep the encription keys *OTA* and *API*

.. literalinclude:: files/configuration.yaml
   :language: yaml
   :linenos:


    
.. Note::
    ``Gauge.png`` and ``Gauge.png`` are some customized gauges to be plotted as part of the background. You can download them to your local path, or just invoke the url as in the *.yaml* example.

        .. image:: images/getting_started/Gauge.png
            :width: 40px   
        .. image:: images/getting_started/Gauge_1.png
            :width: 80px



5. Click on install, make sure that the the board is connected via the USB-C (and that it is into flashing mode, see up in this guide) to the device running the Home Assistant (in my case a Raspberry Pi) before selecting the mode of installation.

.. figure:: images/getting_started/esphome_2.png
    :align: center
    :figwidth: 400px

6. Select the Serial port and let it run, it might take some minutes. 
7. Once it's done, you will have to exit the flashing mode: press the *Reset* pushbutton once. 

Now, your ESPHome-based |Product| should be ready to log data and stream it to your Home Assistant. Note that the current configuration is just an example and you can customize it at your will, including the calibration. 


.. Tip::
    A very easy way to upload and copy files (code or even images) into your ESPHome folder hosted in your HA instance is 
    with the help of the Visual Studio Code integration for HA. This way you can just drag and drop the files over the folder 
    on the Home Assistant’s Visual Studio Code navigation panel on your left.


Flash Tools
^^^^^^^^^^^^
If you want to deploy an ESPHome already compiled *.bin* image, you can use Espressif's official `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_ to upload it into your Smart Powermeter. 
As an example (and test) you can use this :download:`smart-powermeter-offline.bin <files/smart-powermeter-offline.bin>` image with the address `0x0`, make sure `DoNotChgBin` is checked:

.. image:: images/getting_started/Flash_tool.png
    :width: 30%

.. Note:: Make sure that the checkbox close to the filepath is also checked!

Arduino
--------
If you are still interested in programming directly with the Arduino IDE, the procedure is no 
different than with any other ESP32 devices:

1. Open the Arduino IDE and go to File -> Preferences option.
2. Add to the *Additional Boards Manager URSLs* the url:

.. parsed-literal::

    https://dl.espressif.com/dl/package_esp32_index.json

3. Close the preferences and open in the menu Tools -> Board -> Boards Manager.
4. Search for *esp32* and install it. This might take some time.
5. Now you can select the board *ESP32S2 Dev Module* as the target board. Leave the rest of parameters 
   by default.
6. Select the correct port and remember to enter the board into flashing mode before uploading the sketch.


# Smart-WiFi-Scocket
Project Overview
The Smart WiFi Socket is a WiFi-operated device that allows you to control any electronic device plugged into it from anywhere using an internet connection. This project utilizes the ESP8266 microcontroller, a relay module, a switchboard socket, and a 5V power supply. The control is facilitated through the Blynk IoT mobile application, providing a user-friendly interface for remote management.

Features
Remote Control: Operate your electronic devices from anywhere using the Blynk app.
User-Friendly Interface: Simple on/off button control through the Blynk app.
Easy Setup: Quick and easy installation process with detailed guidance.
Compatibility: Works with a variety of electronic devices.

Components Used
ESP8266: A WiFi microcontroller that enables internet connectivity.
Relay Module: Controls the power supply to the connected device.
Switch Board Socket: The socket into which the device is plugged.
5V Power Supply: Powers the ESP8266.

Getting Started
Prerequisites
ESP8266 module
Relay module
Switchboard socket
5V power supply
Blynk IoT app installed on your mobile device
Basic knowledge of electronics and programming

Installation
Assemble the Components:
Connect the relay module to the ESP8266.
Wire the switchboard socket to the relay module.
Power the ESP8266 using the 5V supply.

Set Up Blynk App:
Download and install the Blynk app from the App Store or Google Play.
Create a new project in the Blynk app.
Add a button widget to the project and configure it to control a digital pin (e.g., D1) on the ESP8266.
Note down the Auth Token provided by Blynk.


Programming the ESP8266:
Install the Arduino IDE on your computer.
Add the ESP8266 board to the Arduino IDE.
Install the Blynk library in the Arduino IDE.
Write or modify the code to include the Blynk Auth Token and control the relay module via the ESP8266.
Upload the code to the ESP8266 using a USB-to-serial converter.




Example Code
Here's a basic example of how to control the relay module using the ESP8266 and Blynk:
cpp
Copy code
#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "YourAuthToken";
char ssid[] = "YourNetworkName";
char pass[] = "YourPassword";

void setup()
{
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  pinMode(D1, OUTPUT);
}

void loop()
{
  Blynk.run();
}
Usage
Plug your electronic device into the switchboard socket.
Open the Blynk app on your mobile device.
Press the button in the Blynk app to turn the device on or off.
Troubleshooting
Connection Issues: Ensure the ESP8266 is within range of your WiFi network and the correct credentials are provided.
Power Supply: Verify that the ESP8266 is receiving a stable 5V supply.
Code Uploading: Check the connections and settings if the code does not upload to the ESP8266.
Future Enhancements
Voice Control: Integrate with voice assistants like Alexa or Google Home.
Energy Monitoring: Add functionality to monitor and report the power consumption of the connected device.
Scheduling: Implement scheduling features to automate the on/off control based on time.
Contributions
Contributions to the project are welcome. Feel free to fork the repository and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

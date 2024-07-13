# Smart-WiFi-Socket-With-Anedya-IOT 

The Smart WiFi Socket is a WiFi-operated device that allows you to control any electronic device plugged into it from anywhere using an internet connection. This project utilizes the ESP8266 microcontroller, a relay module, a switchboard socket, and a 5V power supply. The control is facilitated through the Anedya-IOT & streamlit, providing a user-friendly interface for remote management.

## Features

- **Remote Control**: Operate your electronic devices from anywhere using commands in the Anedya-IOT.
- **User-Friendly Interface**: Simple on/off button control through the streamlit cloud.
- **Easy Setup**: Quick and easy installation process with detailed guidance.
- **Compatibility**: Works with a variety of electronic devices.

## Components Used

1. **ESP8266**: A WiFi microcontroller that enables internet connectivity.
2. **Relay Module**: Controls the power supply to the connected device.
3. **Switch Board Socket**: The socket into which the device is plugged.
4. **5V Power Supply**: Powers the ESP8266.
5. **Anedya-IOT Account**: To send ON/OFF commands.
6. **Streamlit Account**: To set ON/OFF buttons.

## Getting Started

### Prerequisites

- ESP8266 module
- Relay module
- Switchboard socket
- 5V power supply
- Basic knowledge of electronics and programming

### Installation

1. **Assemble the Components**:
   - Connect the relay module to the ESP8266 at D0 Pin.
   - You can connect 2nd relay module to the ESP8266 at D5 Pin  .
   - Wire the switchboard socket to the relay module.
   - Power the ESP8266 using the 5V supply.

2. **Set Up Anedya-IOT**:  
   - Go to the Anedya IoT website.
   - Sign up for a new account using your email address and create a password.
   - Log in to your account using the credentials you created.
   - Once logged in, navigate to the dashboard.
   - Click on "Create New Project."
   - Enter a name and description for your project.
   - Click on "Your Project."
   - Click on "Nodes."
   - Click on "Create New Node."
   - Enter a name and description for your node.
   - Node API Identifier: Give a short identifier to refer to this node when accessing through API.
   - Turn on Preauthrorize a Device.
   - Get a Physical Device ID from this website https://www.uuidgenerator.net/  and paste it on Physical Device ID then create node.
   - Now Click on "Details" of the created node note down the Connection Key & Physical Device ID.
   - Next Steps will be done after programing the esp8266 board.
   - Click on "Commands" of the created node.
   - Then Click on "New Command" to control relay 1 or socket 1 write "light" on command or to control relay 2 or socket 2 write "fan" on command
   - After that untick the The data is base64 encoded
   - After that write "on" if you want to turn on socket or write "off" if you want to turn off socket
   - Then Click on "Create Command" then you will see your physical socket will work properly


3. **Programming the ESP8266**:
   - Install the Arduino IDE on your computer.
   - Add the ESP8266 board to the Arduino IDE.
   - Install the Blynk library in the Arduino IDE.
   - Write or modify the code to include the BLYNK_AUTH_TOKEN,BLYNK_TEMPLATE_ID,BLYNK_TEMPLATE_NAME and control the relay module via the ESP8266.
   - Add ssid (your wifi password) & pass (your wifi password) into the code.
   - Upload the code to the ESP8266 

### Code

Here's a basic code of how to control the relay module using the ESP8266 and Blynk:

```cpp

#define BLYNK_TEMPLATE_ID "TMPL3Tkiiwz8Z"//provided by Blynk.
#define BLYNK_TEMPLATE_NAME "WIFISOCKET"//provided by Blynk.
#define BLYNK_AUTH_TOKEN "Pd4kSogDD7HrFAPdvfsUcojt0LrVXib3"//provided by Blynk.
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Manav"; // type your wifi name
char pass[] = "11111111"; // type your wifi password
int relaypin = D4;
void setup()
{
Serial.begin(115200);
Blynk.begin(auth, ssid, pass);
pinMode(relaypin,OUTPUT);
}
void loop()
{
Blynk.run();
}
```


## Usage

1. Plug your electronic device into the switchboard socket.
2. Open the Blynk app on your mobile device.
3. Press the button in the Blynk app to turn the device on or off.

## Troubleshooting

- **Connection Issues:** Ensure the ESP8266 is within range of your WiFi network and the correct credentials are provided.
- **Power Supply:** Verify that the ESP8266 is receiving a stable 5V supply.
- **Code Uploading:** Check the connections and settings if the code does not upload to the ESP8266.

## API Reference

### Blynk Library

The Blynk library allows your hardware to communicate with the Blynk servers, enabling remote control via the Blynk app. Below are the key functions used in the example code:

- `Blynk.begin(auth, ssid, pass)`: Initializes the connection to the Blynk server using the provided Auth Token, WiFi SSID, and password.
- `Blynk.run()`: Keeps the connection to the Blynk server alive and processes incoming commands.

### Digital Pin Control

- `pinMode(pin, mode)`: Configures the specified pin to behave either as an input or an output.


## Future Enhancements

- **Voice Control:** Integrate with voice assistants like Alexa or Google Home.
- **Energy Monitoring:** Add functionality to monitor and report the power consumption of the connected device.
- **Scheduling:** Implement scheduling features to automate the on/off control based on time.

## Contributions

Contributions to the project are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

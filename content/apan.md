Title:APAN: Arduino Privacy Automatic Navigator
Date: 2023-07-22 04:37
Category:Inclassable
Tags:APAN
Authors: Anthony Le Goff
Summary:

Je suis retomber sur un article que j'avais sauvegarder sur mon ordinateur que j'avais en projet de mettre en place en bidouillant avec un [Arduino BLE 33 IoT à 32€](https://www.gotronic.fr/art-arduino-nano-33-iot-abx00032-33808.htm) et un [écran OLED 128x32 à 1,21€](https://fr.aliexpress.com/item/32798439084.html?spm=a2g0o.productlist.main.1.7ccc38c3Yhq97Y&algo_pvid=e3aa5195-379f-494d-9cf7-c4fd4e70dca1&algo_exp_id=e3aa5195-379f-494d-9cf7-c4fd4e70dca1-0&pdp_npi=3%40dis%21EUR%211.31%211.21%21%21%211.43%21%21%40210218bf16899940914706868d077b%2165611003507%21sea%21FR%213106627944&curPageLogUid=oqVpvnmIstn3)

Il y a plusieurs méthodes pour surfer sur internet de manière furtive, tel que les VPN, TOR, Proxy. Et les changements de DNS chiffrés. C'est en particulier pour lutter contre les services de renseignement des gouvernements et le tracking des publicitaires, même votre FAI fait du marchandage de vos données de navigation.

La méthode utilise le principe du leurre. Il faut créer un système de brouillage, à travers du bruit. Chez les militaires et la guerre électronique on appel ça des contres-mesures. En gros générer des données de navigation aléatoire, noyer votre propre navigation internet dans une masse de donnée. Et ça coût pas cher de mettre en place un petit serveur sur votre réseau local via un Arduino qui va générer ces données.

J'ai retrouvé le tuto, j'avais sauvegardé sur mon PC. Car depuis Google censure un peu le mot clé **APAN** et donne aucun résultat.

On peut retrouver la méthode sur [Hackster.io](https://www.hackster.io/cstram/apan-arduino-privacy-automatic-navigator-0c7c85)

Code `apan.ino`:

```C
/*
Carlo Stramaglia 28 August 2021
https://www.youtube.com/c/CarloStramaglia

Arduino
Privacy
Automatic
Navigator

APAN
The Arduino Privacy Automatic Navigator is a free tool created with the intent to confuse the ISP.
When you setup the Arduino Privacy Automatic Navigator in your local network, the system will start 
browsing towards sites that have nothing to do with your lifestyle. To be more precise, it will 
connect to your network with a random host name and will search for a random keyword on google all 
day long. Will also navigate while you are not at home so that the ISP will log the presence of people 
in the house while you are on holiday. This will be done massively in order to confuse the ISP and 
have wrong data.

IMPORTANT: YOU NEED TO PUT YOUR WIFI SSID AND PASSWORD in the arduino_secrets.h file
*/


#include <SPI.h>
#include <WiFiNINA.h>
#include "arduino_secrets.h" // update the file with your network data
#include <U8x8lib.h>

// Settings for Display
U8X8_SSD1306_128X32_UNIVISION_SW_I2C u8x8(/* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key index number (needed only for WEP)

int status = WL_IDLE_STATUS;
char server[] = "www.google.com";    // name address for Google (using DNS)

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
WiFiClient client;

// Variables for the random hostname and search keyword
char word1[12];
char hostn[12];
char webcom[80];
unsigned long t=0;

// Reset PIN
const int OUTPUT_PIN = 2;

void setup() {
  // Setup the PIN for the reset at the end of the sketch
  digitalWrite(OUTPUT_PIN, HIGH);
  pinMode(OUTPUT_PIN, OUTPUT);

  // Display setup
  u8x8.begin();
  u8x8.setPowerSave(0);
  u8x8.setFont(u8x8_font_chroma48medium8_r);

  //Initialize serial and wait for port to open:
  Serial.begin(9600);
//  while (!Serial) {
//    ; // wait for serial port to connect. Needed for native USB port only
//  }
  // Welcome message
  u8x8.drawString(0,0,"WELCOME TO APAN");
  u8x8.drawString(0,1,"---------------");
  u8x8.drawString(0,3," STARTING NOW  ");

  // Create a random hostname
  delay(3000);
  srand(millis());
  rword(hostn);
  Serial.print("The random hostname is: ");
  Serial.println(hostn);
  u8x8.drawString(0,0,"The Hostname is:");
  u8x8.drawString(0,1,"---------------");
  u8x8.drawString(0,3,"                ");
  u8x8.drawString(0,3,hostn);
  WiFi.setHostname(hostn);
 
  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // attempt to connect to WiFi network:
  
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }
  // Create a random keyword to search
  srand(millis());
  rword(word1);
  Serial.print("The random word is: ");
  Serial.println(word1);
  u8x8.drawString(0,0,"The Keyword is: ");
  u8x8.drawString(0,1,"-------------- ");
  u8x8.drawString(0,3,"                ");
  u8x8.drawString(0,3,word1);
  sprintf(webcom,"GET /search?q=%s HTTP/1.1",word1);
  
  Serial.println("Connected to WiFi");
  printWifiStatus();

  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  if (client.connect(server, 80)) {
    Serial.println("connected to server");

    delay (3000);
    // Make a HTTP request:
    client.println(webcom);
    client.println("Host: www.google.com");
    client.println("Connection: close");
    client.println();
    
  }
 
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  char datas[1];
  Serial.println("START PROCESSING DATA");
  u8x8.drawString(0,0,"PROCESSING DATA ");
  u8x8.drawString(0,1,"--------------- ");
  u8x8.drawString(0,3,"                ");
  u8x8.setCursor(0, 3);
  Serial.println("START SPRINTF");
  while (client.available()) {
    // Serial.println("CLIENT AVAILABLE");
    char c = client.read();
    sprintf(datas, "%d", c);
    if (t < millis() ) {
      t = millis() + 30;
      u8x8.print(datas);
    }      
    // Serial.write(c); // Uncomment this to see data on the monitor
    // delay(10);
  }
  Serial.println("START WAIT");
  //Wait 15 seconds
  delay (15000);

  Serial.println("START DICONNECTING SERVER");   
  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting from server.");
    client.stop();
  }

  Serial.println("START RESET");
  // Reset the Arduino
  u8x8.drawString(0,0,"RESETTING BOARD");
  u8x8.drawString(0,1,"--------------- ");
  u8x8.drawString(0,3,"                ");
  delay (3000);
  digitalWrite(OUTPUT_PIN, LOW);

  
}


void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");

  // print mac address:
  byte mac[6];
  WiFi.macAddress(mac);
  Serial.print("MAC: ");
  Serial.print(mac[5],HEX);
  Serial.print(":");
  Serial.print(mac[4],HEX);
  Serial.print(":");
  Serial.print(mac[3],HEX);
  Serial.print(":");
  Serial.print(mac[2],HEX);
  Serial.print(":");
  Serial.print(mac[1],HEX);
  Serial.print(":");
  Serial.println(mac[0],HEX);
/*
  // print mac address:
  int mac = WiFi.macAddress();
  Serial.print ("MAC Address: ");
  Serial.println(mac);
*/

//  char word[12];
//  char word2[12];
//  int x=0;
//  srand(millis());
//    while (x<50)
//    {
//      rword(word1);
//      rword(word2);
//      cout << word << ' ' << word2 << endl;
//      Serial.println(word1);
//      x++;
//    }

}

void rword (char *word)
{
int len = rand () % 11 + 1;
word [len] = 0;
while (len) word [--len] = 'a' + rand () % 26;
}
```

Code `apan_include.ino`:
```C
#define SECRET_SSID "SSID"
#define SECRET_PASS "Password"
```

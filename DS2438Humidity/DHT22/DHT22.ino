/*
 * Code für Testaufbau DHT22 und Arduino Nano Clone. Zusammenkopiert vom OneWireHub Projekt
 * und Beispiel der Arduino DHT Bibliothek.
 *
 * Emuliert einen DS2438 Smart Battery Monitor. Code funktioniert, wird aber nicht weiter
 * eingesetzt und entsprechend nicht besonders sauber programmiert.
 *
 */

#include "OneWireHub.h"
#include "DS2438.h"  // Smart Battery Monitor
#include "DHT.h"

#define DHTPIN 6
#define DHTTYPE DHT22  // DHT 22  (AM2302), AM2321

constexpr uint8_t pin_led       { 13 };
constexpr uint8_t pin_onewire   { 8 };

// Initialize DHT sensor.
DHT dht(DHTPIN, DHTTYPE);

auto hub    = OneWireHub(pin_onewire);
auto ds2438 = DS2438( DS2438::family_code, 0x00, 0x00, 0x38, 0x24, 0xDA, 0x00 );    //      - Smart Battery Monitor


bool blinking(void);
bool do_dht(void);

void setup()
{
    Serial.begin(115200);
    Serial.println("OneWire-Hub DS2438 Smart Battery Monitor");

    pinMode(pin_led, OUTPUT);

    // Setup OneWire
    hub.attach(ds2438);

    // Test-Cases: the following code is just to show basic functions, can be removed any time
    Serial.print("Test: set Temperature in float 38 deg C: ");
    ds2438.setTemperature(38.0f);  // can vary from -55 to 125deg
    Serial.println(ds2438.getTemperature());

    Serial.print("Test: set Voltage to 8.70 V: ");
    ds2438.setVoltage(870); // 10mV-Steps
    Serial.println(ds2438.getVoltage());

    Serial.print("Test: set Current to 700 n: ");
    ds2438.setCurrent(700);  // hasn't any unit or scale
    Serial.println(ds2438.getCurrent());

    dht.begin();

    Serial.println("config done");
}

void loop()
{
    // following function must be called periodically
    hub.poll();
    
    if (do_dht()) {
      Serial.println(F("DHT"));
    }
    
    // Blink
    if (blinking()) {
      Serial.println(F("Blink"));
    }
}

bool blinking(void)
{
    const  uint32_t interval    = 2000;          // interval at which to blink (milliseconds)
    static uint32_t nextMillis  = millis();     // will store next time LED will updated

    if (millis() > nextMillis)
    {
        nextMillis += interval;             // save the next time you blinked the LED
        static uint8_t ledState = LOW;      // ledState used to set the LED
        if (ledState == LOW)    ledState = HIGH;
        else                    ledState = LOW;
        digitalWrite(pin_led, ledState);
        return 1;
    }
    return 0;
}

bool do_dht(void)
{
  const  uint32_t interval    = 2000;          // interval at which to blink (milliseconds)
  static uint32_t nextMillis  = millis();     // will store next time LED will updated

  if (millis() > nextMillis)
  {
    nextMillis += interval;             // save the next time you blinked the LED
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
  
    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t)) {
      Serial.println(F("Failed to read from DHT sensor!"));
      return 0;
    }

    uint16_t volt_10mV;
    volt_10mV = (uint16_t)((h + 41.98)/38.92*100.0);
    ds2438.setVoltage(volt_10mV);
    ds2438.setTemperature(t);
    
    Serial.print(F("Humidity: "));
    Serial.print(h);
    Serial.print(F("%  Temperature: "));
    Serial.print(t);
    Serial.print(F("°C "));

    return 1;
  }
  return 0;
}

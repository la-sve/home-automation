/*
 * Code für Testaufbau mit HTU21D Breakout Board und Arduino Nano Clone. 
 * Zusammenkopiert vom OneWireHub Projekt und Beispiel der Arduino Sparkfun HTU21D Bibliothek.
 *
 * Emuliert einen DS2438 Smart Battery Monitor. Code funktioniert, jedoch scheint es Probleme
 * mit der I2C Bibliothek zu geben. Nach einiger Zeit bleibt der Code "hängen", mutmaßlich aufgrund
 * fehlerhafter Kommunikation. 
 *
 * Abhilfe schafft an dieser Stelle ein Watchdog Timer, siehe bspw.:
 * see e.g.: https://spellfoundry.com/2020/06/25/reliable-embedded-systems-using-the-arduino-watchdog/
 *
 * Achtung: Der neueste Bootloader wird für den Arduino benötigt, um mit watchdog Timern arbeiten zu können.
 */

#include <avr/wdt.h>  // For Watchdog

#include "OneWireHub.h"
#include "DS2438.h"  // Smart Battery Monitor
#include <Wire.h>
#include "SparkFunHTU21D.h"

// Turn on serial communication
//#define DEBUG

constexpr uint8_t pin_led       { 13 };
constexpr uint8_t pin_onewire   { 14 };

// Initialize the sensor.
HTU21D sensor;

auto hub    = OneWireHub(pin_onewire);
auto ds2438 = DS2438( DS2438::family_code, 0x00, 0x00, 0x38, 0x24, 0xDA, 0x00 );    //      - Smart Battery Monitor


bool do_htu(void);

enum eHTUState:uint8_t{
  HTUTriggerHumidity = 0,
  HTUReadHumidity,
  HTUTriggerTemperature,
  HTUReadTemperature,
  HTUWait
};

void setup(){
  
  // Enable the Watchdog
  wdt_enable( WDTO_4S);
  
  #ifdef DEBUG
  Serial.begin(115200);
  Serial.println("OneWire-Hub DS2438 Smart Battery Monitor");
  #endif

  pinMode(pin_led, OUTPUT);

  // Setup OneWire
  hub.attach(ds2438);

  ds2438.setTemperature(38.0f);  // can vary from -55 to 125deg
  ds2438.setVoltage(870); // 10mV-Steps
  ds2438.setCurrent(700);  // hasn't any unit or scale

  #ifdef DEBUG
  // Test-Cases: the following code is just to show basic functions, can be removed any time
  Serial.print("Test: set Temperature in float 38 deg C: ");
  Serial.println(ds2438.getTemperature());

  Serial.print("Test: set Voltage to 8.70 V: ");
  Serial.println(ds2438.getVoltage());

  Serial.print("Test: set Current to 700 n: ");
  Serial.println(ds2438.getCurrent());
  #endif

  sensor.begin();

  #ifdef DEBUG
  Serial.println("config done");
  #endif
}

void loop(){
  
  // following function must be called periodically
  hub.poll();
  
  if (do_htu()) {
    #ifdef DEBUG
    Serial.println(F("HTU Event"));
    #endif
  }
    
}

bool do_htu(void)
{
  const  uint32_t interval_wait    = 1500;     // interval at which to blink (milliseconds)
  const  uint32_t interval_measure = 100;      // Time for the sensor to have a new measurement
  const  uint32_t interval_next    = 10;       // Minimal time before triggering next value
  static uint32_t nextMillis  = millis();      // will store next time LED will updated
  static enum eHTUState state = HTUTriggerHumidity;
  static float t = NAN; 
  static float h = NAN; 

  uint32_t currentMillis = millis();

  if (state == HTUTriggerHumidity && currentMillis > nextMillis){
    sensor.triggerHumidity();
    nextMillis = currentMillis + interval_measure;
    state = (eHTUState)(state + 1); // Continue with next state
    return 1;
  }

  if (state == HTUReadHumidity && currentMillis > nextMillis){
    h = sensor.readHumidity();
    nextMillis = currentMillis + interval_next;
    state = (eHTUState)(state + 1); // Continue with next state
    return 1;
  }

  if (state == HTUTriggerTemperature && currentMillis > nextMillis){
    sensor.triggerTemperature();
    nextMillis = currentMillis + interval_measure;
    state = (eHTUState)(state + 1); // Continue with next state
    return 1;
  }

  if (state == HTUReadTemperature && currentMillis > nextMillis){
    t = sensor.readTemperature();
    nextMillis = currentMillis + interval_next;
    state = (eHTUState)(state + 1); // Continue with next state
    return 1;
  }
  
  if (state == HTUWait && currentMillis > nextMillis){

    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t)) {
      #ifdef DEBUG
      Serial.println(F("Failed to read from HUT21 sensor!"));
      #endif
    }else{
      
      uint16_t volt_10mV;
      volt_10mV = (uint16_t)((h + 41.98)/38.92*100.0);
      ds2438.setVoltage(volt_10mV);
      ds2438.setTemperature(t);
  
      #ifdef DEBUG
      Serial.print(F("Humidity: "));
      Serial.print(h);
      Serial.print(F("%  Temperature: "));
      Serial.print(t);
      Serial.print(F("°C "));
      #endif
    }

    // Toggle LED
    static uint8_t ledState = LOW;      // ledState used to set the LED
    if (ledState == LOW)    ledState = HIGH;
    else                    ledState = LOW;
    digitalWrite(pin_led, ledState);

    // Reset the watchdog
    wdt_reset();
    
    nextMillis = currentMillis + interval_wait;
    state = HTUTriggerHumidity; // Continue with first state
    return 1;
  }
  
  return 0;
}

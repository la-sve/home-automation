EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev "1"
Comp ""
Comment1 "Designed for AISLER 2-Layer Service"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Module:Arduino_Nano_v2.x A1
U 1 1 61AE8D93
P 4650 3450
F 0 "A1" H 4650 2361 50  0000 C CNN
F 1 "Arduino_Nano_v2.x" H 4650 2270 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 4650 3450 50  0001 C CIN
F 3 "https://www.arduino.cc/en/uploads/Main/ArduinoNanoManual23.pdf" H 4650 3450 50  0001 C CNN
	1    4650 3450
	1    0    0    -1  
$EndComp
$Comp
L Connector:RJ45 J1
U 1 1 61AEC3EF
P 7600 2900
F 0 "J1" H 7270 2904 50  0000 R CNN
F 1 "RJ45" H 7270 2995 50  0000 R CNN
F 2 "Connector_RJ:RJ45_Amphenol_54602-x08_Horizontal" V 7600 2925 50  0001 C CNN
F 3 "~" V 7600 2925 50  0001 C CNN
	1    7600 2900
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x04_Female J2
U 1 1 61AED8F8
P 7200 4100
F 0 "J2" H 7228 4076 50  0000 L CNN
F 1 "GY-21 HTU21" H 7228 3985 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 7200 4100 50  0001 C CNN
F 3 "~" H 7200 4100 50  0001 C CNN
	1    7200 4100
	1    0    0    -1  
$EndComp
Text Label 7000 4000 2    50   ~ 0
VIN
Text Label 7000 4100 2    50   ~ 0
GND
Text Label 7000 4200 2    50   ~ 0
SCL
Text Label 7000 4300 2    50   ~ 0
SDA
Text Label 7200 3300 2    50   ~ 0
B-GND
Text Label 7200 3200 2    50   ~ 0
B-5V
Text Label 7200 3100 2    50   ~ 0
A-WireSensor
Text Label 7200 3000 2    50   ~ 0
B-WireRueck
Text Label 7200 2900 2    50   ~ 0
B-WireSensor
Text Label 7200 2800 2    50   ~ 0
A-WireRueck
Text Label 7200 2700 2    50   ~ 0
A-5V
Text Label 7200 2600 2    50   ~ 0
A-GND
Text Label 5150 3450 0    50   ~ 0
1Wire-A
Text Label 5150 3850 0    50   ~ 0
SDA
Text Label 5150 3950 0    50   ~ 0
SCL
Wire Wire Line
	5150 3950 6450 3950
Wire Wire Line
	6450 3950 6450 4200
Wire Wire Line
	6450 4200 7000 4200
Wire Wire Line
	4550 2350 4550 2450
Wire Wire Line
	7000 4100 6500 4100
Wire Wire Line
	6500 3300 6400 3300
Wire Wire Line
	7000 4000 6550 4000
Wire Wire Line
	6550 4000 6550 3200
Wire Wire Line
	6550 3200 6350 3200
Wire Wire Line
	7000 4300 6400 4300
Wire Wire Line
	6400 4300 6400 3850
Wire Wire Line
	5150 3850 6400 3850
$Comp
L Connector:RJ45 J3
U 1 1 61B118EE
P 7600 1500
F 0 "J3" H 7270 1504 50  0000 R CNN
F 1 "RJ45" H 7270 1595 50  0000 R CNN
F 2 "Connector_RJ:RJ45_Amphenol_54602-x08_Horizontal" V 7600 1525 50  0001 C CNN
F 3 "~" V 7600 1525 50  0001 C CNN
	1    7600 1500
	-1   0    0    1   
$EndComp
Text Label 7200 1900 2    50   ~ 0
2B-GND
Text Label 7200 1800 2    50   ~ 0
2B-5V
Text Label 7200 1700 2    50   ~ 0
2A-WireSensor
Text Label 7200 1600 2    50   ~ 0
2B-WireRueck
Text Label 7200 1500 2    50   ~ 0
2B-WireSensor
Text Label 7200 1400 2    50   ~ 0
2A-WireRueck
Text Label 7200 1300 2    50   ~ 0
2A-5V
Text Label 7200 1200 2    50   ~ 0
2A-GND
Wire Wire Line
	6050 1200 6050 2600
Wire Wire Line
	6100 1300 6100 2700
Wire Wire Line
	6150 1400 6150 2800
Wire Wire Line
	6200 1500 6200 2900
Wire Wire Line
	6250 1600 6250 3000
Wire Wire Line
	6300 1700 6300 3100
Wire Wire Line
	6350 1800 6350 2350
$Comp
L Jumper:SolderJumper_2_Open JP5
U 1 1 61B1D460
P 5500 1500
F 0 "JP5" H 5500 1705 50  0000 C CNN
F 1 "B-SolderIfLastOnBus" H 5500 1614 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 5500 1500 50  0001 C CNN
F 3 "~" H 5500 1500 50  0001 C CNN
	1    5500 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6250 1600 5300 1600
$Comp
L Jumper:SolderJumper_2_Open JP4
U 1 1 61B2264C
P 4750 1400
F 0 "JP4" H 4750 1605 50  0000 C CNN
F 1 "A-SolderIfLastOnBus" H 4750 1514 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 4750 1400 50  0001 C CNN
F 3 "~" H 4750 1400 50  0001 C CNN
	1    4750 1400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4650 4450 4750 4450
Connection ~ 4750 4450
NoConn ~ 4150 2850
NoConn ~ 4150 2950
NoConn ~ 4150 3050
NoConn ~ 4150 3150
NoConn ~ 4150 3250
NoConn ~ 4150 3350
NoConn ~ 4150 3450
NoConn ~ 4150 3550
NoConn ~ 4150 3650
NoConn ~ 4150 3750
NoConn ~ 4150 3850
NoConn ~ 4150 3950
NoConn ~ 4150 4050
NoConn ~ 4150 4150
NoConn ~ 5150 2850
NoConn ~ 5150 2950
NoConn ~ 5150 3250
NoConn ~ 5150 3650
NoConn ~ 5150 3750
NoConn ~ 5150 4050
NoConn ~ 5150 4150
NoConn ~ 4850 2450
NoConn ~ 4750 2450
$Comp
L Mechanical:MountingHole H3
U 1 1 61B30BEC
P 2700 1250
F 0 "H3" H 2800 1296 50  0000 L CNN
F 1 "MountingHole" H 2800 1205 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 2700 1250 50  0001 C CNN
F 3 "~" H 2700 1250 50  0001 C CNN
	1    2700 1250
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 61B3149B
P 2200 1250
F 0 "H2" H 2300 1296 50  0000 L CNN
F 1 "MountingHole" H 2300 1205 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 2200 1250 50  0001 C CNN
F 3 "~" H 2200 1250 50  0001 C CNN
	1    2200 1250
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H1
U 1 1 61B320C0
P 1700 1300
F 0 "H1" H 1800 1346 50  0000 L CNN
F 1 "MountingHole" H 1800 1255 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 1700 1300 50  0001 C CNN
F 3 "~" H 1700 1300 50  0001 C CNN
	1    1700 1300
	1    0    0    -1  
$EndComp
Text Label 5150 3550 0    50   ~ 0
1Wire-B
Wire Wire Line
	6400 1900 6400 3300
Wire Wire Line
	7200 2600 6600 2600
Wire Wire Line
	6050 1200 7200 1200
Wire Wire Line
	6100 1300 7200 1300
Wire Wire Line
	6150 1400 7200 1400
Connection ~ 6150 1400
Wire Wire Line
	6200 1500 7200 1500
Wire Wire Line
	6250 1600 7200 1600
Connection ~ 6250 1600
Wire Wire Line
	6300 1700 7200 1700
Connection ~ 6300 1700
Wire Wire Line
	6350 1800 7200 1800
Wire Wire Line
	6400 1900 7200 1900
Wire Wire Line
	6100 2700 6550 2700
Wire Wire Line
	6150 2800 7200 2800
Wire Wire Line
	6200 2900 7200 2900
Wire Wire Line
	6250 3000 7200 3000
Wire Wire Line
	6300 3100 7200 3100
Wire Wire Line
	6550 3200 7200 3200
Connection ~ 6550 3200
Wire Wire Line
	6500 4100 6500 3300
Wire Wire Line
	6500 3300 6600 3300
Connection ~ 6500 3300
$Comp
L Jumper:SolderJumper_2_Open JP6
U 1 1 61B52F36
P 5650 3450
F 0 "JP6" H 5650 3655 50  0000 C CNN
F 1 "Connect-A" H 5650 3564 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 5650 3450 50  0001 C CNN
F 3 "~" H 5650 3450 50  0001 C CNN
	1    5650 3450
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_2_Open JP7
U 1 1 61B54549
P 5650 3550
F 0 "JP7" H 5650 3755 50  0000 C CNN
F 1 "Connect-B" H 5650 3664 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 5650 3550 50  0001 C CNN
F 3 "~" H 5650 3550 50  0001 C CNN
	1    5650 3550
	-1   0    0    1   
$EndComp
Wire Wire Line
	6150 1400 6150 1050
Wire Wire Line
	6150 1050 4750 1050
Wire Wire Line
	4750 1050 4750 1250
Wire Wire Line
	4750 1700 4750 1550
Wire Wire Line
	4750 1700 6300 1700
Wire Wire Line
	6200 1500 5650 1500
Connection ~ 6200 1500
Wire Wire Line
	5300 1600 5300 1500
Wire Wire Line
	5300 1500 5350 1500
Wire Wire Line
	5500 3550 5150 3550
Wire Wire Line
	5500 3450 5150 3450
Wire Wire Line
	6500 4100 6500 4450
Wire Wire Line
	4750 4450 6500 4450
Connection ~ 6500 4100
Wire Wire Line
	4550 2350 6350 2350
Connection ~ 6350 2350
Wire Wire Line
	6350 2350 6350 3200
Wire Wire Line
	5800 3550 6200 3550
Wire Wire Line
	6200 3550 6200 2900
Connection ~ 6200 2900
Wire Wire Line
	5800 3450 6300 3450
Wire Wire Line
	6300 3450 6300 3100
Connection ~ 6300 3100
Text Notes 8850 1250 0    50   ~ 0
Alternativer Anschluss mittels Pins
$Comp
L Connector:Conn_01x08_Male J33
U 1 1 61B7FF5B
P 9700 1900
F 0 "J33" H 9672 1874 50  0000 R CNN
F 1 "Bus Out" H 9672 1783 50  0000 R CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" H 9700 1900 50  0001 C CNN
F 3 "~" H 9700 1900 50  0001 C CNN
	1    9700 1900
	-1   0    0    -1  
$EndComp
Text Label 9500 2300 2    50   ~ 0
2B-GND
Text Label 9500 2200 2    50   ~ 0
2B-5V
Text Label 9500 2100 2    50   ~ 0
2A-WireSensor
Text Label 9500 2000 2    50   ~ 0
2B-WireRueck
Text Label 9500 1900 2    50   ~ 0
2B-WireSensor
Text Label 9500 1800 2    50   ~ 0
2A-WireRueck
Text Label 9500 1700 2    50   ~ 0
2A-5V
Text Label 9500 1600 2    50   ~ 0
2A-GND
$Comp
L Connector:Conn_01x08_Male J11
U 1 1 61B93101
P 9700 2900
F 0 "J11" H 9672 2874 50  0000 R CNN
F 1 "Bus In" H 9672 2783 50  0000 R CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" H 9700 2900 50  0001 C CNN
F 3 "~" H 9700 2900 50  0001 C CNN
	1    9700 2900
	-1   0    0    -1  
$EndComp
Text Label 9500 3300 2    50   ~ 0
B-GND
Text Label 9500 3200 2    50   ~ 0
B-5V
Text Label 9500 3100 2    50   ~ 0
A-WireSensor
Text Label 9500 3000 2    50   ~ 0
B-WireRueck
Text Label 9500 2900 2    50   ~ 0
B-WireSensor
Text Label 9500 2800 2    50   ~ 0
A-WireRueck
Text Label 9500 2700 2    50   ~ 0
A-5V
Text Label 9500 2600 2    50   ~ 0
A-GND
Wire Wire Line
	6550 3200 6550 2700
Connection ~ 6550 2700
Wire Wire Line
	6550 2700 7200 2700
Wire Wire Line
	6600 2600 6600 3300
Connection ~ 6600 2600
Wire Wire Line
	6600 2600 6050 2600
Connection ~ 6600 3300
Wire Wire Line
	6600 3300 7200 3300
$EndSCHEMATC

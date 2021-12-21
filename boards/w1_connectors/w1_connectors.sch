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
L Connector:Conn_01x10_Female J1
U 1 1 61BCF3D2
P 1000 2050
F 0 "J1" H 800 1400 50  0000 C CNN
F 1 "ConnLV" H 850 2650 50  0000 C CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MPT-0,5-10-2.54_1x10_P2.54mm_Horizontal" H 1000 2050 50  0001 C CNN
F 3 "~" H 1000 2050 50  0001 C CNN
	1    1000 2050
	-1   0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x10_Female J2
U 1 1 61BD0E39
P 6150 2150
F 0 "J2" H 5950 1500 50  0000 L CNN
F 1 "ConnHV" H 5800 2650 50  0000 L CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MPT-0,5-10-2.54_1x10_P2.54mm_Horizontal" H 6150 2150 50  0001 C CNN
F 3 "~" H 6150 2150 50  0001 C CNN
	1    6150 2150
	1    0    0    1   
$EndComp
$Comp
L Connector:Conn_01x06_Female J3
U 1 1 61BD4DA7
P 3100 1850
F 0 "J3" H 3128 1826 50  0000 L CNN
F 1 "LevelConverterLV" H 2750 2200 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" H 3100 1850 50  0001 C CNN
F 3 "~" H 3100 1850 50  0001 C CNN
	1    3100 1850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x06_Female J4
U 1 1 61BD8F4C
P 4050 1850
F 0 "J4" H 4150 1850 50  0000 C CNN
F 1 "LevelConverterHV" H 4050 2200 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" H 4050 1850 50  0001 C CNN
F 3 "~" H 4050 1850 50  0001 C CNN
	1    4050 1850
	-1   0    0    -1  
$EndComp
Text Label 2900 1650 2    50   ~ 0
LV11
Text Label 2900 1750 2    50   ~ 0
LV12
Text Label 2900 1950 2    50   ~ 0
GND
Text Label 2900 1850 2    50   ~ 0
LV
Text Label 2900 2050 2    50   ~ 0
LV13
Text Label 2900 2150 2    50   ~ 0
LV14
Text Label 4250 1650 0    50   ~ 0
HV11
Text Label 4250 1750 0    50   ~ 0
HV12
Text Label 4250 1850 0    50   ~ 0
HV
Text Label 4250 1950 0    50   ~ 0
GND
Text Label 4250 2050 0    50   ~ 0
HV13
Text Label 4250 2150 0    50   ~ 0
HV14
$Comp
L Connector:Conn_01x06_Female J5
U 1 1 61BE2C02
P 3100 2850
F 0 "J5" H 3128 2826 50  0000 L CNN
F 1 "LevelConverterHV" H 2750 3200 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" H 3100 2850 50  0001 C CNN
F 3 "~" H 3100 2850 50  0001 C CNN
	1    3100 2850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x06_Female J6
U 1 1 61BE2C08
P 4050 2850
F 0 "J6" H 4150 2850 50  0000 C CNN
F 1 "LevelConverterHV" H 4050 3200 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" H 4050 2850 50  0001 C CNN
F 3 "~" H 4050 2850 50  0001 C CNN
	1    4050 2850
	-1   0    0    -1  
$EndComp
Text Label 2900 2650 2    50   ~ 0
LV21
Text Label 2900 2750 2    50   ~ 0
LV22
Text Label 2900 2950 2    50   ~ 0
GND
Text Label 2900 2850 2    50   ~ 0
LV
Text Label 2900 3050 2    50   ~ 0
LV23
Text Label 2900 3150 2    50   ~ 0
LV24
Text Label 4250 2650 0    50   ~ 0
HV21
Text Label 4250 2750 0    50   ~ 0
HV22
Text Label 4250 2850 0    50   ~ 0
HV
Text Label 4250 2950 0    50   ~ 0
GND
Text Label 4250 3050 0    50   ~ 0
HV23
Text Label 4250 3150 0    50   ~ 0
HV24
Text Label 1200 1650 0    50   ~ 0
LV1
Text Label 1200 1750 0    50   ~ 0
LV2
Text Label 1200 1850 0    50   ~ 0
LV3
Text Label 1200 1950 0    50   ~ 0
LV4
Text Label 1200 2050 0    50   ~ 0
LV5
Text Label 1200 2150 0    50   ~ 0
LV6
Text Label 1200 2250 0    50   ~ 0
LV7
Text Label 1200 2350 0    50   ~ 0
LV8
Text Label 1200 2450 0    50   ~ 0
LV
Text Label 1200 2550 0    50   ~ 0
GND
Text Label 5950 1650 2    50   ~ 0
HV1
Text Label 5950 1750 2    50   ~ 0
HV2
Text Label 5950 1850 2    50   ~ 0
HV3
Text Label 5950 1950 2    50   ~ 0
HV4
Text Label 5950 2050 2    50   ~ 0
HV5
Text Label 5950 2150 2    50   ~ 0
HV6
Text Label 5950 2250 2    50   ~ 0
HV7
Text Label 5950 2350 2    50   ~ 0
HV8
Text Label 5950 2450 2    50   ~ 0
HV
Text Label 5950 2550 2    50   ~ 0
GND
Wire Wire Line
	5950 1650 5500 1650
Wire Wire Line
	5950 1750 5400 1750
Wire Wire Line
	5950 1850 5300 1850
Wire Wire Line
	5950 1950 5200 1950
Wire Wire Line
	5950 2050 5100 2050
Wire Wire Line
	5950 2150 5000 2150
Wire Wire Line
	5950 2250 4900 2250
Wire Wire Line
	5950 2350 4800 2350
Wire Wire Line
	4250 1850 4450 1850
Wire Wire Line
	4250 2850 4450 2850
Wire Wire Line
	4450 2850 4450 1850
Connection ~ 4450 1850
Wire Wire Line
	4800 3150 4800 2350
Wire Wire Line
	4250 3150 4800 3150
Wire Wire Line
	4750 3050 4750 2250
Wire Wire Line
	4250 3050 4750 3050
Wire Wire Line
	4700 2750 4700 2150
Wire Wire Line
	4250 2750 4700 2750
Wire Wire Line
	4650 2650 4650 2050
Wire Wire Line
	4250 2650 4650 2650
Wire Wire Line
	4600 2150 4600 1950
Wire Wire Line
	4250 2150 4600 2150
Wire Wire Line
	4550 2050 4550 1850
Wire Wire Line
	4250 2050 4550 2050
Wire Wire Line
	4250 1950 4500 1950
Wire Wire Line
	4500 1950 4500 2950
Wire Wire Line
	4250 2950 4500 2950
Connection ~ 4500 2950
Wire Wire Line
	4500 2950 4500 3450
Wire Wire Line
	5950 2450 5700 2450
Wire Wire Line
	5950 2550 5700 2550
Wire Wire Line
	5700 2550 5700 3450
Wire Wire Line
	5700 3450 4500 3450
Wire Wire Line
	2900 2950 2650 2950
Wire Wire Line
	2650 2950 2650 3450
Wire Wire Line
	2650 3450 4500 3450
Connection ~ 4500 3450
Wire Wire Line
	1200 2550 1450 2550
Connection ~ 2650 3450
Wire Wire Line
	1450 2550 1450 3450
Wire Wire Line
	1200 2450 1450 2450
Wire Wire Line
	2900 2850 2700 2850
Wire Wire Line
	2700 2850 2700 1850
Wire Wire Line
	2900 1850 2700 1850
Connection ~ 2700 1850
Wire Wire Line
	2900 1950 2650 1950
Wire Wire Line
	2650 1950 2650 2950
Connection ~ 2650 2950
Wire Wire Line
	2600 1850 2600 2050
Wire Wire Line
	2600 2050 2900 2050
Wire Wire Line
	2550 1950 2550 2150
Wire Wire Line
	2550 2150 2900 2150
Wire Wire Line
	2500 2050 2500 2650
Wire Wire Line
	2500 2650 2900 2650
Wire Wire Line
	2450 2150 2450 2750
Wire Wire Line
	2450 2750 2900 2750
Wire Wire Line
	2400 2250 2400 3050
Wire Wire Line
	2400 3050 2900 3050
Wire Wire Line
	2350 2350 2350 3150
Wire Wire Line
	2350 3150 2900 3150
$Comp
L Device:R HVR8
U 1 1 61C22BF7
P 4800 1350
F 0 "HVR8" V 4800 1550 50  0000 L CNN
F 1 "R" H 4750 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 4730 1350 50  0001 C CNN
F 3 "~" H 4800 1350 50  0001 C CNN
	1    4800 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR7
U 1 1 61C3470C
P 4900 1350
F 0 "HVR7" V 4900 1550 50  0000 L CNN
F 1 "R" H 4850 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 4830 1350 50  0001 C CNN
F 3 "~" H 4900 1350 50  0001 C CNN
	1    4900 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR6
U 1 1 61C363DC
P 5000 1350
F 0 "HVR6" V 5000 1550 50  0000 L CNN
F 1 "R" H 4950 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 4930 1350 50  0001 C CNN
F 3 "~" H 5000 1350 50  0001 C CNN
	1    5000 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR5
U 1 1 61C380AF
P 5100 1350
F 0 "HVR5" V 5100 1550 50  0000 L CNN
F 1 "R" H 5050 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 5030 1350 50  0001 C CNN
F 3 "~" H 5100 1350 50  0001 C CNN
	1    5100 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR4
U 1 1 61C39E0D
P 5200 1350
F 0 "HVR4" V 5200 1550 50  0000 L CNN
F 1 "R" H 5150 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 5130 1350 50  0001 C CNN
F 3 "~" H 5200 1350 50  0001 C CNN
	1    5200 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR3
U 1 1 61C3BAE1
P 5300 1350
F 0 "HVR3" V 5300 1550 50  0000 L CNN
F 1 "R" H 5250 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 5230 1350 50  0001 C CNN
F 3 "~" H 5300 1350 50  0001 C CNN
	1    5300 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR2
U 1 1 61C3D7B8
P 5400 1350
F 0 "HVR2" V 5400 1550 50  0000 L CNN
F 1 "R" H 5350 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 5330 1350 50  0001 C CNN
F 3 "~" H 5400 1350 50  0001 C CNN
	1    5400 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R HVR1
U 1 1 61C3F4D1
P 5500 1350
F 0 "HVR1" V 5500 1550 50  0000 L CNN
F 1 "R" H 5450 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 5430 1350 50  0001 C CNN
F 3 "~" H 5500 1350 50  0001 C CNN
	1    5500 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 1200 4800 1200
Wire Wire Line
	4450 1200 4450 1850
Wire Wire Line
	4900 1200 4800 1200
Connection ~ 4800 1200
Wire Wire Line
	4900 1200 5000 1200
Connection ~ 4900 1200
Wire Wire Line
	5000 1200 5100 1200
Connection ~ 5000 1200
Wire Wire Line
	5100 1200 5200 1200
Connection ~ 5100 1200
Wire Wire Line
	5200 1200 5300 1200
Connection ~ 5200 1200
Wire Wire Line
	5300 1200 5400 1200
Connection ~ 5300 1200
Wire Wire Line
	5400 1200 5500 1200
Connection ~ 5400 1200
Wire Wire Line
	5700 1200 5500 1200
Wire Wire Line
	5700 1200 5700 2450
Connection ~ 5500 1200
Wire Wire Line
	4800 1500 4800 2350
Connection ~ 4800 2350
Wire Wire Line
	4900 1500 4900 2250
Connection ~ 4900 2250
Wire Wire Line
	4900 2250 4750 2250
Wire Wire Line
	5000 1500 5000 2150
Connection ~ 5000 2150
Wire Wire Line
	5000 2150 4700 2150
Wire Wire Line
	5100 1500 5100 2050
Connection ~ 5100 2050
Wire Wire Line
	5100 2050 4650 2050
Wire Wire Line
	5200 1500 5200 1950
Connection ~ 5200 1950
Wire Wire Line
	5200 1950 4600 1950
Wire Wire Line
	5300 1500 5300 1850
Connection ~ 5300 1850
Wire Wire Line
	5300 1850 4550 1850
Wire Wire Line
	5400 1500 5400 1750
Connection ~ 5400 1750
Wire Wire Line
	5400 1750 4250 1750
Wire Wire Line
	5500 1500 5500 1650
Connection ~ 5500 1650
Wire Wire Line
	5500 1650 4250 1650
$Comp
L Device:R LVR1
U 1 1 61C7C4BD
P 1650 1350
F 0 "LVR1" V 1650 1550 50  0000 L CNN
F 1 "R" H 1600 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 1580 1350 50  0001 C CNN
F 3 "~" H 1650 1350 50  0001 C CNN
	1    1650 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR2
U 1 1 61C7C4C3
P 1750 1350
F 0 "LVR2" V 1750 1550 50  0000 L CNN
F 1 "R" H 1700 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 1680 1350 50  0001 C CNN
F 3 "~" H 1750 1350 50  0001 C CNN
	1    1750 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR3
U 1 1 61C7C4C9
P 1850 1350
F 0 "LVR3" V 1850 1550 50  0000 L CNN
F 1 "R" H 1800 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 1780 1350 50  0001 C CNN
F 3 "~" H 1850 1350 50  0001 C CNN
	1    1850 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR4
U 1 1 61C7C4CF
P 1950 1350
F 0 "LVR4" V 1950 1550 50  0000 L CNN
F 1 "R" H 1900 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 1880 1350 50  0001 C CNN
F 3 "~" H 1950 1350 50  0001 C CNN
	1    1950 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR5
U 1 1 61C7C4D5
P 2050 1350
F 0 "LVR5" V 2050 1550 50  0000 L CNN
F 1 "R" H 2000 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 1980 1350 50  0001 C CNN
F 3 "~" H 2050 1350 50  0001 C CNN
	1    2050 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR6
U 1 1 61C7C4DB
P 2150 1350
F 0 "LVR6" V 2150 1550 50  0000 L CNN
F 1 "R" H 2100 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 2080 1350 50  0001 C CNN
F 3 "~" H 2150 1350 50  0001 C CNN
	1    2150 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR7
U 1 1 61C7C4E1
P 2250 1350
F 0 "LVR7" V 2250 1550 50  0000 L CNN
F 1 "R" H 2200 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 2180 1350 50  0001 C CNN
F 3 "~" H 2250 1350 50  0001 C CNN
	1    2250 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:R LVR8
U 1 1 61C7C4E7
P 2350 1350
F 0 "LVR8" V 2350 1550 50  0000 L CNN
F 1 "R" H 2300 1700 50  0001 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder" V 2280 1350 50  0001 C CNN
F 3 "~" H 2350 1350 50  0001 C CNN
	1    2350 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1200 2350 2350 2350
Wire Wire Line
	1200 2250 2250 2250
Wire Wire Line
	1200 2150 2150 2150
Wire Wire Line
	1200 2050 2050 2050
Wire Wire Line
	1200 1950 1950 1950
Wire Wire Line
	1200 1850 1850 1850
Wire Wire Line
	1200 1750 1750 1750
Wire Wire Line
	1200 1650 1650 1650
Wire Wire Line
	2700 1200 2350 1200
Wire Wire Line
	2700 1200 2700 1850
Wire Wire Line
	2350 1200 2250 1200
Connection ~ 2350 1200
Wire Wire Line
	2250 1200 2150 1200
Connection ~ 2250 1200
Wire Wire Line
	2150 1200 2050 1200
Connection ~ 2150 1200
Wire Wire Line
	2050 1200 1950 1200
Connection ~ 2050 1200
Wire Wire Line
	1950 1200 1850 1200
Connection ~ 1950 1200
Wire Wire Line
	1850 1200 1750 1200
Connection ~ 1850 1200
Wire Wire Line
	1750 1200 1650 1200
Connection ~ 1750 1200
Wire Wire Line
	1650 1200 1450 1200
Wire Wire Line
	1450 1200 1450 2450
Connection ~ 1650 1200
Wire Wire Line
	1450 3450 2650 3450
Wire Wire Line
	2350 1500 2350 2350
Connection ~ 2350 2350
Wire Wire Line
	2250 1500 2250 2250
Connection ~ 2250 2250
Wire Wire Line
	2250 2250 2400 2250
Wire Wire Line
	2150 1500 2150 2150
Connection ~ 2150 2150
Wire Wire Line
	2150 2150 2450 2150
Wire Wire Line
	2050 1500 2050 2050
Connection ~ 2050 2050
Wire Wire Line
	2050 2050 2500 2050
Wire Wire Line
	1950 1500 1950 1950
Connection ~ 1950 1950
Wire Wire Line
	1950 1950 2550 1950
Wire Wire Line
	1850 1500 1850 1850
Connection ~ 1850 1850
Wire Wire Line
	1850 1850 2600 1850
Wire Wire Line
	1750 1500 1750 1750
Connection ~ 1750 1750
Wire Wire Line
	1750 1750 2900 1750
Wire Wire Line
	1650 1500 1650 1650
Connection ~ 1650 1650
Wire Wire Line
	1650 1650 2900 1650
$EndSCHEMATC

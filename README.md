# Pen Plotter
I designed and built a Pen Plotter to plot generative art. This document is mostly for me in case I waant to come back and improve my design, so I won't go into detail on assembly or how to actually get it working. Feel free to use the STLs to print your own. I will warn you some of the hole sizes are too small for the harware and shafts, and a lot of dremel work was required to get it to fit together. I lost my Inventor liscense before I got to make improvements, so I'm just calling this project finished.

<p float="left">
<img src="https://github.com/zradlicz/Pen-Plotter/blob/main/Media/20211016_145640.jpg" width=400px>
<img src="https://github.com/zradlicz/Pen-Plotter/blob/main/Media/20211016_145644.jpg" width=400px>
<img src="https://github.com/zradlicz/Pen-Plotter/blob/main/Media/20211016_164535.jpg" width=400px>
<img src="https://github.com/zradlicz/Pen-Plotter/blob/main/Media/20211019_193142.jpg" width=400px>
<p/>

### Arduino
Arduino folder contains grbl which has been modified to control a servo on the xlim pin. This is necessary for the pen to move up and down.
### GCode
The Gcode folder contains two python scripts to write gcode to a file which can then be used to upload to Universal GCode Sender. The Pen plotter then connects to UGS and runs.




## BOM
Part | Quantity | Price | Link
----- | ------- | ------- | ------
**3D PRINT**| | |
X_STATIC_END | 1 | N/A | N/A
X_MOVING_END | 1 | N/A | N/A
PLATFORM | 2 | N/A | N/A
PEN_HOLDER | 1 | N/A | N/A
MOTOR_MOUNT | 2 | N/A | N/A
BELT_HOLDER | 2 | N/A | N/A
**Timing Belt**| | |
GT2 Timing Belt 2mm pitch 6mm wide | 1 | $4.00 | https://www.amazon.com/dp/B0776KXY8G?psc=1&ref=ppx_yo2_dt_b_product_details
GT2 Timing Pulley 5mm 20 Teeth with Set Screw | 2 | $1.50 | https://www.amazon.com/dp/B0776KXY8G?psc=1&ref=ppx_yo2_dt_b_product_details
GT2 Timing Pulley Toothless 3mm Bore 6mm width | 4 | $1.60 | https://www.amazon.com/dp/B01H3FNZ4M?ref=ppx_yo2_dt_b_product_details&th=1
GT2 Timing Pulley Idler 3mm Bore 20 teeth| 1 | $1.40 | https://www.amazon.com/dp/B01H3DSGAC?ref=ppx_yo2_dt_b_product_details&th=1
**Axis** | | |
6mm x 300mm Linear Motion Rod Shaft | 4 | $3.44 | https://www.amazon.com/dp/B08HYF2WPX?ref=ppx_yo2_dt_b_product_details&th=1
LM6UU Linear Ball Bearing 6mm Bore 12mm OD 35mm Length | 4 | $3.00 | https://www.amazon.com/dp/B08NYJ72Z2?ref=ppx_yo2_dt_b_product_details&th=1
**Motion Control**| | |
Nema 17 Stepper Motor 45Ncm 1.8 degree | 2 | $9.00 | https://www.amazon.com/dp/B074T9ZZFJ?psc=1&ref=ppx_yo2_dt_b_product_details
9g Micro Servo | 1 | $2.74 | https://www.amazon.com/dp/B07MLR1498?ref=ppx_yo2_dt_b_product_details&th=1
CNC Shield Arduino Kit | 1 | $24.00 | https://www.amazon.com/dp/B06XHKSVTG?ref=ppx_yo2_dt_b_product_details&th=1
**Hardware**| | |
M3x20 Screw | 8 | $.10 | https://www.amazon.com/dp/B01NBOCXHE?ref=ppx_yo2_dt_b_product_details&th=1
M3x12 Screw | 2 | $.10 | https://www.amazon.com/dp/B01NBOCXHE?ref=ppx_yo2_dt_b_product_details&th=1
M3x25 Screw | 2 | $.10 | https://www.amazon.com/dp/B01NBOCXHE?ref=ppx_yo2_dt_b_product_details&th=1
3mm x 20mm Round Shaft | 4 | $1.00 | https://www.amazon.com/dp/B07JNP45G9?
**TOTAL**| |**$89.96**|

### Setup
Here is the list of GRBL Parameters I found to work the best.

$0=10
$1=25
$2=0
$3=0
$4=0
$5=0
$6=0
$10=1
$11=0.010
$12=0.002
$13=0
$20=0
$21=0
$22=0
$23=0
$24=25.000
$25=500.000
$26=250
$27=1.000
$30=1000
$31=0
$32=0
$100=84.000
$101=84.000
$102=250.000
$110=4000.000
$111=4000.000
$112=500.000
$120=200.000
$121=200.000
$122=10.000
$130=200.000
$131=200.000
$132=200.000

## Example Work

<p float="left">
<img src="https://github.com/zradlicz/Pen-Plotter/blob/main/Media/color_contour.png" width=400px>
<img src="https://github.com/zradlicz/Pen-Plotter/blob/main/Media/20211119_105208.jpg" width=400px>
<p/>

On the left is the generated image, on the right is the plotter plot. It is not as smooth or accurate as I want, and color changing is done by hand which causes some inaccuracy. The Gcode script to generate GCode also has some bugs which cause the discontinuites at some of the edges. Also my cat moved the machine a little bit at the very end.

## List of Design Improvements
- Pen Holder is too thin and has to much deflection in Y direction  
- Wires get in the way during printing  
- Design electronics box  
- Use set screws to hold shafts in place rather than press fit  



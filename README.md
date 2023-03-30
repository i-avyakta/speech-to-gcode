# speech-to-gcode

i created speech to gcode solution. i am using python speech_recognition and ttgLib.TextToGcode library. 

for speech i am using, i am using my microphone, so before run this code connect your pc to a microphone then run it, 
so firstly it will convert the speech to text 

then i am using TextToGcode Library to convert this generated text to gcode 
it's syntax is 

ttg("TEXT", SIZE, ROTATION, "MODE", FEEDRATE).toGcode("ON COMMAND", "OFF COMMAND", "FAST COMMAND", "SLOW COMMAND")

ttg(text,1,0,"return",1).toGcode("M300 S50.00","M300 S30.00","G0","G1")

We Are Using

TEXT = text
SIZE = 1
ROTATION = 0
MODE = "file" #toget the file directly
FEEDRATE = 1

ON: "M300 S50.00"
OFF: "M300 S30.00"
FAST: "G0"
SLOW: "G1"

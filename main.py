import speech_recognition as sr
from ttgLib.TextToGcode import ttg

r= sr.Recognizer()
def speechtotext():
        try:
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source)
              print("say somethibng")
              audio= r.listen(source)
              text= r.recognize_google(audio,language="en-IN", show_all = False)
              print(text)
              
              gcode = ttg(text,1,0,"return",1).toGcode("M300 S30","M300 S50","G1","G0")
              f= open('text.gcode','w')
            
              for i in gcode:
                f.write(i)
                f.write('\n')
              f.close()
              
        except:
         print("error")

        
        
if __name__=='__main__':
    speechtotext()



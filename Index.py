#import the module 
from gtts import gTTS
#adding text 
mytext = "Welcome to Coding India 's Youtube channel plz like share and subscribe"
#adding language
language = "en"
#editing it 
myobj = gTTS(text = mytext,lang = language,slow = False)
#saving it 
myobj.save("welcome.mp3")

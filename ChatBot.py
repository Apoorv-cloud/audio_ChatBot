import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only

f=open('fifa.txt','r',errors = 'ignore')
raw=f.read()
raw = raw.lower()# converts to lowercase

sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
GREETING_INPUTS = ("hello", "hi", "greetings", "sup","hey", "cool","hlo","up" )
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me","ha ha","chilling out, as you do"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        
 from sklearn.feature_extraction.text import TfidfVectorizer
 
 from sklearn.metrics.pairwise import cosine_similarity
 
 sent_tokens[0:2]
 
 GREETING_RESPONSES[0:4]
 
 def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
        
   import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id, voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',160)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("Hello Apoorv")


flag=True
    
speak("My name is Waris. I will answer your queries about Chatbots. If you want to exit, type Bye!")    
print("Sudo: My name is Waris. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Waris: You are welcome..")
            speak(" You are welcome..")
        else:
            if(greeting(user_response)!=None):
                gre =greeting(user_response)
                speak(gre)
                print("Waris: "+gre)
            else:
                print("Waris: ",end="")
                res=response(user_response)
                print(res)
                speak(res)
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Waris: Bye! take care..")
        speak("Bye! take care..")
        
   import speech_recognition as sr

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listen....")
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognix....")
        query=r.recognize_google(audio,Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

takeCommand()

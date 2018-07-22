from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
import requests
import json
import sys
import time
import itertools
import threading
import code
from pyfiglet import Figlet 


def error(word):
    if not word.isalpha():
        print("Please enter a valid word ")

#defining the animation
def the_process_function():
    n = 10
    for i in range(n):
        time.sleep(1)
        sys.stdout.write('\r'+'searching... \t process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
        sys.stdout.flush()
    sys.stdout.write('\r'+'searching... finished               \n')

def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'searching...'+char)
        time.sleep(.1)
        sys.stdout.flush() 

the_process = threading.Thread(name='process', target=the_process_function)




#Color printing with ANSI Escape sequence
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#Styles of Tokens
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#00FFFF',
    Token.Instruction: '', 
    Token.Answer: '#2196f3 bold',
    Token.Question: '#7FFF00 bold',
})



#App Login and API Keys Credential
app_id='c2d464e1'
app_key='89616b9e14d443bcdb7227e28d8287cf'

#For Pyliget
f=Figlet("small")

def intro():
    #intro screen
    print(" ")
    print(f.renderText("COMLID"))
    print(" ")
    prRed("WELCOME TO COMLID ")
    prLightPurple("Version = 1.0.0")
    prLightGray("Powered By Oxford Dictionary")

    print(" ")

def interface():
    questions1=[
    {
    'type':'input',
    'name': 'nam',
    'message':'Enter your name :'

    },
    {
        'type':'list',
        'name':'Choose',
        'message' : "Choose the one you want to do :", 
        'choices':['Dictionary','Translator','About'],
        'filter': lambda val: val.lower()
    }
    ]
    answers1=prompt(questions1,style=style)

    if(answers1["Choose"]=='dictionary'):
        print("\nHi, "+answers1["nam"]+" Welcome to COMMAND LINE Dictionary ")

        print(" ")
        questions2=[{
            'type': 'list',
            'name': 'lang',
            'message': 'Choose the Language of Word you want search: ',
            'choices': ['en','es','lv','hi','sw','ta','gu'],
            'default':'en'
        }]
        answers2=prompt(questions2,style=style)

        language=answers2["lang"]

        prPurple("\nEnter the word to be searched :")
        word_id=input()  
        error(word_id)



        url='https://od-api.oxforddictionaries.com:443/api/v1/entries/'+language+'/'+word_id.lower()

        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

        data=r.json()

        #triggering the animation
        the_process.start()
        while the_process.isAlive():
                animated_loading()

        word=data['results'][0]['id']
        lang=data['results'][0]['language']
        etymo=data['results'][0]['lexicalEntries'][0]["entries"][0]["etymologies"][0]
        meaning=data['results'][0]['lexicalEntries'][0]["entries"][0]["senses"][0]["definitions"][0]
        sht_def=data['results'][0]['lexicalEntries'][0]["entries"][0]["senses"][0]["short_definitions"][0]
        cate=data['results'][0]['lexicalEntries'][0]["lexicalCategory"][0]
        pron=data['results'][0]['lexicalEntries'][0]["pronunciations"][0]["phoneticSpelling"][0:]
        dilect=data['results'][0]['lexicalEntries'][0]["pronunciations"][0]["dialects"][0]

        print("\nWord searched : "+word)
        print("\nLanguage : "+lang)
        print("\nEtymologies : "+etymo)
        prLightPurple("\nMeaning of "+word+" is : "+meaning)
        prCyan("\nShort Defination : "+sht_def)
        prYellow("\nDialect : "+dilect)
        prGreen("\nPronouncation: "+pron)
        print(" ")

    elif(answers1["Choose"]=='translator'):
        print("\nHi, "+answers1["nam"]+" Welcome to COMMAND LINE Translator ")
        print(" ")

        questions3=[
            {
                'type':'list',
                'name':'cho1',
                'message':'Source Language: ',
                'choices':['en','es','ms','id','tn','ur','de','pt'],
                'default':'en'
            },
            {
                'type':'list',
                'name':'cho2',
                'message':'Target Language: ',
                'choices':['en','es'],  #,'ms','id','nso','tn','ur','de','pt'
                'default':'en'
            }
        ]
        answers3=prompt(questions3,style=style)

        source_language = answers3["cho1"]
        target_language = answers3["cho2"]


        prPurple("\nEnter the word to be translated :")
        word_id1=input()

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + source_language + '/' + word_id1.lower() + '/translations=' + target_language
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

        data1=r.json()


        trans=data1['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][0]["translations"][0]["text"][0:] #

        print("\nTranslated Word: ")
        prPurple(trans)

    else:
        print("\nThis CLI Dictionary cum Translator(COMmand Line Dictionary) is created by Ayan Bag")
        print("Current Version: 1.0.1")
        print("\nThis application is powered by Oxford Dictionary")

def end():
    questions4=[
    {
        'type': 'list',
        'name': 'toBeExit',
        'message': 'Do you want to exit? ',
        'choices':['Yes']
       
    }
    ]
    answers4=prompt(questions4,style=style)
    if(answers4['toBeExit']=='yes'):
        system.exit(1)

if __name__=="__main__":
    intro()
    interface()
    end()
    

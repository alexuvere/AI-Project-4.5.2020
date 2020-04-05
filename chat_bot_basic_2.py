# -*- coding: utf-8 -*-
"""Chat bot Basic 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YvQEJhCW3vMCAUNCTW_2GPjOwQ2-tS_4
"""

# description: this is a Chat Bot program

# import the library
from nltk.chat.util import Chat, reflections

pairs = [
         ['my name is (.*)', ['Hi %1']],
         ['(hi|hello|hey|holla|hola)', ['hey there', 'hi there', 'haayyy']],
        ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
         ['(.*)(location|city) ?', 'Tokyo, Japan'],
         ['(.*) created you ?', ['alexuvere@gmail.com did using NLTK']],
         ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
         ['(.*)help(.*)',  ['I can help you']],
         ['(.*) your name ?' , ['my name is J.A.R.V.I.S']]
]

reflections

my_dummy_reflections = {
    'go' : 'gone', 
    'hello' : 'hey there'
}

chat = Chat(pairs, my_dummy_reflections)
#chat._substitute('go hello')
chat.converse()






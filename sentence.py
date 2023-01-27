from random import sample
import pandas as pd
import numpy as np
import sys
import re
import random


pd.set_option('display.max_columns', None)

def analysis(filepath,word):
    df = pd.read_csv(filepath)
    data_list = df[df['singular'] == word]

    if len(data_list) == 0:
        print('没这个单词')
        return 0

    for index in data_list.index:
        subl,grammar,iobj,dobj,pobj,effect,sentence='','','','','','',''
        if 'effect' in df and str(df.at[index, 'effect']) != 'nan':
          effect = df.loc[index]['effect'].split(',')
          effect = sample(effect, k=1)

        if 'grammar' in df and str(df.at[index, 'grammar']) != 'nan':
          grammar = df.loc[index]['grammar'].split(',')
          grammar = sample(grammar, k=1)
          attend = ['where','what','why','whose','when','whom','which','how', '普通疑问句', '并列 and']  
          attend = sample(attend, k=1)
          if grammar[0] == 'subl + Link verb + predicative':
            grammar.append(attend[0])

        if 'dobj' in df and str(df.at[index, 'dobj']) != 'nan':
          #dobj = df.loc[index]['dobj'].split(',')

          dobj = re.split(r'[ ,]', df.loc[index]['dobj'])
          dobj = sample(dobj, k=1)
          attend = ['目的状语', '情态动词', '情态动词+疑问句',' ',' ',' ',' ']
          attend = sample(attend, k=1)
          dobj.append(attend[0])          
        if 'pobj' in df and str(df.at[index, 'pobj']) != 'nan':
          pobj = re.split(r'[ ,]', df.loc[index]['pobj'])
          # pobj = df.loc[index]['pobj'].split(',')
          pobj = sample(pobj, k=1)

        if 'sentence' in df and str(df.at[index, 'sentence']) != 'nan':
          sentence = df.loc[index]['sentence'].split(',')
          sentence = sample(sentence, k=1)

        print(effect,grammar,iobj,dobj,pobj,sentence)

    iobjdobj = data_list.to_string(columns=['iobjdobj'], index=False, header=False)
    iobjdobj = iobjdobj.split(',')
    pobj = sample(iobjdobj, k=1)
   # print('作双宾', iobjdobj)


def adj(filepath, word):
    df = pd.read_csv(filepath)
    df = df[df['adj'] == word]
   # df.drop(columns=['adj'], inplace=True)
   # df.dropna(axis=1, how='all', inplace=True)
    print(df)

def verb(filepath,word):
    df = pd.read_csv(filepath)
    df = df[df['verb'] == word]

    if len(df) == 0:
        print('没这个单词')
        return 0

    
    for index in df.index:
        subl,tense,iobj,dobj,effect,transformation,binbu=['  '],'','',[' '],'','',''
        if 'subl' in df and str(df.at[index, 'subl']) != 'nan':
          subllist = df.loc[index]['subl'].split(',')
          lens=len(subllist)
          subl = sample(subllist, k=1)

        if 'iobj' in df and str(df.at[index, 'iobj']) != 'nan':  
            iobj = df.loc[index]['iobj']

        if 'dobj' in df and str(df.at[index, 'dobj']) != 'nan':
          dobj = re.split(r'[ ,]', df.loc[index]['dobj'])
          dobj = sample(dobj, k=1)
        
        if  '宾补' in df and str(df.at[index, '宾补']) != 'nan':
          binbu = re.split(r'[ ,]', df.loc[index]['宾补'])
          binbu = sample(binbu, k=1)
        if 'transformation' in df and str(df.at[index, 'transformation']) != 'nan':
          tense = ['一般过去时','过去完成时','现在进行时','一般现在时','一般将来时']
          transformation = re.split(r'[ ,]', df.loc[index]['transformation'])
          verb = df.loc[index]['verb']
          transformation.append(verb)
          #transformation = sample(transformation, k=1)
          num = random.randint(0, 4)
          transformation = transformation[num]
          tense=tense[num]
        if 'effect' in df and str(df.at[index, 'effect']) != 'nan':  
            effect = df.loc[index]['effect']

        print(subl,tense,transformation,iobj,dobj,effect,binbu)
    df.drop(columns=['verb','tense','transformation','effect'],inplace=True,)
    df.dropna(axis=1,how='all', inplace=True)
    #df.drop(df.loc[df['transitive'] == 1], axis=1, inplace=True)
    print(df.to_string(index=False,))
   # print(subl,iobj,dobj,effect,transformation)
        

def human(filepath):
    df = pd.read_csv(filepath)
    singularlist,plurallist = [],[]

    for index in df.index:
        singularlist.append(df.loc[index]['singular'])
        plurallist.append(df.loc[index]['plural'])
    # print(singularlist)
    # print(plurallist)
    return singularlist,plurallist

def obj(filepath):
    df = pd.read_csv(filepath)
    singularlist,plurallist = [],[]
    for index in df.index:
        singularlist.append(df.loc[index]['singular'])
        plurallist.append(df.loc[index]['plural'])
    # print(singularlist)
    # print(plurallist)
    return singularlist,plurallist

def humanAndObject():

    singularlist, plurallist =  human(humanpath)
    singular = sample(singularlist, k=1)
    plural = sample(plurallist, k=1)
    objsingular, objplural = obj(objpath)
    objsingular = sample(objsingular, k=1)
    objplural = sample(objplural, k=1)
    print(singular,plural,objsingular,objplural)






if __name__ == "__main__":
    objpath='/Users/fire/Documents/note/nick-english/object.csv'
    verbpath='/Users/fire/Documents/note/nick-english/verb.csv'
    humanpath='/Users/fire/Documents/note/nick-english/human.csv'
    adjpath='/Users/fire/Documents/note/nick-english/adj.csv'

    word = sys.argv[1]
    tenselist=['现在进行时','一般现在时','一般过去时','一般将来时','现在完成时']

    #tense = sample(tenselist, k=1)
   # print(tense)
    #analysis(objpath,word)
    
    verb(verbpath,word)
    humanAndObject()
   # adj(adjpath,word)

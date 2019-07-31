import speech_recognition as sr
import os
import pyttsx3
from gtts import gTTS


def main():
    
    homedir = os.path.expanduser('~')
    
    x = '''style, aisle, bile, bille, cheil, chyle, 
    crile, deihl, dial, feile, geil, gile, gille,
    guile, guyle, heil, hile, hyle, i'll, isle, kile, 
    kyl, kyle, lile, lyle, mile, misle, niall, nile, pfeil,
    phile, phyle, pile, pyle, reihl, rile, ruyle,
    ryle, scyle, seil, sheil, smile, spile, stijl, 
    stile, style, theil, theile, tile, trial, triall, 
    vieil, vile, weil, weill, weyle, while,
    wile, wyle, zeile, zile ,abteil, affile,
    air mile, argyle, argyll, asile, awhile, 
    beguile, black bile, carlisle, carlyle, carwile,
    civile, compile, corbeil, corneille, cryophile, 
    defile, delisle, desfile, distyle, ensile, enstyle,
    erstwhile, esile, exile, fertile, freestyle, gentile, 
    hairstyle, hair style, half mile, hip tile, 
    hostile, infile, invile, in style, junk pile,
    kurzweil, land mile, lifestyle, life style
    , meanwhile, mikhail, misfile, monteil, 
    nevile, new style, odile, old style, orseille, 
    panfile, profile, quintile, refile, restyle, 
    revile, ridge tile, scibile, scissile, sea mile, 
    sedile, senile, senkbeil, sheath pile, sheet pile, 
    square mile, stockpile, sundial, tactile, textile,
    trash pile, turnstile, unfile, unpile, untile,
    vantuyl, wohlfeil, worthwhile, xenophile'''     
    flist=x.split(',')
    
    x='''bakery, beggary, breviary, celery, centaury,
    century, dentary, ectomy, emery, empery, every,
    factory, feathery, gregory, heathery, hennery, 
    history, kedgeree, leathery, lechery, memories,
    memory, mercury, mystery, penury, peppery, pessary,
    plenary, reverie, revery, sensory, septenary, severy,
    smeltery, treachery, treasuries, treasury, venery,
    victory,accessary, accessory, decennary, directories,
    dispensary, exemplary, lientery, mesentery, peremptory, 
    possessory, prebendary, preceptory, screen memory, subtreasury,
    suspensory, vasectomy, wild celery,tree'''
    dlist = x.split(',')
    
    dfc = 'Do you want to search for a directory or a file  ? '
    ob = gTTS(text=dfc,lang='en')
    ob.save("dfc.wav")
    os.system("mpg321 dfc.wav")
    dfr=getaudio()
    dfr = dfr.lower()
    print(dfr)
    if dfr in dlist:
        dirc = 'tell me the name of the directory .'
        ob = gTTS(text=dirc,lang='en')
        ob.save('dirc.wav')
        os.system('mpg321 dirc.wav')
        dirr = getaudio()
        dirr = dirr.lower()
        found = False
        for r,d,f in os.walk(homedir):
            for s in d:
                if s.lower() == dirr:
                    speakdir=os.path.join(r,s)
                    found=True
        if found:
            foundpath=' the directory is located at '+speakdir
            ob = gTTS(text=foundpath,lang='en')
            ob.save('foundpath.wav')
            os.system('mpg321 foundpath.wav')
        else:
            notfound = 'sorry ! could not find the directory'
            ob.gTTS(text=notfound,lang='en')
            ob.save('notfound.wav')
            os.system('mpg321 notfound.wav')
    
       
    elif dfr in flist:
        filnc = 'tell me the name of the file without the file extension'
        filnam = getaudio().lower()
        filec = 'tell me the extension of the file'
        filext = getaudio().lower()
        filfnam = '.'.join(filnam,filext)
        found = False
        for r,d,f in os.walk(homedir):
            for fl in f:
                if fl ==filfnam:
                    speakfile=os.path.join(r,fl)
                    found = True
        if found:
            text = "found file at"+speakfile
            ob = gTTS(text=text,lang='en')
            ob.save('foundfile.wav')
            os.system('mpg321 foundfile.wav')
        else:
            text = "sorry could not find the file . maybe case sensitivity is a issue"
            ob = gTTS(text=text,lang='en')
            ob.save('flienotfound.wav')
            os.system('mpg321 filenotfound.wav')
    else:
        print('Sorry ! could not complete your request')
    
def exc():
    print('Sorry ! could not make out what you said ')

def getaudio():
    r = sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        audio = r.listen(source)    
    response = r.recognize_google(audio)
    return response
main()

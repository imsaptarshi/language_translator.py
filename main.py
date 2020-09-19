def install(package):#to install required packages for running the code
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def listen():#taking command from user (speech to text)
    import pyaudio
    import speech_recognition as sr
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Speak.....\n")
        audio_data = r.listen(source)
        r.pause_threshold=1
        print("R e c o g n i z i n g . . . .\n")
        # convert speech to text
        try:
            text = r.recognize_google(audio_data)
        except:
            text = "Couldn't Recognise.."
    print("You Said     : "+text+"\n")
    return text
def speak(str):#speaking (text to speech)
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")#dispatching the voice of sapi
    speak.Speak(str)#making sapi speak the string passed to it
    print(str)
def bar():
    print("----------------------------------------------------------------------")
def get_languages():
    return (googletrans.LANGUAGES) # To return all the languages that google 
def get_key(key,my_dict):
    # list out keys and values separately 
    key_list = list(my_dict.keys()) 
    val_list = list(my_dict.values())
    #returning key of the value
    return (key_list[val_list.index(key)]) 
def translate(source_text:str,target_lang='en'):
    import googletrans#importing functions from googletrans
    bar()
    print(f"\nText detected             : {source_text} \n")
    translator=googletrans.Translator()#instance of Translator class
    languages=get_languages()
    try:
        source_lang=str(translator.detect(source_text).lang)
    except:
        print("Couldn't detect the language \n")
        again=input('Press Enter to exit\n')
    source_lang_formal=languages[source_lang]
    time.sleep(0.7)
    print(f"Source language dectected : {source_lang_formal} \n")
    bar()
    """In-function input"""
    try:
        target_lang=input("Enter the language you want to translate in : ")
        target_lang=target_lang.lower()
        bar()
        target_lang=get_key(target_lang,languages)
    except:
        true=True
        while true:
            print("Sorry, Language not found.\n")
            ex=input("Press Enter to exit\nPress 1 to select language again\nPress 2 to see supported languages\n")
            if '1' in ex:
                try:
                    target_lang=input("Enter the language you want to translate in : ")
                    target_lang=target_lang.lower()
                    bar()
                    target_lang=get_key(target_lang,languages)
                    true=False
                except:
                    pass
            elif '2' in ex:
                bar()
                langs=get_languages()
                val_list = list(langs.values())
                for lang in val_list:
                    print(lang)
                bar()
            else:
                exit()
    """In function input"""
    target_text=translator.translate(source_text,dest=target_lang).text
    target_lang_formal=languages[target_lang]
    time.sleep(0.7)
    print(f"\nTarget language detected : {target_lang_formal} \n")
    time.sleep(0.7)
    print(f"Translated to {target_lang_formal}    : {target_text} \n")
    return target_text
if __name__ == "__main__":
    print("Initializing.....")
    try:
        install('googletrans')
        install('pyaudio')
        install('pywin32')
        install('speechrecognition')
    except:
        e=input("\n\n=====================\nSome Modules Cannot be installed..\n=====================\nPress enter to exit.")
        quit()
    try:
        import time
        import googletrans#importing functions from googletrans
    except:
        e=input("\n\n=====================\nSome Modules Cannot be installed..\n=====================\nPress enter to exit.")
        quit()

    
    ex='1'
    while '1' in ex:
        bar()
        user_choice=input("\nChoose..\nPress 1 - Speak your words or sentence\nPress 2 - Enter text manually\nPress 3 - Read from source.txt\n")
        print('\n')
        bar()
        if '3' in user_choice:
            print("\nReading source.txt...")
            time.sleep(0.7)
            source_file=open('C:\\Users\\HP\\Desktop\\PROJECTS\\Language_Translation_App\\source.txt','r')
            target_file=open('C:\\Users\\HP\\Desktop\\PROJECTS\\Language_Translation_App\\target.txt','r+')
            source_text=source_file.read()
            target_text=translate(source_text)
            target_file.write(target_text)
            time.sleep(0.7)
            print('target.txt successsfully updated!')
            bar()
            ex=input('\nPress 1 - Try again\nPress 2 - to hear the translation\nPress Enter to quit\n')
            if '2' in ex:
                speak(target_text)
                ex=input('\nPress 1 - Try again\nPress Enter to quit\n')
        elif '2' in user_choice:
            source_text=input("Enter your text you want to translate : ")
            time.sleep(0.7)
            target_text=translate(source_text)
            bar()
            ex=input('\nPress 1 - Try again\nPress 2 - to hear the translation\nPress Enter to quit\n')
            if '2' in ex:
                speak(target_text)
                ex=input('\nPress 1 - Try again\nPress Enter to quit\n')
        elif '1' in user_choice:
            source_text=listen()
            target_text=translate(source_text)
            bar()
            ex=input('\nPress 1 - Try again\nPress 2 - to hear the translation\nPress Enter to quit\n')
            if '2' in ex:
                speak(target_text)
                ex=input('\nPress 1 - Try again\nPress Enter to quit\n')
        else:
            bar()
            ex=input('Wrong choice \nPress 1 - Try again\nPress Enter to quit\n')
            if '1' not in ex:
                exit()
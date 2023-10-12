import requests 
import customtkinter


win = customtkinter.CTk()
win.geometry('1400x1000')
win.title('Translation Application')

# Main Class Container 
class main():
    def __init__(self,text,):
        self.text = text

    def detect(self):
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

        payload1 = { "q": self.text }
        headers1 = {
	        "content-type": "application/x-www-form-urlencoded",
	        "Accept-Encoding": "application/gzip",
	        "X-RapidAPI-Key": "9c6b0f569dmshd2a3fe04a9d7209p147fc9jsn11f8f4b224c9",
	        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }
        response = requests.post(url, data=payload1, headers=headers1)
        print(response.json())


    def target(self):
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = {
	        "q": self.text,
	        "target": "es",
	        "source": "en"
        }
        headers = {
	        "content-type": "application/x-www-form-urlencoded",
	        "Accept-Encoding": "application/gzip",
	        "X-RapidAPI-Key": "9c6b0f569dmshd2a3fe04a9d7209p147fc9jsn11f8f4b224c9",
	        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }
        response = requests.post(url, data=payload, headers=headers)    
        print(response.json())

# Users Input
def return_key(event):
    global userText
    userText = textEntry.get()
    win.focus_set()

    # Main Class Container
    input = main(userText)
    input.detect()
    input.target()

# VIEWS 
    # background Frames
leftFrame = customtkinter.CTkFrame(win,
                                   width= 400, 
                                   height= 500, 
                                   corner_radius= 15,
                                   fg_color='grey'
                                   )
leftFrame.place(relx=0.3, rely=0.55, anchor=customtkinter.CENTER)

rightFrame = customtkinter.CTkFrame(win,
                                   width= 400, 
                                   height= 500, 
                                   corner_radius= 15,
                                   fg_color='grey'
                                   )
rightFrame.place(relx=0.7, rely=0.55, anchor=customtkinter.CENTER)
    # labels 
titleLabel = customtkinter.CTkLabel(win,
                                    text= "Translate Any Language ... (Almost)",
                                    )
titleLabel.place(relx=0.5, rely=0.10, anchor=customtkinter.CENTER)
titleLabel.configure(font=('Georgia bold',40))

    # User Text Input
textEntry = customtkinter.CTkEntry(win, 
                                  placeholder_text='Enter text to translate',
                                  bg_color= 'grey',
                                  fg_color= 'grey97',
                                  text_color='black',
                                  placeholder_text_color='black',
                                  justify= 'center',
                                  width= 380,
                                  height= 480                                     
                                  )
textEntry.place(relx=0.3, rely=0.55, anchor=customtkinter.CENTER)
textEntry.bind('<Return>', return_key)

win.mainloop()

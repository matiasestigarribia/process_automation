import time
import pyautogui

def process_automation(software):
    try:
        #open software
        pyautogui.hotkey('win', 'r')
        pyautogui.write(software + ".exe")
        pyautogui.press('enter')
        
        #wait time for software to open
        time.sleep(2)
        
        #writing on software
        message = "Process automation with Python and pyautogui succesfull"
        pyautogui.write(message)
        print("Message written in", software, "window.")

        #saving arquive
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.write("automatic_file_" + time.strftime("%d%m%Y"))  #name of the file with date
        pyautogui.press('enter')
        
        print("File succesfully saved on " + software + " under automatic_file_" + time.strftime("%d/%m/%Y"))

        time.sleep(1)
        
        pyautogui.hotkey('alt', 'f4')   #close window
        
        print("Window closed successfully!")
        
    except:
        
        print("An error ocurred while trying to access ", software)
    
if __name__ == "__main__":
    process_automation("Notepad")   #you can change Notepad for other text editor
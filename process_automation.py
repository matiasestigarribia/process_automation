import time
import pyautogui
import logging


class ProcessAutomation():
    
    def  __init__(self):
        pyautogui.FAILSAFE=True
        self.message = "Process automation with Python and pyautogui succesfull"
        logging.basicConfig(
                    filename = 'my_log.log',
                    level = logging.INFO,
                    filemode =  'w',
                    format = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
)
    
    def open_soft(self, software):
        pyautogui.hotkey('win', 'r')
        pyautogui.write(software + ".exe")
        pyautogui.press('enter')
        
        #wait time for software to open
        time.sleep(2)
    def write_message(self, software):
        pyautogui.write(self.message)
        logging.info("Message written in" + software + "window.")
        
    def save_arquive(self, software):
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.write("automatic_file_" + time.strftime("%d.%m.%Y"))  #name of the file with date
        pyautogui.press('enter')
        
        logging.info("File succesfully saved on " + software + " under automatic_file_" + time.strftime("%d.%m.%Y"))
        

        time.sleep(1)
        
        pyautogui.hotkey('alt', 'f4')   #close window
        
        
        logging.info("Window closed successfully!")
    def process_automation(self, software):
        self.open_soft(software)
        self.write_message(software)
        self.save_arquive(software)
        ...
        
if  __name__ == "__main__":
    myProcess = ProcessAutomation()
    myProcess.process_automation("Notepad")
    
    
 


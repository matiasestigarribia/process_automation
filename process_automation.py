import time
import pyautogui
import logging
import os
from config import SLEEP_TIMES


class ProcessAutomation():
    
    def  __init__(self):
        pyautogui.FAILSAFE=True
        self.message = "Process automation with Python and pyautogui succesfull"
        self.project_directory = os.path.dirname(os.path.abspath(__file__))
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
        
        
        time.sleep(SLEEP_TIMES['open_software'])
    def write_message(self, software):
        pyautogui.write(self.message)
        logging.info("Message written in " + software + " window.")
    
    def check_and_modify_file_name(self, file_name):
        i=1
        while os.path.exists(os.path.join(self.project_directory, file_name)):
            logging.warning("File name already exist")
            file_name = file_name[:-4] + "_" + str(i) + file_name[-4:]
            i+=1
        return file_name
    
    def save_arquive(self, software, save_path=None):
        if save_path is None:
            save_path = os.path.join(self.project_directory)
        
        pyautogui.hotkey('ctrl', 's')
        
        
        #comprobar si o nome de arquivo ja existe
        file_name = "automatic_file_" + time.strftime("%d.%m.%Y" + ".txt")
        file_name = self.check_and_modify_file_name(file_name)
        
        
        file_path = os.path.join(save_path, file_name)
        pyautogui.write(file_path)  
        pyautogui.press('enter')
        time.sleep(SLEEP_TIMES['save_file'])
        
        logging.info("File succesfully savedd on " + software + " under " + file_name)
        
        time.sleep(SLEEP_TIMES['close_window'])
        logging.info("Automation completed successfully!")
        pyautogui.hotkey('alt', 'f4')   #close window
     

    def process_automation(self, software):
        self.open_soft(software)
        self.write_message(software)
        self.save_arquive(software)
        
        
if  __name__ == "__main__":
    myProcess = ProcessAutomation()
    myProcess.process_automation("Notepad")
    
    
 


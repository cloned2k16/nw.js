import time
import os
import platform
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nw_util import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("nwapp=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
driver.implicitly_wait(10)
time.sleep(1)
try:
    print driver.current_url
    wait_window_handles(driver, 2)
    print 'close windows in reversed order'
    for handle in reversed(driver.window_handles):
        driver.switch_to_window(handle)
        driver.close()
        
    time.sleep(3) # wait for quit
    assert(no_live_process(driver))
    
finally:
    driver.quit()

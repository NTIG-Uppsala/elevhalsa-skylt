import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Bredden av webbläsaren
WIDTH = 1366

# Höjden av webbläsaren
HEIGHT = 768

chrome_options = Options()

# Lägger till ett argument för att webbläsaren inte ska ha ett synligt fönster
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("{}/../Skylt/index.html".format(os.getcwd()))

driver.set_window_size(WIDTH, HEIGHT)

carousel = driver.find_element_by_class_name("carousel")

# Räknar ut hur länge som sidan stannar på en slide
slide_interval = int(carousel.get_attribute("data-interval")) / 1000

# Specifierar antalet slides på sidan
slide_count = len(carousel.find_elements_by_xpath("ol/li"))

# Specifierar hur länge som programmet ska försöka hitta element på sidan
driver.implicitly_wait(slide_interval)

# Skapar en mapp för screenshots om den inte redan existerar
if not os.path.exists("screenshots"):
	os.mkdir("screenshots")

for i in range(slide_count):
	# Försöker hitta slide med klassen "active"
	carousel.find_element_by_xpath("ol/li[@data-slide-to='{}'][@class='{}']".format(i, "active"))

	# Väntar på att övergången till sliden blir klar
	time.sleep(0.5)

	# Sparar en skärmbild av sliden
	driver.save_screenshot(str.format("screenshots/slide_{}.png", i))

# Stänger webbläsaren
driver.close()
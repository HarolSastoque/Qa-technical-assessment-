from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Iniciar navegador
driver = webdriver.Chrome()  # Asegúrate de tener chromedriver en PATH
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Cerrar el banner si aparece
try:
    close_ad = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "close-fixedban"))
    )
    close_ad.click()
except:
    pass
try:
    close_ad = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "close-fixedban"))
    )
    close_ad.click()
except:
    pass


time.sleep(3)
driver.execute_script("""
    let ad = document.getElementById('fixedban');
    if (ad) { ad.remove(); }
    let footer = document.querySelector('footer');
    if (footer) { footer.remove(); }
""")



# Llenar campos
driver.find_element(By.ID, "firstName").send_keys("Harol")
driver.find_element(By.ID, "lastName").send_keys("Sastoque")
driver.find_element(By.ID, "userEmail").send_keys("harol.sastoque@example.com")

time.sleep(5)
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Número de teléfono
driver.find_element(By.ID, "userNumber").send_keys("3216549870")

# Fecha de nacimiento
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1995")
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("Febreaury")
driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()

# Materias
materia = driver.find_element(By.ID, "subjectsInput")
materia.send_keys("Math")
materia.send_keys(Keys.ENTER)

# Seleccionar hobby
time.sleep(3)
try:
   driver.find_element(By.XPATH, "//label[text()='Reading']").click()
except:
    
    driver.find_element(By.XPATH,'//*[@id="hobbiesWrapper"]/div[2]/div[2]/label/text()').click()
# Dirección
driver.find_element(By.ID, "currentAddress").send_keys("Calle 123, Bogotá")

# Scroll hacia abajo para ver estado/ciudad
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Seleccionar estado
driver.find_element(By.ID, "state").click()
driver.find_element(By.XPATH, "//div[text()='NCR']").click()
    
# Seleccionar ciudad
driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

# Enviar formulario
driver.find_element(By.ID, "submit").click()


time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="closeLargeModal"]').click()

print("Enviado el formulario")

driver.close()


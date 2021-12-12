import selenium.webdriver
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture # dupa aceasta stie sa mearga in metoda browser care este o configurare a testelor
def browser():
    # initializam instanta de Chromedriver, se deschide tab-ul de chrome
    b = selenium.webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # dupa ce am dat yield ne intoarce ca si o variabila, pana la yield e ce vrem sa facem inainte de fiecare test
    yield driver

    driver.quit()

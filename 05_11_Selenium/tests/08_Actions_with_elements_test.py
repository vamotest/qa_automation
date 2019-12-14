from locators.drag_and_drop import DragAndDrop
from selenium.webdriver.common.action_chains import ActionChains


def test_drag_and_drop(browser):
    """
    Перетаскивание документов в корзину
    :param browser:
    """

    # Открываем страницу с корзиной и документами:
    url = 'https://marcojakob.github.io/dart-dnd/basic'
    browser.wd.get(url)

    # Определяем местоположение элементов на странице:
    documents = browser.wd.find_elements(*DragAndDrop.document)
    trash = browser.wd.find_element(*DragAndDrop.trash)

    # С помощью, ActionChains перетаскиваем каждый документы в корзину:
    for document in documents:
        actions = ActionChains(browser.wd)
        actions.drag_and_drop(document, trash).perform()

    # Закрываем браузер:
    browser.quit()

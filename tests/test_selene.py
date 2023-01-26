import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene.support import by
from selene.support.conditions import be


def test_github():
    with allure.step("открываем главную страницу"):
        browser.open("https://github.com/")
    with allure.step("ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()
    with allure.step("переходим в репозиторий"):
        s(by.link_text('eroshenkoam/allure-example')).click()
        s("#issues-tab").click()
    with allure.step("проверяем наличие issues 76"):
        s(by.partial_text("#76")).should(be.visible)

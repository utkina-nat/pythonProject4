from selene import be, have
from selene.support.shared import browser


browser.open('https://google.com/ncr')
browser.element('[name = "q"]').should(be.blank).type('selene').press_enter()
browser.element('[id="search"]').should(have.text("yashaka/selene: User-oriented Web UI browser tests in ..."))

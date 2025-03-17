import time
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from RPA.Desktop import Desktop

browser = Selenium()
browser.open_browser(browser='chrome')
browser.driver.maximize_window()
browser.driver.delete_all_cookies()
output_dir = "./output/sc"
desktop = Desktop()


@task
def open_chrome_full_screen():
    browser.go_to("https://avatarux.com")
    browser.wait_until_element_is_visible("id:ageOver")
    browser.click_element("id:ageOver")
    browser.wait_until_element_is_visible("xpath:/html/body/div[3]/div/div/div/div[2]/button[3]")
    browser.click_element("xpath:/html/body/div[3]/div/div/div/div[2]/button[3]")
    browser.wait_until_element_is_visible('xpath://*[@id="menu-item-4999"]/div/a')
    browser.mouse_over('xpath://*[@id="menu-item-4999"]/div/a')
    browser.wait_until_element_is_visible('xpath://*[@id="menu-item-4999"]/div/div/a[1]')
    browser.wait_until_element_is_visible('xpath://*[@id="menu-item-4999"]/div/div/a[3]')
    browser.click_element('xpath://*[@id="menu-item-4999"]/div/div/a[3]')
    browser.wait_until_element_is_visible('xpath://*[@id="acf-block-colored-heading-block_85a638f5b79a19306f22aafe3acb285d-heading"]/h2/span')
    for _ in range(30):
        browser.press_keys(None, 'DOWN')
    browser.wait_until_element_is_visible('css:html.wf-lexend-n1-active.wf-lexend-n4-active.wf-lexend-n5-active.wf-lexend-n6-active.wf-lexend-n7-active.wf-lexend-n9-active.wf-epilogue-n4-active.wf-epilogue-n6-active.wf-active body.page-template-default.page.page-id-6412.page-child.parent-pageid-4992.page-theme-dark.mm-wrapper div#mm-0.mm-page.mm-slideout div.main-content main#main section#acf-block-games-slider-block_9dc69be3305e2c49fcf5f42ed4c038df.acf-block-games-slider div.container.position-relative.c-mt-5 div.position-relative.overflow-hidden div#tns1-ow.tns-outer div#tns1-mw.tns-ovh div#tns1-iw.tns-inner div#tns1.game-preview__slider-wrapper.d-flex.position-relative.js-games-slider.tns-slider.tns-carousel.tns-subpixel.tns-calc.tns-horizontal div#tns1-item0.game-preview.game-preview--dark.tns-item.tns-slide-active div.game-preview__content-wrapper.c-mx-2.c-p-4.position-relative div.game-preview__buttons.d-flex.flex-xl-row.justify-content-between.align-items-start.align-items-xl-end.c-mt-5.flex-row.flex-sm-column button.crunch-button.crunch-button__full-background.crunch-button__full-background--with-icon.crunch-button__full-background--with-icon--left.crunch-button__full-background--small.js-iframe-modal-trigger')
    browser.click_element('css:html.wf-lexend-n1-active.wf-lexend-n4-active.wf-lexend-n5-active.wf-lexend-n6-active.wf-lexend-n7-active.wf-lexend-n9-active.wf-epilogue-n4-active.wf-epilogue-n6-active.wf-active body.page-template-default.page.page-id-6412.page-child.parent-pageid-4992.page-theme-dark.mm-wrapper div#mm-0.mm-page.mm-slideout div.main-content main#main section#acf-block-games-slider-block_9dc69be3305e2c49fcf5f42ed4c038df.acf-block-games-slider div.container.position-relative.c-mt-5 div.position-relative.overflow-hidden div#tns1-ow.tns-outer div#tns1-mw.tns-ovh div#tns1-iw.tns-inner div#tns1.game-preview__slider-wrapper.d-flex.position-relative.js-games-slider.tns-slider.tns-carousel.tns-subpixel.tns-calc.tns-horizontal div#tns1-item0.game-preview.game-preview--dark.tns-item.tns-slide-active div.game-preview__content-wrapper.c-mx-2.c-p-4.position-relative div.game-preview__buttons.d-flex.flex-xl-row.justify-content-between.align-items-start.align-items-xl-end.c-mt-5.flex-row.flex-sm-column button.crunch-button.crunch-button__full-background.crunch-button__full-background--with-icon.crunch-button__full-background--with-icon--left.crunch-button__full-background--small.js-iframe-modal-trigger')
    time.sleep(10)

@task
def navigate_to_the_game():
    browser.set_screenshot_directory(output_dir)
    browser.set_focus_to_element("id:js-modal-iframe")
    browser.capture_element_screenshot("id:js-modal-iframe")
    browser.click_element("id:js-modal-iframe")
    browser.capture_element_screenshot("id:js-modal-iframe")

@task
def browse_game_info():
    # Open up Game Settings
    desktop.click("point:1680,1046")
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    # Game Info menu and scroll down game iframe and web page
    desktop.click("point:1560,880")
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    desktop.click("point:1560,880")
    for _ in range(1000):
        browser.press_keys(None, 'DOWN')
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    # Close Game Info
    desktop.click("point:1720,640")
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    time.sleep(5)
   
@task
def browse_game_rules():
    # Open up Game Settings and Game Rules 
    desktop.click("point:1680,1046")
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    desktop.click("point:1560,955")
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    desktop.click("point:1560,880")
    for _ in range(1000):
        browser.press_keys(None, 'DOWN')
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    # Close Game Rules
    desktop.click("point:1720,640")
    time.sleep(5)
    browser.capture_element_screenshot("id:js-modal-iframe")
    time.sleep(5)



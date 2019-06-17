from crawl.screen_shot import *
from selenium import webdriver


def get_browser(url: str) -> RemoteWebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('lang=zh_CN.UTF-8')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    rect = browser.get_window_rect()
    size = browser.get_window_size()

    print('rect: {}, size: {}'.format(rect, size))
    return browser


if __name__ == '__main__':
    browser = get_browser('https://tushare.pro/document/2?doc_id=33')

    # 移除悬浮
    browser.execute_script("""
    var toTop = document.querySelector('.scroll-to-top');
    if(toTop){
    toTop.remove();
    }
    """)

    # 隐藏滚动条
    browser.execute_script("""
    var style = document.createElement('style');
    style.innerHTML='body::-webkit-scrollbar{display:none;}';
    document.querySelector('head').append(style);
    """)
    screen_shot = ScreenShot()
    screen_shot.save_full_page_screen_shot('ts.jpg', browser=browser)
    browser.quit()

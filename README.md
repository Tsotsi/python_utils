# python-utils

python utils


### ScreenShot

```python3
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
```

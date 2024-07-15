import webbrowser

# 열고 싶은 URL 리스트
urls = [
    "http://naver.com",
    "http://google.com",
    "http://youtube.com"
]

# 각 URL을 새로운 탭에서 열기
for url in urls:
    webbrowser.open_new_tab(url)

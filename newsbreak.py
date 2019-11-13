import time
import webbrowser

news_site = 'http://bbc.com'
interval = 10*60  # Interval (min*sec) between page refreshes
breaks_wanted = 32  # How many times the page should be reloaded

# DO NOT MODIFY ANYTHING UNDER THIS LINE --------------------------
breaks_taken = 0
print("News Break V1.0 | Started at " + time.ctime())
print("Interval is :" + str(interval) +"s")

while breaks_taken < breaks_wanted:
    webbrowser.open(news_site, new=0, autoraise=True)
    breaks_taken += 1
    time.sleep(interval)

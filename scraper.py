import scraperwiki
html = scraperwiki.scrape('https://inmo.ie/6022')
import lxml.html
root = lxml.html.fromstring(html)
tds = root.cssselect('td')
for td in tds:
    print td.text_content()
for td in tds:
    record = { "td" : td.text_content() }
    scraperwiki.sqlite.save(["td"], record)

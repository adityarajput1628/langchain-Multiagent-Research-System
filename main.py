from src.tools.tools import web_search, scrape_url

output = web_search.invoke("what is country wuth most population")
print(output)
scrape_url_output = scrape_url("https://en.wikipedia.org/wiki/List_of_capitals_of_France")
print(scrape_url_output)
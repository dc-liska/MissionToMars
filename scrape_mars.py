#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd


# NASA Mars News

# In[2]:


#Scrape the NASA Mars News Site ( https://mars.nasa.gov/news/ ) and collect the latest News Title and Paragraph Text.
def get_Mars_News():
    def init_browser():
        executable_path = {"executable_path": "resources/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

    browser = init_browser()

    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find_all("div", class_="content_title")[0].get_text()
    news_text = soup.find("div", class_="article_teaser_body").get_text()

    #print(news_title)
    #print(news_text)
    news_results= [news_title,news_text]
    return news_results


# Mars Featured Image

# In[3]:


#Visit https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars for JPL Featured Space Image and use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
def get_featured_image():
    featured_pic_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_pic_url)

    html = browser.html
    soup = bs(html, "html.parser")

    base_image_URL="https://www.jpl.nasa.gov"

    #Featured Image identifying markup
    featured_image_hypertext = soup.find("div", class_="carousel_items").find("article")["style"]
    featured_image_parts = featured_image_hypertext.split("'")

    featured_image = featured_image_parts[1]
    featured_image_URL= str(base_image_URL) + str(featured_image)
    #print(featured_image_URL)
    return featured_image_URL


# Mars Weather

# In[4]:


#Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars
#weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
def get_Mars_Weather():
    latest_mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(latest_mars_weather_url)

    html = browser.html
    soup = bs(html, "html.parser")

    latest_mars_weather = soup.find_all("p", class_="js-tweet-text")[0].get_text()

    latest_mars_weather = latest_mars_weather.split("pic.")
    mars_weather = latest_mars_weather[0]
    #print(mars_weather)
    return mars_weather


# Mars Facts

# In[7]:


#Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing
#facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.
def get_Mars_Facts_Table():
    mars_facts_url = "https://space-facts.com/mars/"

    facts_table = pd.read_html(mars_facts_url)[0]
    mars_facts_html_table = facts_table.to_html()

    #print(mars_facts_html_table)
    return mars_facts_html_table


# Mars Hemispheres

# In[ ]:


def get_Mars_Hemisphere_Images():
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]
    return hemisphere_image_urls


# In[ ]:


def scrape():
    
    scraped_data = {}
    mars_news_results = get_Mars_News()
    mars["mars_news_title"] = mars_news_results[0]
    mars["mars_news"] = mars_news_results[1]
    mars["mars_featured_image"] = get_featured_image()
    mars["mars_weather"] = get_Mars_Weather()
    mars["mars_facts"] = get_Mars_Facts_Table()
    mars["mars_hemisphere_images"] = get_Mars_Hemisphere_Images()

    return scraped_data


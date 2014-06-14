Procurement Data Scraper
=========================

Scraper for DC Data Sprint: Indian Procurement at Tenders.Gov.IN


#Usage

    > python scraper.py <choice> <tid>
    
The scraper works on pages of the form: `http://tenders.gov.in/innerpage.asp?choice=tc5&tid=karn665134&work=1` where tid and choice need to go into the command line for the scraper.  

####Example

    > python scraper.py  tc5 karn665134

Output is JSON.  If a list of every tid and choice combination can be found, we can do a scraper to pull the complete dataset.







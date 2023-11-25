# Restaurant Scraper

A Scraper that extract information about Restaurants (Name and Rating).

## How to Use it

1. Clone the repo
```
    git clone {}
    cd {}
```

2. Create Virtual Environment using Python's `venv` module
```
    python -m venv scrape-env

    # for linux and mac
    source ./scrape-env/Scripts/activate 
    
    # for windows (batch)
    ./scrape-env/Scripts/activate.bat

    # for windows (powershell)
    ./scrape-env/Scripts/activate.ps1

```

3. Install Dependencies 
```
    pip install -r requirements.txt
```

4. Edit the information in the `scraper.py` file.  
        - Change the URL to whichever review webpage you want scrape. It should a list of restaurants with its rating.  
        - Assing the CSS Selectors for the restaurant's name and restaurant's rating.  
        - Use the `scrape_page(.)` function to scrape the page.  
        - Don't Chage the code in the mentioned areas.

5. Run the Script. 
```
    python scraper.py
```

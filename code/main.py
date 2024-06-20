
from yahoo_finance import YahooFinance

def main(region: str):
    
    yahoo_finance = YahooFinance("https://finance.yahoo.com/screener/new")
    yahoo_finance.filter_by_region(region)

if __name__ == '__main__':
    main("Brazil")
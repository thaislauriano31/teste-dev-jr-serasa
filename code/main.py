
from classes.yahoo_finance import YahooFinance

def main():
    region = input(
        "Qual região você deseja usar como filtro?\n(Escreva o nome como está no site, por favor)\n"
        ).strip().title()
    yahoo_finance = YahooFinance("https://finance.yahoo.com/screener/new")
    yahoo_finance.get_stocks(region)

if __name__ == '__main__':
    main()
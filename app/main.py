import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  ->sin pandas<-
  data = read_csv.read_csv('app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  #->Con pandas<-
  df=pd.read_csv('data.csv')
  data=df[df['Continent']== 'Europe']
  countries=data['Country'].values
  percentages=data['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
    '''
if __name__ == '__main__':
  run()
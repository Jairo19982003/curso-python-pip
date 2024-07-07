import utils 
import read_csv
import charts
import pandas as pd  # type: ignore

def run():
  '''
  data = list(filter(lambda item: item['Continent']=='North America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent']=='Africa']

  countries = df['Country/Territory'].values
  percentages = list(df['World Population Percentage'])
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Digite el pais por favor  =>: ')
  print(country)
  
  result = utils.population_by_country(data, country)

  if len(result)>0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels, values)
  
  
if __name__== '__main__':
  run()
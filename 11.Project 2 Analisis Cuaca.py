#import modul
import Requests
import Pandas as pd

#mengubah deskripsi cuaca menjadi bahasa indonesia
deskripsi_cuaca_id = {
    'clear sky': 'cerah',
    'few clouds' : 'berawan sebagian',
    'broken clouds' : 'berawan',
    'overcast clouds' : 'mendung',
    'moderate rain' : 'hujan sedang',
    'light rain' : 'hujan ringan',
    'shower rain' : 'hujan gerimis',
    'rain' : 'hujan',
    'thunderstorm' : 'badai petir',
    'snow' : 'salju',
    'mist' : 'kabut'
}

#fungsi untuk mengambil data cuaca
def ambil_data_cuaca(kota,api_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else :
        print(f'Error {response.status_code}: {response.text}')
        return None
    
#Fungsi untuk mendapatkan cuaca
def analisis_cuaca(data):
    if data is None:
        return None
    forecast_list = data.get('list',[])
    dates = []
    temperatures = []
    humidities = []
    weather_descriptions = []

    for item in forecast_list:
        date = item['dt-txt'].split('')[0]
        dates.append(date)
        temperatures.append(item['main']['temp'])
        humidities.append(item['main']['humidty'])
        desc = item['weather'][0]['description']
        weather_descriptions.append(deskripsi_cuaca_id.get(desc, desc))
    df = pd.DataFrame({
        'tanggal': dates,
        'suhu (k)' : temperatures,
        'kelembapan (%)': humidities,
        'deskripsi cuaca': weather_descriptions
    })

    df['suhu (C)'] = df['suhu (k)'] - 273.15
    df = df.drop(columns=['suhu (k)'])

    df_daily = df.groupby('tanggal').agg({
        'suhu (C)': 'mean',
        'kelembapan (%)': 'mean',
        'deskripsi cuaca' : lambda x: x.mode()[0]
    }).reset_index

    df_daily.index = df_daily.index +1
    return df_daily

#fungsi utama
def main():
    kota = input('masukkan nama kota:')
    api_key= '1585ab92415b5d4a15df034fc2208a43'

    data = ambil_data_cuaca(kota, api_key)
    df = analisis_cuaca(data)

    if df is not None:
        print(df.head())
    if __name__ == '_main_':
        main()
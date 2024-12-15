import requests
import json

YEAR = 2022
def get_url(i):
    return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/UHqzLeAl/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217728X0X1048578X0X0X1024X18464X131072X256X0X0X0X0X0X0X128/1/0/page/{i}/?_=1734122814493'
    #return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/vJuMPo6c/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/2/page/{i}/?_=1724956755698'
    #return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/zoZ4r7jR/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/0/page/{i}/?_=1724676234926'
    #return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/jDTEm9zs/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/0/page/{i}/?_=1724670227066'
    #return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/nmP0jyrt/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/0/page/{i}?_=1724668051063'
    #return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/tdkpynmB/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/0/page/{i}?_=1724622553073'
    #return f'https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/AJuiuwWt/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/0/page/{i}/?_=1724615445286'
    #return f"https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/h2NtrDMq/X360488X0X0X0X0X0X0X0X0X0X0X0X0X134217729X0X1048578X0X0X1024X18464X131072X256/1/0/page/{i}/?_=1724614515712"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,hr;q=0.8,sl;q=0.7',
  'content-type': 'application/json',
  #'cookie': 'OptanonAlertBoxClosed=2024-08-25T19:27:12.932Z; eupubconsent-v2=CQD527AQD527AAcABBENBDFsAP_gAAAAAChQKBNV_G__bWlr8X73aftkeY1P99h77sQxBhfJE-4FzLuW_JwXx2ExNA36tqIKmRIAu3bBIQNlGJDUTVCgaogVryDMakWcgTNKJ6BkiFMRO2dYCF5vmwtj-QKY5vp991dx2Bet7dr83dzyz4VHn3a5_2a0WJCdA58tDfv9bROb-9IOd_x8v4v0_F_rE2_eT1l_tevp7B8-cts79XW-9_fff79LAAAAIEgAgLzHQAQF5koAIC8ykAEBeYAA.f_wAAAAAAAAA; _ga=GA1.1.2090758140.1724614022; lux_uid=172461439061767649; op_cookie-test=ok; op_user_time=1724614390; op_user_cookie=9517503783; op_user_hash=87ab7345a2ec60ad3de098d2231e01c3; op_user_time_zone=2; op_user_full_time_zone=37; _sg_b_n=1724614481658; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Aug+25+2024+21%3A35%3A08+GMT%2B0200+(Central+European+Summer+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=20e06168-ffc5-4dd4-9c91-4f66a4cbf874&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CV2STACK42%3A1&hosts=H194%3A1%2CH302%3A1%2CH236%3A1%2CH198%3A1%2CH203%3A1%2CH190%3A1%2CH301%3A1%2CH303%3A1%2CH304%3A1%2CH230%3A1%2CH305%3A1&genVendors=V2%3A1%2C&AwaitingReconsent=false&geolocation=RS%3B00; XSRF-TOKEN=eyJpdiI6IlpvQnBvVG9DTnE5WXVuR3ltU29zZFE9PSIsInZhbHVlIjoiSHErTmVGM1pGdWpkbmc1UHErYWFWQW5QOEtSSEN4djVwaTZ6NmRnTXhEUTBVbzJqTXBreVNFM1FjWTBFYUl4WlRWY2NqM2xjcmJpMFFyNDZUWndpM1BQYXBILy9rd1dpeHJ6dFU2MWlscG5uUmZXVG55SjlwQnlVZU5kNGp2UTQiLCJtYWMiOiI1NDQwMjM4NjU0ZGE4NGQyMTkxYTA2MjNiODQzZDk5ZjdhMjJmMWQ3NGYxZTA3ZTI5MzFhOGIzNGRmMDFjZjk2IiwidGFnIjoiIn0%3D; oddsportalcom_session=eyJpdiI6IlFiTXhyYzUvSklCMURsbmdMb0VJcWc9PSIsInZhbHVlIjoieksydnVLNk0wcDUzK2I2SWUwaTQ4VUc2TktqQnVmZ01EL3dhMTNQTlhJUU16djJXczFCZ3BFNFVUTWMvNFZobm5ERVZEMXJNOWIzT28wUXFFY0liYXpGeVdyOGlZa1hQQWo1QmRySXBHVGphVW1UUEFjbmMrRlQ5TzVCcWhGVDAiLCJtYWMiOiI1YjU0YjkzZWI5YjZjOWJmZjY2MDE0OTg2MGY5NGNhMDMzMzNkY2VkMTNlYTE5MGI4NzY4N2Y0NDUzNjgzNDVlIiwidGFnIjoiIn0%3D; _sg_b_p=%2Ffootball%2Fengland%2Fpremier-league-2019-2020%2Fresults%2F%2C%2Ffootball%2Fengland%2Fpremier-league-2019-2020%2Fresults%2F%2C%2Ffootball%2Fengland%2Fpremier-league-2019-2020%2Fresults%2F%2C%2Fresults%2F%2C%2Ffootball%2Fengland%2Fpremier-league%2Fresults%2F; _sg_b_v=1%3B465%3B1724614392; _ga_5YY4JY41P1=GS1.1.1724614022.1.1.1724614515.17.0.0',
  'cookie': '__gads=ID=ac91f5d6472d370d:T=1724618340:RT=1724618708:S=ALNI_MYb9Dnxqj7p8luKfRVQ-kwT9tUPbw; __gpi=UID=00000ea5e462a35e:T=1724618340:RT=1724618708:S=ALNI_MaPB6drrvFtHl5yPsNOBh7F2XckoQ; __eoi=ID=b43a5f88d9d0e071:T=1724618340:RT=1724618708:S=AA-AfjZtVD8Fxs_PvQpvzSBlTL1i; op_cookie-test=ok; op_user_time=1734122666; op_user_cookie=11013859971; op_user_hash=3a8c1ff9ab8d0a333fb72bc731bc6fc7; lux_uid=173412266697303571; op_user_time_zone=1; op_user_full_time_zone=37; XSRF-TOKEN=eyJpdiI6IkhLM1R1QkFhQ1ZKbnVkNjljQkZIbUE9PSIsInZhbHVlIjoiaHVqcmJFZjJRSWJtd1lDQ0I2bXE0bERpWmIxSGNHdERNdEYxQ3laNXd3ZEhUVXVWNkMweDV5WHJxUFY0bDRWeStlT0hkbHFwdEZrVElhSG1vWCt1VjQzTkgrRnZGQ2NhbmxqWFBmQkdwbFViRE50TTJsaXhUV3JIRi9OTnVjYTEiLCJtYWMiOiI2YmMwOTk1OTJkZTliZDI2YjdkZGNmOTBiODAzZWJiMjI0MzIzOWUxYzhjZTE2NjAyYTBlNzNhMzJjY2I5NTAyIiwidGFnIjoiIn0%3D; oddsportalcom_session=eyJpdiI6IkJDR0hWZGVhKzk4NEhKTllTbTdzU1E9PSIsInZhbHVlIjoidzJUbkJCSXZQMnQ5dzM2UFVkdFVOa3pjZDNlWmE2TzgvNk9vaG1vY21vMzNvNlE2d0VmaytRdDdBdG9SOVhoejNIWEMxQ0NkQ1NmQkJETWVaVFFmcHlLRTdSK1ROVXN0eEs2QmVyWDNwV2VqUTJDeDYwTUFiSGxoVlVTdWxZOVoiLCJtYWMiOiIwY2UxZDYzMDcwYTMxMjJkOTgwZGVlNzc2NmNiOTIyMDA2NjJkZjRmMGFkNWYxNjM0NzVmN2E4M2VlZDFmZTAxIiwidGFnIjoiIn0%3D; _sg_b_p=%2F%2C%2Ffootball%2Fgermany%2Fbundesliga%2F%2C%2Ffootball%2Fgermany%2Fbundesliga%2F%2C%2Ffootball%2Fgermany%2Fbundesliga%2Fresults%2F%2C%2Ffootball%2Fgermany%2Fbundesliga-2022-2023%2Fresults%2F%2C%2Ffootball%2Fgermany%2Fbundesliga-2022-2023%2Fresults%2F%2C%2Ffootball%2Fgermany%2Fbundesliga-2022-2023%2Fresults%2F; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+13+2024+21%3A46%3A56+GMT%2B0100+(Central+European+Standard+Time)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=4fcdb410-7708-4512-b09a-2786f7691802&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CV2STACK42%3A0&hosts=H194%3A1%2CH302%3A1%2CH236%3A1%2CH198%3A1%2CH230%3A1%2CH203%3A1%2CH286%3A1%2CH526%3A1%2CH16%3A0%2CH190%3A0%2CH21%3A0%2CH301%3A0%2CH303%3A0%2CH304%3A0%2CH99%3A0%2CH305%3A0%2CH593%3A0&genVendors=V2%3A0%2C&AwaitingReconsent=false; _sg_b_v=1%3B316%3B1734122668',
  'priority': 'u=1, i',
  'referer': 'https://www.oddsportal.com/football/england/premier-league-2019-2020/results/',
  'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
  'x-requested-with': 'XMLHttpRequest',
  #'x-xsrf-token': 'eyJpdiI6IlpvQnBvVG9DTnE5WXVuR3ltU29zZFE9PSIsInZhbHVlIjoiSHErTmVGM1pGdWpkbmc1UHErYWFWQW5QOEtSSEN4djVwaTZ6NmRnTXhEUTBVbzJqTXBreVNFM1FjWTBFYUl4WlRWY2NqM2xjcmJpMFFyNDZUWndpM1BQYXBILy9rd1dpeHJ6dFU2MWlscG5uUmZXVG55SjlwQnlVZU5kNGp2UTQiLCJtYWMiOiI1NDQwMjM4NjU0ZGE4NGQyMTkxYTA2MjNiODQzZDk5ZjdhMjJmMWQ3NGYxZTA3ZTI5MzFhOGIzNGRmMDFjZjk2IiwidGFnIjoiIn0='
  'x-xsrf-token': 'eyJpdiI6IkhLM1R1QkFhQ1ZKbnVkNjljQkZIbUE9PSIsInZhbHVlIjoiaHVqcmJFZjJRSWJtd1lDQ0I2bXE0bERpWmIxSGNHdERNdEYxQ3laNXd3ZEhUVXVWNkMweDV5WHJxUFY0bDRWeStlT0hkbHFwdEZrVElhSG1vWCt1VjQzTkgrRnZGQ2NhbmxqWFBmQkdwbFViRE50TTJsaXhUV3JIRi9OTnVjYTEiLCJtYWMiOiI2YmMwOTk1OTJkZTliZDI2YjdkZGNmOTBiODAzZWJiMjI0MzIzOWUxYzhjZTE2NjAyYTBlNzNhMzJjY2I5NTAyIiwidGFnIjoiIn0='
}

for i in range(1,9):
    response = requests.request("GET", get_url(i), headers=headers, data=payload)
    with open(f'data/betting_{YEAR}_Bundesliga_page_{i}.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
#print(response.text)

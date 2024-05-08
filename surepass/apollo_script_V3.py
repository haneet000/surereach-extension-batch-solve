import requests
import json
import os

session = requests.session()
url = "https://app.apollo.io/api/v1/mixed_people/search"


for page in range(25):
    payload = json.dumps({
        "finder_table_layout_id": "65b26347e6ae8f01c6f803ec",
        "contact_label_ids": [
            "663b2be14c0cd300017791a9"
        ],
        "prospected_by_current_team": [
            "yes"
        ],
        "page": page,
        "display_mode": "explorer_mode",
        "per_page": 25,
        "open_factor_names": [],
        "num_fetch_result": 22,
        "context": "people-index-page",
        "show_suggestions": False,
        "ui_finder_random_seed": "4ksaoud4gx",
        "cacheKey": 1715160891394
    })
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'hubspotutk=89cd4d1363a3bb11489db759fd296d10; _cioanonid=5f40ebb2-8434-091a-2a1c-8218e9e04e97; mutiny.user.token=7cdee69a-d842-4f87-b7d4-9b582519cf6b; _fbp=fb.1.1707120701795.1916077219; intercom-device-id-dyws6i9m=00a33780-4112-4678-9f0b-550d2e5fdf8a; _cioid=65b26347e6ae8f01c6f80486; __stripe_mid=816cc19e-ab09-4e9e-b095-767a71ad731f3b2ef7; amp_91ff3d=rX3Xpv9SFGXzmn3vFNnZ-E.NjViMjYzNDdlNmFlOGYwMWM2ZjgwNDg2..1hmgn6q9t.1hmgnchmk.k.2.m; fs_uid=#W8ZH#75727da7-3e41-4033-9bf9-4d0fc1539dce:2c710463-8612-462a-b12a-7c93d57046df:1709206711101::3#19eec7c3#/1740742708; zp__utm_medium=Discovery; zp__initial_utm_medium=Discovery; zp__initial_utm_campaign=Discovery%20Person%20Page%20-%20General; ps_mode=trackingV1; zp__initial_utm_content=5d419cf4a3ae616945cda861; _hjSessionUser_3601622=eyJpZCI6IjZmOTMzOTAxLTc1NGQtNTA0MC1iZDYyLTNkYzMzNTUzOTAwMCIsImNyZWF0ZWQiOjE3MTAxNjI2MTIzNDYsImV4aXN0aW5nIjp0cnVlfQ==; __q_state_xnwV464CUjypYUw2=eyJ1dWlkIjoiZDgwYjJkYzQtNjcxMi00NWJhLWIxZmEtYzNlYTdmOGI5Mzk1IiwiY29va2llRG9tYWluIjoiYXBvbGxvLmlvIn0=; zp__initial_referrer=https://www.google.com/; zp__initial_utm_source=www.google.com; zp__utm_content=5dc7353b18396f00015011ce; remember_token_leadgenie_v2=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTFZakkyTXpRM1pUWmhaVGhtTURGak5tWTRNRFE0Tmw4d01qWmpNREJqTkRrMFl6VXlORE0xWkRBMk1EVXhaR1UyTURZeVpUUTJZU0k9IiwiZXhwIjoiMjAyNC0wNS0xNVQwNzoxMToyOC42NTVaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3Rva2VuX2xlYWRnZW5pZV92MiJ9fQ%3D%3D--bb9bbb67ab3081645234a0118d30f11c6c3aa07e; zp__utm_campaign=Discovery%20Person%20Page%20-%20General; _ga_2KJN2H89XE=GS1.1.1713508734.3.1.1713508751.43.0.0; zp__utm_source=knowledge.apollo.io; ZP_LATEST_LOGIN_PRICING_VARIANT=23Q2_EC_W49; ZP_Pricing_Split_Test_Variant=23Q2_EC_W49; _clck=ggsbxw%7C2%7Cfll%7C0%7C1542; __hstc=21978340.89cd4d1363a3bb11489db759fd296d10.1707115041900.1714819573648.1715151002629.53; __hssrc=1; _gid=GA1.2.1193850265.1715151004; _ga=GA1.1.35341912.1707115047; _ga_CBPPE9HPBE=GS1.1.1715151004.25.0.1715151011.0.0.0; _gcl_au=1.1.325228364.1715151013; _ga_76XXTC73SP=GS1.1.1715151013.27.0.1715151014.59.0.1755115650; _clsk=iv8itj%7C1715151026097%7C2%7C0%7Cu.clarity.ms%2Fcollect; GCLB=COvGxp_jq4vJUhAD; X-CSRF-TOKEN=YL6glTOibA-OOfLMjeGatNN-O7oRbafRgvtc8A0NRWcAtWPgyCG79J8g5GEYCfWeJaAyK30I-sAduL5c7O8Jzw; _leadgenie_session=z6WR0O74aFjjitC2lJt1Fw5gdMPdY764CjmEL%2FrFs26Xm2kKjtfIbkehwhogQ7fdjujls9JHkRMjaRMFiKMWHryMbSREPFXbVxEJz1AbEWPaBitXOc24mre%2ByvNHskgl00ksBRrZoITx6eM6ydeZ9xy0omwQPVBweC%2FsFns3LM5J%2FN%2B4vk%2BMKpN6kHcBE50kIAVLhmJPhtNTOwW4VAnrL77JnnPDj%2FPeGPLrXG6RIJxHe%2BTj4%2BZ50QBn7hMRwcZSze0VknTQKjPnhxEQoXXhH%2BGfHaG0ckuqqCU%3D--wTG0UYQcX3hGTZRY--vUrhLyBkeWRxC6eajkiiEg%3D%3D; intercom-session-dyws6i9m=a29nSzJycnRNVkM3K2ZkMEdXSmUzN2Z0QlFpdWk5YjlSSmFYVjhrYmVsMncraG1ObXUzSUQ0bFpJR01iUXV0Sy0tTXhGdEM2cndaam9jR0x6cVI4c1g1UT09--976c420fb1653abd22cad146d21676e00375875d; _dd_s=rum=0&expire=1715161791320; amplitude_id_122a93c7d9753d2fe678deffe8fac4cfapollo.io=eyJkZXZpY2VJZCI6ImQ2YmUxOTcxLWFkYmMtNGMyYy1hZWEwLWI3ZDgyYTg1NGJkNFIiLCJ1c2VySWQiOiI2NWIyNjM0N2U2YWU4ZjAxYzZmODA0ODYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE3MTUxNjA4NjcwNDAsImxhc3RFdmVudFRpbWUiOjE3MTUxNjA4OTEzMjIsImV2ZW50SWQiOjEwMTgsImlkZW50aWZ5SWQiOjIxMDQsInNlcXVlbmNlTnVtYmVyIjozMTIyfQ==; X-CSRF-TOKEN=vhxhT77Qa6rgpQ_d3SrPbAZBH3eFdHL5rr5J3eG4pa7eF6I6RVO8UfG8GXBIwqBG8J8W5ukRL-gx_atxAFrpBg; _leadgenie_session=9SQF5B5azGkWpzTcZniTCFU8%2BpZG00icFIjwHbyxSblnVJfuxnn%2FblsBz7ocenL%2B7ybJmV7DDKPhplB1fyea6sOjsyIyPnRE7IvlSUYOfCXUJ0D4FZe6DwmNdkkUfaZOuK5au4FhsdnBaujDwRX9VODGT%2FR%2BzIADeyabUSJdZ1H5DmyrBTiqKl9uTtRfP6ShwNMM%2FdPR%2BS7YZKqeqeL5YlNPK2Ffh4O7VIfh2FaYLvh0EE33YZWffJpSaVY%2BS9etOhYNHfNrYEK%2FxbzTZf9r9Dz4UFigyHP0egM%3D--5G1VOTkZEFGneSZn--mBJZHcJeQqbuzKatAwYYcQ%3D%3D',
        'origin': 'https://app.apollo.io',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.apollo.io/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-csrf-token': 'YL6glTOibA-OOfLMjeGatNN-O7oRbafRgvtc8A0NRWcAtWPgyCG79J8g5GEYCfWeJaAyK30I-sAduL5c7O8Jzw'
    }

    response = session.post(url, headers=headers, data=payload)

    req_response = response.json()
    display_name = req_response["breadcrumbs"][0]['display_name']

    folder_path = "C:/Users/devid/PycharmProjects/honey/pythonProject/surepass/batch_solver_folder/apollo_all_company_data"
    json_file_name = f"{display_name}_{page}.json"
    full_path = os.path.join(folder_path, json_file_name)

    with open(full_path, 'w') as file:
        json.dump(req_response, file, indent=2)
    print(f"Saved data from page {page} to {json_file_name}")

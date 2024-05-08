class Uan_history_untagged():
    def __init__(self):
        self.all_get_data = []
        self.list_to_json = {}
        self.session = requests.session()
        self.index = 0
        self.lead_id = None
        # fetch data down arrow side
        self.main_url = "https://surepass.salesmate.io/apis/deal/v1/board-view/cards?rows=9&from=0"
        self.phone_to_full_name = "https://kyc-api.surepass.io/api/v1/bank-verification/upi-mobile-to-name"

    main_url_headers = {
        'authority': 'surepass.salesmate.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'accesstoken': '6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644',
        'content-type': 'application/json',
        'cookie': '_fbp=fb.1.1691751413434.1501901083; sm-hn=surepass.salesmate.io; sm-ac-tk=6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644; sm-user-email=sales%40surepass.io; sm-impersonate=false; sm-is-login-using-recovery-code=false; sm-user-id=7; sm-hn-common=surepass.salesmate.io; amp_6e403e=7zlkwpITU9i3S_X2-EJ-m9...1hf70bua7.1hf70bua7.d.0.d; landedOnPage=www.salesmate.io; _hjSessionUser_1217448=eyJpZCI6ImUyYTc3ODA3LWZlY2ItNTg4ZS1iZWJlLTBhZjY2OGYxMjQ1ZSIsImNyZWF0ZWQiOjE3MDM4NDM2NTgzMDYsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.422296213.1703843659; utm_source=Direct; utm_medium=(Direct); _clck=4w4ks9%7C2%7Cfjh%7C0%7C1458; _ga=GA1.1.528073730.1664513486; _ga_0LEBD9YWK3=GS1.1.1708686485.22.0.1708686488.57.0.0; sm-container-state=true',
        'isimpersonate': 'false',
        'origin': 'https://surepass.salesmate.io',
        'referer': 'https://surepass.salesmate.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-linkname': 'surepass.salesmate.io',
        'x-workspace-id': ''
    }

    lead_header = {
        'authority': 'surepass.salesmate.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'accesstoken': '6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644',
        'content-type': 'application/json',
        'cookie': '_fbp=fb.1.1691751413434.1501901083; sm-hn=surepass.salesmate.io; sm-ac-tk=6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644; sm-user-email=sales%40surepass.io; sm-impersonate=false; sm-is-login-using-recovery-code=false; sm-user-id=7; sm-hn-common=surepass.salesmate.io; amp_6e403e=7zlkwpITU9i3S_X2-EJ-m9...1hf70bua7.1hf70bua7.d.0.d; landedOnPage=www.salesmate.io; _hjSessionUser_1217448=eyJpZCI6ImUyYTc3ODA3LWZlY2ItNTg4ZS1iZWJlLTBhZjY2OGYxMjQ1ZSIsImNyZWF0ZWQiOjE3MDM4NDM2NTgzMDYsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.422296213.1703843659; utm_source=Direct; utm_medium=(Direct); _clck=4w4ks9%7C2%7Cfjh%7C0%7C1458; _gid=GA1.2.721485861.1708583433; _ga=GA1.2.528073730.1664513486; _clsk=r4lhoj%7C1708583455759%7C2%7C1%7Cz.clarity.ms%2Fcollect; _ga_0LEBD9YWK3=GS1.1.1708583432.21.1.1708583459.33.0.0; sm-container-state=true',
        'isimpersonate': 'false',
        'origin': 'https://surepass.salesmate.io',
        'referer': 'https://surepass.salesmate.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-linkname': 'surepass.salesmate.io',
        'x-workspace-id': ''
    }

    phone_to_full_name_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwOTM2NDIzNywianRpIjoiNmZjNmUyMjAtNGQyZC00YTBjLWJmNWQtOTMzNTZhNjMyODNiIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGV2LnVzZXJuYW1lXzJ0a3l0dTdpdGtna20yejIydnJlbHVzZ2FnZ0BzdXJlcGFzcy5pbyIsIm5iZiI6MTcwOTM2NDIzNywiZXhwIjoyMDI0NzI0MjM3LCJ1c2VyX2NsYWltcyI6eyJzY29wZXMiOlsidXNlciJdfX0.DOrXAK3_6WGMdJfnWE3p002qVqqLMNst7lP3SRjMdrQ'
    }

    main_payload = main_url_payload()

    def main_url_func(self):
        try:
            while True:
                response = self.session.post(self.main_url, headers=self.main_url_headers, data=main_url_payload())
                request_response = response.json()
                if len(request_response['Data']['data']) <= self.index:
                    print("No more leads to process.")
                    break

                status_response = request_response['Data']['data'][self.index]['primaryContact']['mobile']
                self.lead_id = request_response['Data']['data'][self.index]['id']

                last_10_digits = status_response[-10:]
                print(last_10_digits)
                if last_10_digits.isdigit() and len(last_10_digits) == 10:
                    self.find_uan(last_10_digits)
                else:
                    print(f"Skipping number at index {self.index}. Invalid or not in the expected format.")
                self.index += 1
        except Exception as e:
            print(f"An error occurred in main_url_func: {e}")

    def find_uan(self, last_10_digits):
        try:
            find_phone_to_full_name_payload = json.dumps({"mobile_number": last_10_digits})
            find_full_name_response = self.session.post(self.phone_to_full_name, headers=self.phone_to_full_name_headers, data=find_phone_to_full_name_payload)
            if find_full_name_response.status_code == 200:
                response_json = find_full_name_response.json()
                response_data = response_json.get('data', {})
                full_name = response_data.get('full_name')
                if full_name:
                    self.make_lead(full_name)
                else:
                    print("Failed to retrieve Full name .")
            elif find_full_name_response.status_code == 422:
                print("Failed to retrieve Full Name. Status code 422 received.")
            else:
                print(f"Failed to retrieve full name. Response status: {find_full_name_response.status_code}")
        except Exception as e:
            print(f"An error occurred in find_phone_no_to_full_name: {e}")


    def make_lead(self, full_name):
        try:
            lead_url = f"https://surepass.salesmate.io/apis/deal/v4/modules/4/object/{self.lead_id}/notes"
            lead_id_payload = json.dumps({
                "note": f"<div>Automation - Full Name - {full_name}</div>",
                "attachments": [],
                "type": "Note"
            })
            # Post request to create lead
            lead_id_response = self.session.post(lead_url, headers=self.lead_header, data=lead_id_payload)
            print(lead_id_response.status_code)
            # Process response if needed
            self.index += 1
        except Exception as e:
            print(f"An error occurred in make_lead: {e}")


if __name__ == "__main__":
    solving_uan_history = Uan_history_untagged()
    solving_uan_history.main_url_func()
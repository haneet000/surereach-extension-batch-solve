import requests
import json
from honey.my_project.untagged_leads_uan_history_payload import main_url_payload


class Untagged_leads():
    def __init__(self):
        self.session = requests.session()
        self.index = 0
        self.lead_id = None
        # fetch data down arrow side
        self.main_url = "https://surepass.salesmate.io/apis/deal/v1/board-view/cards?rows=6&from=0"
        self.email_logs_url = "https://app.surepass.io/api/v1/admin/email-logs"
        self.salemate_id_to_console_url = "https://app.surepass.io/api/v1/admin/set-crm-profile-url"
        self.main_url_payload_var = main_url_payload()

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

    email_logs_headers = {
          'authority': 'app.surepass.io',
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/json',
          'origin': 'https://console-admin.surepass.io',
          'referer': 'https://console-admin.surepass.io/',
          'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-site',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }

    lead_header = {
        'authority': 'surepass.salesmate.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'accesstoken': '6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644',
        'content-type': 'application/json',
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

    salemate_id_to_console_headers = {
          'authority': 'app.surepass.io',
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/json',
          'origin': 'https://console-admin.surepass.io',
          'referer': 'https://console-admin.surepass.io/',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

    email_id_logs_headers ={
      'authority': 'app.surepass.io',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': 'sib_cuid=79a397ff-3504-4c4b-8e93-52299c2cdad5; _gcl_au=1.1.1151342286.1707566274; _ga=GA1.1.819824749.1707566274; messagesUtk=59de5c0ecd8e4c1199abd3a52d09f504; _hjSessionUser_2837838=eyJpZCI6ImYwMGNiMDI5LTRjYzQtNWQ5Yy1hYTA5LWQ0MjIyMGJiNmZiOSIsImNyZWF0ZWQiOjE3MDc1NjY0MTYzMTAsImV4aXN0aW5nIjp0cnVlfQ==; ajs_anonymous_id=%225c897b5d-47b7-4587-b067-475f8e81610c%22; hubspotutk=e1e1bb92912b4f2c9fd1402a40942aef; GCP_IAP_UID=117281239643461000806; cf_clearance=WOvfHkXht5SA2P0cojmiLSLbddoEeun3bvZYVJBEugw-1709552738-1.0.1.1-ZwvztLQd.8Ihmwlnb7YA1QCT9aIff7sRJJ4ZrF53gst46vYI7aDdluzmDlDPh71.gyIO4cH3FzrTMBsOc_LgEw; __hstc=190410484.e1e1bb92912b4f2c9fd1402a40942aef.1707566865768.1707566865768.1709552738098.2; _ga_XTFP6C19HL=GS1.1.1709552734.2.1.1709553783.0.0.0; access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk2NjM0MDgsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6ImFjY2VzcyJ9.JaZRkvIRcqm22gZl0kKxxcxIXydDZkGdGqcJgysTIio; refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTIyMzM4MDgsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6InJlZnJlc2gifQ.ZOz8Rib-Ztdu-ubxIkwFuxFzjOVXU_QeNx3EEe7tpjA',
      'origin': 'https://console-admin.surepass.io',
      'referer': 'https://console-admin.surepass.io/',
      'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }


    def main_func(self):
        try:
            while True:
                response = self.session.post(self.main_url, headers=self.main_url_headers, data=self.main_url_payload_var)
                request_response = response.json()
                if len(request_response.get('Data', {}).get('data', [])) <= self.index:
                    print("No more leads to process.")
                    break

                if request_response:
                    email_id_request_res = request_response['Data']['data'][self.index]['primaryContact']['email']
                    self.lead_id = request_response['Data']['data'][self.index]['id']
                    print(email_id_request_res)
                    self.email_logs(email_id_request_res)
                else:
                    print(f"Skipping number at index {self.index}. Invalid or not in the expected format.")
                self.index += 1
        except Exception as e:
            print(f"An error occurred in main_func: {e}")

    def email_logs(self, email_id_request_res):
        # email_id_logs_payload = json.dumps({"target_user_email": email_id_request_res})
        email_logs_url = f"https://console-admin.surepass.io/self-signup/profile/{email_id_request_res}"
        print(email_logs_url)
        try:
            email_log_response = self.session.get(email_logs_url, headers=self.email_id_logs_headers)
            if email_log_response.status_code == 200:

                lead_url = f"https://surepass.salesmate.io/apis/deal/v4/modules/4/object/{self.lead_id}/notes"
                lead_id_payload = json.dumps({
                    "note": f"<div>Automation - Console - https://console-admin.surepass.io/self-signup/profile/{email_id_request_res}</div>",
                    "attachments": [],
                    "type": "Note"
                })
                lead_id_response = self.session.post(lead_url, headers=self.lead_header, data=lead_id_payload)
                print(lead_id_response.status_code)
                crm_profile_url = f'https://surepass.salesmate.io/#/app/deals/{self.lead_id}/detail'
                salemates_id_to_console_payload = json.dumps({"target_user_email": email_id_request_res,
                                                              "crm_profile_url":crm_profile_url })
                salemate_id_to_console_res = self.session.post(self.salemate_id_to_console_url,
                                                               headers=self.salemate_id_to_console_headers,
                                                               payload = salemates_id_to_console_payload)
                print(f'{salemate_id_to_console_res.status_code} Salemate link added on console')
                self.index += 1
            else:
                print(email_log_response.status_code)
                self.index += 1
        except Exception as e:
            print(f"Error occurred: {e}")
            self.index += 1


# Instantiate the class and call the main function
if __name__ == "__main__":
    untagged_leads = Untagged_leads()
    untagged_leads.main_func()



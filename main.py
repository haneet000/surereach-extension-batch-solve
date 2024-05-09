import csv
import json
import os
from concurrent.futures import ThreadPoolExecutor
from requests import request


class LinkedinBatchSolver(object):
    base_url = "https://api.surereach.io/api/v1/surereach/users/fetch-linkedin-data"

    def __init__(self, csv_path):
        self.progress = 0
        self.last_index = None
        self.csv_path = csv_path

    @staticmethod
    def get_headers():
        token = os.getenv("TOKEN")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        return headers

    @staticmethod
    def get_payload(linkedin_id):
        payload = {"profile_url": linkedin_id}
        return payload

    def get_filename(self):
        filename_arr = self.csv_path.split("/")
        output_filename = filename_arr[len(filename_arr) - 1].replace(".csv", "")
        output_filename = f"{output_filename}_solved.csv"
        return output_filename

    def create_index(self):
        try:
            with open("last_index.json", "r") as progress_file:
                progress_dict = json.load(progress_file)

                self.last_index = progress_dict.get("last_index")
        except FileNotFoundError:
            with open("last_index.json", "w") as progress_file:
                self.last_index = last_index = -1

                json.dump({"last_index": last_index}, progress_file)

    @staticmethod
    def format_details(response, profile):
        json_response = response.json()
        json_data = json_response.get("data", dict())

        emails = json_data.get("email") if json_data.get("email") is not None else ""
        profile_url = json_data.get("profile_url") if json_data.get("profile_url") is not None else ""
        phone = json_data.get("phone_no") if json_data.get("phone_no") is not None else ""

        return {"sure_email": emails,
                "sure_phone": phone,
                "profile_url": profile}

    def read_csv(self):

        # reading existing csv
        with open(self.csv_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            list_of_dict = list(csvreader)

        return list_of_dict

    def write_csv(self, linkedin_data):
        output_filename = self.get_filename()

        # Open the existing CSV in read mode and read its content
        with open(output_filename, 'a+', newline='', encoding="utf-8") as csvfile:
            rows = self.read_csv()  # Read all rows into a list
            fieldnames = [*rows[0].keys()]
            fieldnames.extend(["sure_email", "sure_phone"])

            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                csvwriter.writeheader()

            # Update the rows where needed
            for row in rows:
                if row['linkedin_url'] == linkedin_data.get("profile_url"):
                    row['sure_email'] = linkedin_data.get("sure_email")
                    row['sure_phone'] = linkedin_data.get("sure_phone")

                    csvwriter.writerow({**row})
                    break

        return True

    def fetch_data(self):
        self.create_index()
        list_of_dict = self.read_csv()

        for idx, data in enumerate(list_of_dict):
            self.progress += 1

            linkedin = data.get("linkedin_url")

            if idx <= self.last_index:
                print(f"{linkedin} already processed")
                continue

            # fetching data
            response = self.request_linkedin(linkedin)
            if response.status_code != 200:
                raise Exception

            formatted_details = self.format_details(response, linkedin)

            print("progress: ", self.progress)
            self.write_csv(formatted_details)

            with open("last_index.json", "w") as progress_file:
                last_index = idx
                json.dump({"last_index": last_index}, progress_file)

        return "Finished..........................................................................."

    def request_linkedin(self, linkedin):
        response = request(
            "POST", self.base_url, headers=self.get_headers(), json=self.get_payload(linkedin), verify=False
        )
        return response

    @classmethod
    def extract_data(cls, csv_path):
        return cls(csv_path).fetch_data()


def batch_solver():
    try:

        csv_path = "C:/Users/devid/Downloads/Need 120 mobiles out of 626 links.csv"
        return LinkedinBatchSolver.extract_data(csv_path)
    except Exception as e:
        print(e)


    from dotenv import load_dotenv
    load_dotenv()
    print(batch_solver())

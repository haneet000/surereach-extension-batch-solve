import csv
import json
import os
import time
# from dotenv import load_dotenv
from requests import request


class LinkedinBatchSolver(object):
    base_url = "https://api.surereach.io/api/v1/surereach/users/fetch-linkedin-data"

    def __init__(self, csv_path):
        self.progress = 0
        self.last_index = None
        self.csv_path = csv_path

    @staticmethod
    def get_headers():
        # TOKEN = os.getenv("TOKEN")
        # token = os.getenv("TOKEN")
        headers = {
            'Content-Type': 'application/json',
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsImZyb250ZW5kIjp0cnVlLCJzZXJ2ZXIiOnRydWUsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTczNTczOSwianRpIjoiMzIxMGMzMGItYjE3Ni00ZWUzLWE2N2EtZWY2NGY4NTE5ZjUwIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiY2xpZW50Lis5MTk1ODIzMTQyODAiLCJuYmYiOjE2OTE3MzU3MzksImV4cCI6MTcyMzI3MjAzOSwidXNlcl9jbGFpbXMiOnsic2NvcGVzIjpbInN1cmVyZWFjaC1hY2Nlc3MiXX19.CiOy9Mf5sb-KOOvIYvQF-vJEnW4A7TzFPfecLzEmHxg'
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
            with open("C:/Users/devid/PycharmProjects/pythonProject/surepass/last_index.json", "r") as progress_file:
                progress_dict = json.load(progress_file)

                self.last_index = progress_dict.get("last_index")
        except FileNotFoundError:
            with open("C:/Users/devid/PycharmProjects/pythonProject/surepass/last_index.json", "w") as progress_file:
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
        with open(self.csv_path, 'r', encoding='Latin-1') as csvfile:
            csvreader = csv.DictReader(csvfile)
            list_of_dict = list(csvreader)

        return list_of_dict

    def write_csv(self, linkedin_data):
        output_filename = self.get_filename()

        with open(output_filename, 'a+', newline='', encoding='Latin-1') as csvfile:
            rows = self.read_csv()
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
            linkedin = data.get("linkedin_url")
            if idx <= self.last_index:
                print(f"{linkedin} already processed")
            else:
                response = self.request_linkedin(linkedin)
                if response.status_code == 200:
                    formatted_details = self.format_details(response, linkedin)

                    print("progress: ", self.progress)
                    self.write_csv(formatted_details)
                    # time.sleep(5)
                    self.progress += 1

                with open("C:/Users/devid/PycharmProjects/pythonProject/surepass/last_index.json", "w") as progress_file:
                    last_index = idx
                    json.dump({"last_index": last_index}, progress_file)

        return "Finished..........................................................................."

    def request_linkedin(self, linkedin):
        response = request(
            "POST", self.base_url, headers=self.get_headers(), json=self.get_payload(linkedin), verify=False
        )
        if response.status_code != 200:
            print(response.content, "linkedin", linkedin)
        return response

    @classmethod
    def extract_data(cls, csv_path):
        return cls(csv_path).fetch_data()


def batch_solver():
    try:

        csv_path = "C:/Users/devid/Downloads/linkedin_url - Sheet1.csv"
        return LinkedinBatchSolver.extract_data(csv_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # from dotenv import load_dotenv
    # load_dotenv()
    print(batch_solver())




import json
import pandas as pd
from pathlib import Path


def create_df():
    count = 0
    for index, row in df.iterrows():

        rc_number = row["rc_number"]
        chsi_number = row["CHASSIS NUMBER"]

        if not rc_number or isinstance(rc_number, float):

            flatten_data = {
                "vehicle_chasi_number": chsi_number,
                "rc_number": None,
                "status_code": 422
            }
            new_df = pd.DataFrame(flatten_data, index=[index])
            all_rows.append(new_df)

        else:

            rc_number = str(rc_number).strip()
            json_file = json_files_path.joinpath(rc_number).with_suffix(".json")
            flag = json_file.is_file()
            if flag:
                with open(json_file, "r") as f:
                    json_data = json.load(f)
                    status = json_data.get("status_code")
                    if status == 200:
                        data = json_data.get("data")
                        data.pop("client_id")
                        flatten_data = {
                            "vehicle_chasi_number": data["rc_chasi_no"],
                            "rc_number": data["rc_number"],
                            "vehicle_engine_number": data["vehicle_engine_number"],
                            "registration_date": data["registration_date"],
                            "owner_name": data["owner_name"],
                            "father_name": data["father_name"],
                            "present_address": data["present_address"],
                            "permanent_address": data["permanent_address"],
                            "mobile_number": data["mobile_number"],
                            "vehicle_category": data["vehicle_category"],
                            "maker_description": data["maker_description"],
                            "maker_model": data['maker_model'],
                            "body_type": data['body_type'],
                            "fuel_type": data["fuel_type"],
                            "color": data["color"],
                            "norms_type": data["norms_type"],
                            "fit_up_to": data["fit_up_to"],
                            "financer": data['financer'],
                            "financed": data['financed'],
                            "insurance_company": data["insurance_company"],
                            "insurance_policy_number": data["insurance_policy_number"],
                            "insurance_upto": data["insurance_upto"],
                            "manufacturing_date": data["manufacturing_date"],
                            "manufacturing_date_formatted": data["manufacturing_date_formatted"],
                            "registered_at": data["registered_at"],
                            "latest_by": data["latest_by"],
                            "less_info": data["less_info"],
                            "tax_upto": data["tax_upto"],
                            "tax_paid_upto": data["tax_paid_upto"],
                            "cubic_capacity": data["cubic_capacity"],
                            "vehicle_gross_weight": data["vehicle_gross_weight"],
                            "no_cylinders": data["no_cylinders"],
                            "seat_capacity": data["seat_capacity"],
                            "sleeper_capacity": data["sleeper_capacity"],
                            "standing_capacity": data["standing_capacity"],
                            "wheelbase": data["wheelbase"],
                            "unladen_weight": data["unladen_weight"],
                            "vehicle_category_description": data["vehicle_category_description"],
                            "pucc_number": data["pucc_number"],
                            "pucc_upto": data["pucc_upto"],
                            "permit_number": data["permit_number"],
                            "permit_issue_date": data["permit_issue_date"],
                            "permit_valid_from": data["permit_valid_from"],
                            "permit_valid_upto": data["permit_valid_upto"],
                            "permit_type": data["permit_type"],
                            "national_permit_number": data["national_permit_number"],
                            "national_permit_upto": data["national_permit_upto"],
                            "national_permit_issued_by": data["national_permit_issued_by"],
                            "non_use_status": data["non_use_status"],
                            "non_use_from": data["non_use_from"],
                            "non_use_to": data["non_use_to"],
                            "blacklist_status": data["blacklist_status"],
                            "noc_details": data["noc_details"],
                            "owner_number": data["owner_number"],
                            "rc_status": data["rc_status"],
                            "masked_name": data["masked_name"],
                            "status_code": status
                        }

                        new_df = pd.DataFrame(flatten_data, index=[index])
                        all_rows.append(new_df)
                    else:
                        rc_number = json_data["data"].get("rc_number")

                        flatten_data = {
                            "vehicle_chasi_number": chsi_number,
                            "rc_number": rc_number,
                            "status_code": 422
                        }
                        new_df = pd.DataFrame(flatten_data, index=[index])
                        all_rows.append(new_df)
                        count += 1
            else:
                flatten_data = {
                    "vehicle_chasi_number": chsi_number,
                    "rc_number": rc_number,
                    "status_code": 422
                }
                count += 1
                new_df = pd.DataFrame(flatten_data, index=[index])
                all_rows.append(new_df)

        print(index)
    print(f"Total 422 cases are: {count}")
    return write_csv(all_rows)


def write_csv(all_rows):
    final_df = pd.concat(all_rows)
    final_csv = main_path.joinpath("final_rc_details.csv")
    final_pipe_csv = main_path.joinpath('final_rc_pipe_details.csv')
    final_df.to_csv(final_csv, mode="w", index=False)
    final_df.to_csv(final_pipe_csv, sep='|', index=False)
    print("final csv created")


if __name__ == "__main__":
    all_rows = list()
    main_path = Path(r"C:\Users\Hiresh Verma\surepass\batch_solver\RC\chassis_to_rc\TML\batch_95")
    json_files_path = main_path.joinpath("rc_details_json")
    csv_file = main_path.joinpath("chasis_rc_number.csv")

    df = pd.read_csv(csv_file)
    create_df()

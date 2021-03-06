from os import chdir
from cleaner import load_sheet, write_csv, split_name, merge_and_tag, add_fields


def process_staff_data():
    chdir('./data')
    infile = 'LEEDS 2023 Staff List.xlsx'
    wb = load_sheet(infile, sheet="Sheet1", skip_rows=2)

    def process_staff_record(record):
        record = split_name(record, name="Name", exceptions={
            "Abigail Scott Paul": ["Abigail", "Scott Paul"],
            "Martha Rose Wilson": ["Martha Rose", "Wilson"]
        })

        record = merge_and_tag(record,
                               fields=['Mobile', 'Office No', 'DDL'],
                               tags=['Mobile', 'Work', 'Direct'],
                               output_field='Phone'
                               )

        record = add_fields(record, fields={
            "Organisation": "LEEDS 2023",
            "Person Type": "Staff"
        })

        return record

    wb = [process_staff_record(r) for r in wb]

    write_csv(wb, 'CRM0001_staff_list.csv')


if __name__ == "__main__":
    process_staff_data()

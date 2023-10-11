import xlrd

from utilities.search_claims import Search_claims_data


class XlsxReader:
    @staticmethod
    def get_xlsx_search_claims_data():
        wb = xlrd.open_workbook(f"./utilities/search_claims_data.xlsx")
        sheet = wb.sheet_by_index(0)
        search_data = []

        for i in range(1, sheet.nrows):
            search_claims_data = search_claims_data(sheet.cell(i, 0).value,  # employee_name
                                                    sheet.cell(i, 1).value,  # reference_ID
                                                    sheet.cell(i, 2).value,  # event name
                                                    sheet.cell(i, 3).value,  # status
                                                    sheet.cell(i, 4).value,  # from_date
                                                    sheet.cell(i, 5).value,  # to_date
                                                    sheet.cell(i, 6).value)  # include
            search_data.append(search_claims_data)
        return search_data

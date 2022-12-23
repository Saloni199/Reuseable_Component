import tabula


import os
def get_table(pdf,index):
    try:
        tables = tabula.read_pdf(pdf, pages='all')
        return  tables[int(index)]
        # print(type(tables))
        # Tables=pd.DataFrame(tables[int(index)])
        # return Tables
    except:
        print("Error in extracting table from pdf")

def get_all_tables(pdf):
    try:
        tables = tabula.read_pdf(pdf, pages='all')
      
        return tables
    except:
        print("Error in extracting table from pdf")

def get_table_on_page_at_index(pdf,page_no,index):
    try:
        tables = tabula.read_pdf(pdf, pages=int(page_no))
      
        return tables[int(index)]
    except:
        print("Error in extracting table from pdf")

    # folder_name = "tables"
    # if not os.path.isdir(folder_name):
    #     os.mkdir(folder_name)
    # # iterate over extracted tables and export as excel individually
    # for i, table in enumerate(tables, start=1):
    #     table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)
        
        # print(len(tables))

# tables = tabula.read_pdf("foo.pdf", pages='all')
# print(tables)

# convert all tables of a PDF file into a single CSV file
# supported output_formats are "csv", "json" or "tsv"
# tabula.convert_into("1710.05006.pdf", "output.csv",
#                     output_format="csv", pages="all")

# save them in a folder


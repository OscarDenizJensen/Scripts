import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Conf_Test.xlsx')
worksheet = workbook.add_worksheet()

config=open("Presentation.config","r")

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

for line in config:
    if "root-authentication" not in line and "encrypted" not in line:
        if "}" in line:
            col-=1
            if col==0:
                row+=1
            elif col==1:
                row+=1

        if ";" in line:
            line=line.replace(";","")
            clean_line=line.strip()

            if clean_line!=" ":
                worksheet.write(row,col,clean_line)
                row+=1

        elif "{" in line:
            line=line.replace("{","")
            clean_line=line.strip()

            if clean_line!=" ":

                worksheet.write(row,col,clean_line)
                col+=1

    else:
        if "root-authentication" not in line:
            col+=1

    print row, col
workbook.close()
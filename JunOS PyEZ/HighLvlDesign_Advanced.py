import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Conf_Test.xlsx')
worksheet = workbook.add_worksheet()

config=open("Presentation.config","r")

col=0
row=0
count=0

with open("Presentation.config","r") as tmp_file:
    for line in tmp_file:
        line=line.strip()
        line="\n"+line

        if "root-authentication" not in line and "encrypted" not in line: ########### and "##" not in line:
            if "{" in line:
                line=line.replace("{","")

                clean_line=line.rstrip()

                if int(clean_line.count(" "))>0:
                    split=clean_line.split(" ")

                    for x in split:
                        if x != split[len(split)-1]:
                            worksheet.write(row,col,x)
                            col+=1
                            count+=1
                        else:
                            worksheet.write(row,col,x)
                            col+=1
                else:
                    worksheet.write(row,col,clean_line)
                    col+=1

            elif ";" in line:
                line=line.replace(";","");
                clean_line=line.rstrip()

                if int(clean_line.count(" "))>0:
                    split=clean_line.split(" ")
                    for x in split:
                        if x != split[len(split)-1]:
                            worksheet.write(row,col,x)
                            col+=1
                            count+=1
                        else:
                            #print x
                            worksheet.write(row,col,x)
                            row+=1

                            if count>0:
                                print count
                                for x in range(count):
                                    col-=1
                                count=0
                else:
                    worksheet.write(row,col,clean_line)
                    row+=1

            elif "}" in line:
                line=line.replace("}","")
                line=line.rstrip()
                col-=1
                if col==0:
                    row+=1

        elif "root-authentication" in line:
            col+=1


workbook.close()
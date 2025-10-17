input_path = "C:\\Users\\bonny\\github\\endeavor_tracklines\\csv_files\\EN711_EN736.csv"
output_path = "C:\\Users\\bonny\\github\\endeavor_tracklines\\csv_files\\EN711_EN736_edits.csv"

import csv
with open(input_path,"r") as source:
    rdr= csv.reader( source )
    with open(output_path,"w") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[2]) )
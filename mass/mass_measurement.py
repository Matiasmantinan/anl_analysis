import pandas as pd
from datetime import datetime
import os
from pathlib import Path
import glob

def create_file(output_file):
    df = pd.DataFrame(columns=["component","componentType","stage","testType",
			"date","runNumer","property1 key", "property1 value","property2 key", 
	        "property2 value","property3 key", "property3 value","property4 key", 
	        "property4 value","passed","problems","result1 key","result1 value"])
    
    files_present = glob.glob(str(output_file))
    if not files_present:
        df.to_csv(output_file,index=False)




def add_date_folder():
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    path = Path("../", date)
    files_present = glob.glob(str(path))
    if not files_present:
        path.mkdir(parents=True, exist_ok=False)
    return path



def main():
    path = add_date_folder()
    output_file = Path(path,"test.csv")
    create_file(output_file)
    add_data(output_file,1)



def add_data(output_file,mass):
    df = pd.read_csv(output_file)

    print(df)

    index = len(df.index)

    df.loc[index,"component"] = "20UPGXB2000035"
    df.loc[index,"componentType"] = "BARE_MODULE"
    df.loc[index,"stage"] = "BAREMODULERECEPTION"
    df.loc[index,"testType"] = "MASS_MEASUREMENT"
    df.loc[index,"date"] = datetime.now().strftime("%d/%m/%y")
    #df.loc[len(df.index)] = data

    print(df)

    df.to_csv(output_file,index=False)



if __name__ == "__main__":
    main()

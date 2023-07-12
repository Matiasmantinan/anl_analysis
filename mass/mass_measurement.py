import pandas as pd
from datetime import datetime
import os
from pathlib import Path
import glob

def create_file(output_file):
    df = pd.DataFrame(columns=["component","institution","componentType","stage","testType",
			"date","runNumber","property1_key", "property1_value","property2_key", 
	        "property2_value","property3_key", "property3_value","property4_key", 
	        "property4_value","passed","problems","result1_key","result1_value"])
    
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
    file_name = "mass_measurement_"+datetime.now().strftime("%m_%d_%y")+".csv"
    output_file = Path(path,file_name)
    create_file(output_file)

    mass = 900.1
    serial = "20UPGXB2000035"
    run = 1
    analysis_version = "v1"
    scale_accuracy = 1.
    add_data_csv(output_file,serial,mass,scale_accuracy,run,analysis_version)



def add_data_csv(output_file,serial,mass,scale_accuracy,run,analysis_version):
    df = pd.read_csv(output_file)

    print(df)

    index = len(df.index)

    df.loc[index,"component"] = serial
    df.loc[index,"institution"] = "ANL"
    df.loc[index,"componentType"] = "BARE_MODULE"
    df.loc[index,"stage"] = "BAREMODULERECEPTION"
    df.loc[index,"testType"] = "MASS_MEASUREMENT"
    df.loc[index,"date"] = datetime.now().strftime("%d/%m/%y")
    df.loc[index,"runNumber"] = run
    df.loc[index,"property1_key"] = "SCALE_ACCURACY"
    df.loc[index,"property1_value"] = scale_accuracy
    df.loc[index,"property2_key"] = "ANALYSIS_VERSION"
    df.loc[index,"property2_value"] = analysis_version
    df.loc[index,"runNumber"] = run
    df.loc[index,"passed"] = test_passed(mass)
    df.loc[index,"problems"] = test_problems(mass)
    df.loc[index,"result1_key"] = "MASS"
    df.loc[index,"result1_value"] = mass 
    #df.loc[len(df.index)] = data

    print(df)

    df.to_csv(output_file,index=False)



def add_data_json(output_file,serial,mass,scale_accuracy,run,analysis_version):
    print("add_data_json")



def test_passed(mass):
    # insert logic
    return "True"


def test_problems(mass):
    # insert logic
    return "False"

if __name__ == "__main__":
    main()
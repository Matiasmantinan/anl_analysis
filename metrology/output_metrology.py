



def create_metrology_csv_file(output_file):
    df = pd.DataFrame(columns=["component","institution","componentType","stage","testType",
			"date","runNumber","property1_key", "property1_value","property2_key", 
	        "property2_value","passed","problems","result1_key","result1_value"])
    
    files_present = glob.glob(str(output_file))
    if not files_present:
        df.to_csv(output_file,index=False)




def add_date_folder():
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    path = Path("../results", date)
    return add_folder(path)


def add_folder(path):
    files_present = glob.glob(str(path))
    if not files_present:
        path.mkdir(parents=True, exist_ok=False)
    return path






def add_metrology_data_csv(output_file,serial,mass,scale_accuracy,run,analysis_version):
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



def add_metrology_BM_data_json(json_path,serial,run,analysis_version):
    json_name = serial+"_MASS_"+datetime.now().strftime("%m_%d_%y")+".json"
    json_file = Path(json_path, json_name)
    mass_dict = {
        "component":serial,
        "testType":"QUAD_BARE_MODULE_METROLOGY",
        "institution":"ANL",
        "runNumber":str(run),
        "date":str(datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
        "passed": True,
        "problems": False,
        "properties":{
            "ANALYSIS_VERSION":analysis_version,
        },
        "results":{
            "SENSOR_X":500.88,
            "SENSOR_Y":952.92,
            "SENSOR_THICKNESS":623.38,
            "SENSOR_THICKNESS_STD_DEVIATION":868.7,
            "FECHIPS_X":442.33,
            "FECHIPS_Y":591.76,
            "FECHIP_THICKNESS":833.83,
            "FECHIP_THICKNESS_STD_DEVIATION":514.55,
            "BARE_MODULE_THICKNESS":895.9,
            "BARE_MODULE_THICKNESS_STD_DEVIATION":363.45
            },
        }

    mass_json = json.dumps(mass_dict)
    with open(json_file, "w") as outfile:
        outfile.write(mass_json)



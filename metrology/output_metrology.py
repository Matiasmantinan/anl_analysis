



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



def add_metrology_data_json(json_path,serial,mass,scale_accuracy,run,analysis_version):
    json_name = serial+"_MASS_"+datetime.now().strftime("%m_%d_%y")+".json"
    json_file = Path(json_path, json_name)
    mass_dict = {
        "component":serial,
        "testType":"MASS_MEASUREMENT",
        "institution":"ANL",
        "runNumber":str(run),
        "date":str(datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')),
        "passed": True,
        "problems": False,
        "properties":{
            "SCALE_ACCURACY":scale_accuracy,
            "ANALYSIS_VERSION":analysis_version,
            },
            "results":{
                "MASS":mass
                },
                }
    
    mass_json = json.dumps(mass_dict)
    with open(json_file, "w") as outfile:
        outfile.write(mass_json)



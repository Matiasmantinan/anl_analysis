import argparse
from statistics import mean
import numpy as np
import glob
import os
from pathlib import Path

from output_metrology import *


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--inputFile", type=str, help = "input txt file",default=None)
    #parser.add_argument("-j", "--inputFileJig", type=str, help = "input jig txt file", default = "Jig_SQ.txt" )
    parser.add_argument("-m", "--measurement", type=str, help = "measurement type, right now the measurement: flex, BM, dummyBM or assembly")

    args = parser.parse_args()


    # infile = args.inputFile

    measurement = args.measurement
    infile = args.inputFile


    path = add_date_folder()
    json_path = add_folder(Path(path,"json_data"))
    file_name = "metrology_measurement_"+datetime.now().strftime("%m_%d_%y")+".csv"
    output_csv_file = Path(path,file_name)
    create_metrology_csv_file(output_csv_file)



    if measurement=="flex":
        if not infile:
            infile = max(glob.iglob("flex_SQ_*"), key=os.path.getctime)
        infile,serialNum = addSerialQuery(infile)
        infile_jig = "Jig_SQ.txt"
        flexMeasurement(serialNum,infile,infile_jig,output_csv_file,json_path)
    elif measurement=="dummyBM":
        if not infile:
            infile = max(glob.iglob("dummyBM_SQ*"), key=os.path.getctime)
        infile,serialNum = addSerialQuery(infile)
        infile_jig = "dummyBMJig_SQ.txt"
        dummyMeasurement(infile,infile_jig)
    elif measurement =="assembly":
        if not infile:
            infile = max(glob.iglob("AssembledModule_SQ*"), key=os.path.getctime)
        infile,serialNum = addSerialQuery(infile)
        infile_jig = "AssembledModuleJig_SQ.txt"
        assemblyMeasurement(infile,infile_jig)
    elif measurement == "BM":
        if not infile:
            infile = max(glob.iglob("realBM_SQ_*"), key=os.path.getctime)
        infile,serialNum = addSerialQuery(infile)
        infile_jig = "realBMJig_SQ.txt"
        BMMeasurement(serialNum,infile, infile_jig, output_csv_file, json_path)





# perform analisis for a flex
def flexMeasurement(serialNum,infile,infile_jig,outputcsv,outputjson):

    len_Y = []
    len_X = []
    len_Z_Laser = []
    len_Z_Optical = []
    pickup_1 = []
    pickup_2 = []
    pickup_3 = []
    pickup_4 = []
    PC_1 = []
    PC_2 = []
    PC_3 = []
    HV = []
    pickup = []
    PC = []
    HV = []

    jig_pickup_1 = []
    jig_pickup_2 = []
    jig_pickup_3 = []
    jig_pickup_4 = []

    jig_PC_1 = []
    jig_PC_2 = []
    jig_PC_3 = []
    jig_HV = []


    with open(infile_jig) as jig_file:
        for line in jig_file:
            if "Pickup1" in line and "Laser" not in line:
                jig_pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                jig_pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup3" in line and "Laser" not in line:
                jig_pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))            
            if "Pickup4" in line and "Laser" not in line:
                jig_pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))        

            if "PC_1" in line and "Laser" not in line:
                jig_PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                jig_PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                jig_PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "HV" in line and "Laser" not in line:
                jig_HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
                    

    with open(infile) as file:
        for line in file:
            if "Pickup1" in line and "Laser" not in line:
                pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup3" in line and "Laser" not in line:
                pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup4" in line and "Laser" not in line:
                pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "PC_1" in line and "Laser" not in line:
                PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    

            if "HV" in line and "Laser" not in line:
                HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))


            if "distance_X" in line:
                x_dimension =  float((line.split()[1].replace('DX|','')).replace('|',''))
                print ("X: ",x_dimension)
            if "distance_Y" in line:
                y_dimension =  float((line.split()[1].replace('DY|','')).replace('|',''))
                print ("Y: ", y_dimension)


    pickup_1_z =  (np.subtract(jig_pickup_1, pickup_1))
    pickup_2_z =  (np.subtract(jig_pickup_2, pickup_2))
    pickup_3_z =  (np.subtract(jig_pickup_3, pickup_3))
    pickup_4_z =  (np.subtract(jig_pickup_4, pickup_4))
    print ("Pickup 1: ", abs(np.mean(pickup_1_z)), "   ", np.std(pickup_1_z))
    print ("Pickup 2: ", abs(np.mean(pickup_2_z)), "   ", np.std(pickup_2_z) )
    print ("Pickup 3: ", abs(np.mean(pickup_3_z)), "   ", np.std(pickup_3_z))
    print ("Pickup 4: ", abs(np.mean(pickup_4_z)), "   ", np.std(pickup_4_z))


    avg_pickup_thickness = abs(np.mean([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)]))
    std_pickup_thickness = np.std([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)])
    print ("Avg pickup thickness:  ", avg_pickup_thickness)
    print ("Std Dev pickup thickness: ", std_pickup_thickness)

    PC_1_z =  (np.subtract(jig_PC_1, PC_1))
    PC_2_z =  (np.subtract(jig_PC_2, PC_2))
    PC_3_z =  (np.subtract(jig_PC_3, PC_3))

    avg_pc_height = abs(np.mean([np.mean(PC_1_z), np.mean(PC_2_z), np.mean(PC_3_z)]))
    print ("Average PC height:  ", avg_pc_height)

    HV_z = np.subtract(jig_HV, HV)
    avg_HV_thickness = np.mean(HV_z)
    print ("Avg HV height: ", avg_HV_thickness )

    results = {
        "X_DIMENSION": x_dimension,
        "Y_DIMENSION": y_dimension,
        "X-Y_DIMENSION_WITHIN_ENVELOP": True,
        "AVERAGE_THICKNESS_FECHIP_PICKUP_AREAS": avg_pickup_thickness,
        "STD_DEVIATION_THICKNESS_FECHIP_PICKUP_AREAS": std_pickup_thickness,
        "HV_CAPACITOR_THICKNESS": avg_HV_thickness,
        "HV_CAPACITOR_THICKNESS_WITHIN_ENVELOP": True,
        "AVERAGE_THICKNESS_POWER_CONNECTOR": avg_pc_height
    }

    add_metrology_FLEX_data_json(outputjson, serialNum,1,"v1",results)


def addSerialQuery(infile):
    print ("Module input file: ", infile)
    while True:
        serialNum = input("Flex Serial Number: ")
        renameQuery = input("Do you want to rename the file?[Y/n]: ").lower()

        if renameQuery=='y':
            print('Renaming file:')
            infile = renameFile(infile,serialNum)
            break
        elif renameQuery =='n':
            print('Will not rename file')
            break
        else:
            print("Error. Press y or n.")

    return (infile,serialNum)


def dummyMeasurement(infile,infile_jig):
    dummy_thickness = []
    jig_dummy_thickness = []

    with open(infile_jig) as jig_file:
        for line in jig_file:
            if ("Z" in line):
                jig_dummy_thickness.append(float((line.split()[1].replace('Z|','')).replace('|','')))

    with open(infile) as file:
        for line in file:
            if ("Z" in line):
                dummy_thickness.append(float((line.split()[1].replace('Z|','')).replace('|','')))                

    Z_dummy =  (np.array(dummy_thickness) - jig_dummy_thickness)
    print ("BM thickness average: ", mean(Z_dummy))  
    print ("BM thickness std dev: ", np.std(Z_dummy))  


def assemblyMeasurement(infile,infile_jig):

    len_Y = []
    len_X = []
    len_Z_Laser = []
    len_Z_Optical = []
    pickup_1 = []
    pickup_2 = []
    pickup_3 = []
    pickup_4 = []
    PC_1 = []
    PC_2 = []
    PC_3 = []
    HV = []
    pickup = []
    PC = []
    HV = []

    jig_pickup_1 = []
    jig_pickup_2 = []
    jig_pickup_3 = []
    jig_pickup_4 = []

    jig_PC_1 = []
    jig_PC_2 = []
    jig_PC_3 = []
    jig_HV = []




    with open(infile_jig) as jig_file:
        for line in jig_file:
            if "Pickup1" in line and "Laser" not in line:
                jig_pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                jig_pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup3" in line and "Laser" not in line:
                jig_pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))            
            if "Pickup4" in line and "Laser" not in line:
                jig_pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))        

            if "PC_1" in line and "Laser" not in line:
                jig_PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                jig_PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                jig_PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "HV" in line and "Laser" not in line:
                jig_HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
                    

    with open(infile) as file:
        for line in file:
            if "Pickup1" in line and "Laser" not in line:
                pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup3" in line and "Laser" not in line:
                pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup4" in line and "Laser" not in line:
                pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "PC_1" in line and "Laser" not in line:
                PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    

            if "HV" in line and "Laser" not in line:
                HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))


            if "distance_X" in line:
                print ("X: ", float((line.split()[1].replace('DX|','')).replace('|','')))
            if "distance_Y" in line:
                print ("Y: ", float((line.split()[1].replace('DY|','')).replace('|','')))


    pickup_1_z =  (np.subtract(jig_pickup_1, pickup_1))
    pickup_2_z =  (np.subtract(jig_pickup_2, pickup_2))
    pickup_3_z =  (np.subtract(jig_pickup_3, pickup_3))
    pickup_4_z =  (np.subtract(jig_pickup_4, pickup_4))
    print ("Pickup 1: ", abs(np.mean(pickup_1_z)), "   ", np.std(pickup_1_z))
    print ("Pickup 2: ", abs(np.mean(pickup_2_z)), "   ", np.std(pickup_2_z) )
    print ("Pickup 3: ", abs(np.mean(pickup_3_z)), "   ", np.std(pickup_3_z))
    print ("Pickup 4: ", abs(np.mean(pickup_4_z)), "   ", np.std(pickup_4_z))
    print ("Avg pickup thickness:  ", abs(np.mean([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)])))
    print ("Std Dev pickup thickness: ", np.std([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)]))

    PC_1_z =  (np.subtract(jig_PC_1, PC_1))
    PC_2_z =  (np.subtract(jig_PC_2, PC_2))
    PC_3_z =  (np.subtract(jig_PC_3, PC_3))

    print ("Average PC height:  ", abs(np.mean([np.mean(PC_1_z), np.mean(PC_2_z), np.mean(PC_3_z)])))

    HV_z = np.subtract(jig_HV, HV)
    print ("Avg HV height: ", abs(np.mean(HV_z)) )

def BMMeasurement(serialNum,infile, infile_jig,outputcsv,outputjson):
    DX_FE = 0
    DY_FE = 0
    DX_Sensor = 0
    DY_Sensor = 0
    FE_left = []
    FE_right = []
    bm = []
    FE_left_jig = []
    FE_right_jig = []
    bm_jig = []
    with open(infile) as file:
        for line in file:
            if "distance_FE_X.DX" in line:
                DX_FE = float(line.split()[1].replace('DX|','').replace('|',''))
            if "distance_FE_Y.DY" in line:
                DY_FE = float(line.split()[1].replace('DY|','').replace('|',''))
            if "distance_Sensor_X.DX" in line:
                DX_Sensor = float(line.split()[1].replace('DX|','').replace('|',''))
            if "distance_Sensor_Y.DY" in line:
                DY_Sensor = float(line.split()[1].replace('DY|','').replace('|',''))
            if "FE_left" in line:
                FE_left.append(float(line.split()[1].replace('Z|','').replace('|','')))
            if "FE_right" in line:
                FE_right.append(float(line.split()[1].replace('Z|','').replace('|','')))
            if "bm" in line:
                bm.append(float(line.split()[1].replace('Z|','').replace('|','')))

    with open(infile_jig) as file:
        for line in file:
            if "FE_left" in line:
                FE_left_jig.append(float(line.split()[1].replace('Z|','').replace('|','')))
            if "FE_right" in line:
                FE_right_jig.append(float(line.split()[1].replace('Z|','').replace('|','')))
            if "bm" in line:
                bm_jig.append(float(line.split()[1].replace('Z|','').replace('|','')))
  
    FE_left_z = (np.subtract(FE_left, FE_left_jig))
    FE_right_z = (np.subtract(FE_right, FE_right_jig))
    bm_z = (np.subtract(bm, bm_jig))

    print ("BM thickness average: ", np.mean(bm_z))  
    print ("BM thickness std dev: ", np.std(bm_z))
    print("FE Left thickness average: ", mean(FE_left_z))
    print("FE Left std dev: ", np.std(FE_left_z)) 
    print("FE Right thickness average: ", mean(FE_right_z))
    print("FE Right std dev: ", np.std(FE_right_z))
    print("FE Y Distance: ", DY_FE) 
    print("FE X Distance: ", DX_FE)
    print("Sensor Y Distance: ", DY_Sensor)
    print("Sensor X Distance: ", DX_Sensor)
    

    
    results = {
            "SENSOR_X":DX_Sensor,
            "SENSOR_Y":DY_Sensor,
            #"SENSOR_THICKNESS":623.38,
            #"SENSOR_THICKNESS_STD_DEVIATION":868.7,
            "FECHIPS_X":DX_FE,
            "FECHIPS_Y":DY_FE,
            "FECHIP_THICKNESS":np.mean(FE_left_z+FE_right_z),
            "FECHIP_THICKNESS_STD_DEVIATION":np.std(FE_left_z+FE_right_z),
            "BARE_MODULE_THICKNESS":np.mean(bm_z),
            "BARE_MODULE_THICKNESS_STD_DEVIATION":np.std(bm_z)
            }
    
    add_metrology_BM_data_json(outputjson,serialNum,1,"1",results)

# receives string infile and string serialNum
# renames file and returns new name
def renameFile(infile, serialNum):
    listFileName = infile.split('_')
    listFileName.insert(-1,serialNum)
    newName = "_".join(listFileName)

    print("Renaming file: {} ---> {}".format(infile,newName))

    os.rename(infile,newName)

    return newName



if __name__=='__main__':
    main()
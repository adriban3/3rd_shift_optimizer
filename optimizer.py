import xlrd
import xlwt
import pandas
import numpy
import matplotlib.pyplot as plt
import re

file_path = input("Please insert file location")
file_name = input("Please insert file name")

def optimizer(file_path, file_name):

    #concatenating path and file name to pull data into array
    file = file_path + file_name

    #initializing counting variables to store number of pieces by size
    thcount = 0
    shcount = 0
    twhcount = 0
    tmcount = 0
    thmcount = 0
    eicount = 0

    #reading in excel file containing job_slit_status data, converting to array, extracting lot widths column
    df = pandas.read_excel(file, header=None)
    df_arr = df.values
    mats = df_arr[1:-1,5]
    lot_widths = df_arr[1:-1,13]
    ei_mats_arr = ["A90", "A150", "A120", "APH", "PM", "RPH", "TM", "UM"]

    #for loop to count number of jobs at each size
    for index, item in enumerate(lot_widths):
        
        #check to see if job is for 300mm slitter
        if int(item) <= 300:
            thcount += 1
            
        #check if job is meant for 600mm slitter
        elif int(item) <=600:
            shcount += 1

        #check if job is meant for 1.2m slitter
        elif int(item) <=1200:
            if not any(substring in mats[index] for substring in ei_mats_arr):
                twhcount += 1

        #check if job is meant for 2m slitter
        elif int(item) <=2000:
            if not any(substring in mats[index] for substring in ei_mats_arr):
                tmcount += 1

        #check if job is meant for 3m slitter
        elif int(item) > 2000:
            if not any(substring in mats[index] for substring in ei_mats_arr):
                thmcount += 1
            
        #check if job is meant for 80in slitters
        else:
            eicount += 1

    plot_arr = [thcount, shcount, twhcount, tmcount, thmcount, eicount]
    x = ["300mm", "600mm", "1.2m", "2m", "3m", "80in"]

    plt.bar(x, plot_arr)
    plt.ylabel("Lot Width (m)")
    plt.title("Slitter Utilization")
    plt.show()

optimizer(file_path, file_name)
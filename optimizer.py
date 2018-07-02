import xlrd
import xlwt
import pandas
import numpy
import matplotlib.pyplot as plt
import re
import wx
 
def onButton(event):
    print("Button pressed.")
 
app = wx.App()
 
frame = wx.Frame(None, -1, 'win.py')
frame.SetSize(0,0,200,50)
 
# Create open file dialog
openFileDialog = wx.FileDialog(frame, "Open", "", "", 
                                      "", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
openFileDialog.ShowModal()
fileNamePath = openFileDialog.GetPath()
openFileDialog.Destroy()

def optimizer(fileNamePath):

    #initializing counting variables to store number of pieces by size
    thcount = 0
    thlsum = 0

    shcount = 0
    shlsum = 0

    twhcount = 0
    twhlsum = 0

    tmcount = 0
    tmlsum = 0

    thmcount = 0
    thmlsum = 0

    eicount = 0
    eilsum = 0

    #reading in excel file containing job_slit_status data, converting to array, extracting lot widths column
    df = pandas.read_excel(fileNamePath, header=None)
    df_arr = df.values
    mats = df_arr[1:,5]
    lot_widths = df_arr[1:,13]
    job_lengths = df_arr[1:,9]
    ei_mats_arr = ["A90", "A150", "A120", "APH", "PM", "RPH", "TM", "UM"]

    #for loop to count number of jobs at each size
    for index, item in enumerate(lot_widths):
        #check if 80in material
        if not any(substring in mats[index] for substring in ei_mats_arr):
            #check which slitter it belongs at
            if int(item) <= 300:
                thcount += 1
                thlsum += int(job_lengths[index])
            elif int(item) <= 600:
                shcount += 1
                shlsum += int(job_lengths[index])
            elif int(item) <= 1200:
                twhcount += 1
                twhlsum += int(job_lengths[index])
            elif int(item) <= 2000:
                tmcount += 1
                tmlsum += int(job_lengths[index])
            elif int(item) > 2000:
                thmcount += 1
                thmlsum += int(job_lengths[index])
        #if 80in material
        elif any(substring in mats[index] for substring in ei_mats_arr):
            #check which slitter it belongs at
            if int(item) <= 300:
                thcount += 1
                thlsum += int(job_lengths[index])
            elif int(item) <= 600: 
                shcount += 1
                shlsum += int(job_lengths[index])
            elif int(item) > 600:
                eicount += 1
                eilsum += int(job_lengths[index])

    plot_arr = [thcount*thlsum, shcount*shlsum, twhcount*twhlsum, tmcount*tmlsum, thmcount*thmlsum, eicount*eilsum]
    x = ["300mm", "600mm", "1.2m", "2m", "3m", "80in"]

    plt.bar(x, plot_arr)
    plt.ylabel("Job Length x Lot Width (m*mm)")
    plt.title("Slitter Utilization")
    for a,b in zip(x, plot_arr):
        plt.text(a,b,str(b))
    plt.show()

optimizer(fileNamePath)
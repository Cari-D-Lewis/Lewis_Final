#!/usr/bin/env python
# coding: utf-8

# # Cari Lewis Final Project
# ## Script to create new map in ArcGIS Pro, map points, and change point markers

# In[1]:


#import packages
import os
import arcpy
import arcgis
from arcgis.gis import GIS
from arcpy import env

#define the workspace environment; use double "\\" so that python reads it properly
arcpy.env.workspace="C:\\Users\\Cari\\Desktop\\Coding\\ArcGIS\\Lewis_Final_Project.aprx\\Default.gdb"
workspace=arcpy.env.workspace


# In[4]:


#define all variables
map_file="cb_2018_us_state_5m\\cb_2018_us_state_5m.shp" #HAVE to use "" otherwise ArcGIS won't recognize the map
filename="C:\\Users\\Cari\\Desktop\\Coding\\ArcGIS\\Lewis_Final_Project.aprx\\infestations.txt"
lyr_file="C:\\Users\\Cari\\Desktop\\Coding\\ArcGIS\\Lewis_Final_Project.aprx\\2020_USA_Median_Household_Income.lyrx"
file="C:\\Users\\Cari\\Desktop\\Coding\\ArcGIS\\Lewis_Final_Project.aprx\\k_pops_test.xlsx"

#reference the curent project for edits
aprx=arcpy.mp.ArcGISProject("CURRENT")

#define credentials
username="<username>"
password="<password>"

#connect to the ESRI website using credentials
gis=GIS("https://www.arcgis.com/sharing/rest/oauth2/authorize?client_id=esriapps&response_type=token&showSignupOption=true&signuptype=publicaccount&locale=en&expiration=480&redirect_uri=https%3A%2F%2Faccounts.esri.com%2Fen%2Foauth2%3Fredirect_success%3Dhttps%253A%252F%252Fwww.esri.com%252Fen-us%252Fhome", username, password)


# when working with arcpy, the format is: arcpy.<class>.<property>

# In[15]:


#insert the US map layer for the points to be mapped on
arcpy.env.overWriteOutput=True
arcpy.management.MakeFeatureLayer(map_file, "US Map")


# In[5]:


###have to download the web file as a layer file before executing this code
#call the layer file to be mapped
income_lyr=arcpy.mp.LayerFile(lyr_file)

#give the current project a location to map to
m=aprx.listMaps()[0]
m.addLayer(income_lyr, "TOP")


# In[6]:


#create empty lists for ID, longitude, latitude
ID=[]
LONG=[]
LAT=[]

#open the infestation file to file_object
with open(filename) as file_object:
    content=file_object.readlines()[1:]

#write a loop to split the columns to a new list
for i in content:
    strip_content=i.rstrip() #strips the newline characters from the lines
    split_content=strip_content.split('\t') #splits the lines at a \t character
    ID.append(split_content[0]) #appends the ID to the ID list
    LONG.append(split_content[1]) #appends the longitude coordinate to the LONG list
    LAT.append(split_content[2]) #appends the latitude coordinate to the LAT list
    
#create a new feature class that contains these points and the sample IDs
arcpy.management.CreateFeatureclass(workspace, "TestPoints_Mod", "Point","","DISABLED", "DISABLED", arcpy.SpatialReference(4269))
arcpy.management.AddField("TestPoints_Mod", "ID", "TEXT","","",20)

#open the editor
edit_points=arcpy.da.InsertCursor("TestPoints_Mod",['ID','Shape@'])

#create a loop that adds the ID and point coordinates to the new file
for x in range(0,10):
    point_obj=arcpy.Point(LONG[x],LAT[x])
    point_obj.X=LONG[x]
    point_obj.Y=LAT[x]
    strname=ID[x]
    row=[strname,point_obj]
    edit_points.insertRow(row)

#close out of the editor
del edit_points

#add the X,Y coordinates to the XY Object
arcpy.management.AddXY('TestPoints_Mod')


# In[ ]:


#convert k_pops file to ArcGIS Table
arcpy.conversion.ExcelToTable(file,'k_pops','Sheet1')

#join the k_pops file with the points file using the OBJECTID as a common field
arcpy.management.AddJoin('TestPoints_Mod', 'OBJECTID','k_pops', 'OBJECTID', 'KEEP_COMMON')

#modify the point symbols with the k cluster text file
p=arcpy.mp.ArcGISProject('CURRENT')
m=p.listMaps('Map')[0]
lyr=m.listLayers('TestPoints_Mod')[0]
sym=lyr.symbology
sym.updateRenderer('UniqueValueRenderer')
sym.renderer.fields=["Percent"]
lyr.symbology=sym

#apply the symbology to all the infestation points
for grp in sym.renderer.groups:
    for itm in grp.items:
        transVal = itm.values[0][0] #Grab the first "percent" value in the list of potential values
        itm.symbol.color = {'RGB': [0, 0, 0, int(transVal)]}
        itm.label = str(transVal)

for x in range(0,10):
    point=sym.renderer.groups[0].items[x].symbol
    point.color={'RGB' : [0,0,0,100]}
    point.size=10

lyr.symbology=sym

###it is not possible to create pies in ArcGIS Pro using Python YET; so they have to be modified by hand


# In[7]:


#extract the income level of each infestation point to a file

#use an ANOVA to determine if there is a difference between income levels and the presence of bed bugs

#is it possible to create a timelapse map with the "movement" of infestations over time?


# In[9]:





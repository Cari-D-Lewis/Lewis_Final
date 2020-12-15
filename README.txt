This README file provides the instructions on how to use this script in ArcGIS Pro to map: 

1. a shapefile 
2. a layer file 
3. infestation points using latitude/longitude coordinates 
4. and modify the symbology of the points


.......Prior to running this script.......
-make a new project in ArcGIS Pro and open the python window
-download the necessary files (see Needed files and formats) and save them in the ArcGIS Pro Project folder
-unzip the cb_2018_us_state_5m.zip file to access the U.S. states shapefile

    ***NOTE: The script called "k_pops_generator.py" is not necessary to run this program, but instead generates a random dataset of genetic clusters to use for making the pies. Currently it generates 5 clusters.***


.......Needed files and formats.......
1. shapefile ending with .shp 
    (cb_2018_us_state_5m.shp)
2. text file with the latitude/longitude of the points to be mapped. This file must only have 3 columns: first=ID, second=longitude, third=latitude.
    (infestations.txt)

    ***NOTE: if the latitude and longitude are switched, the points will be in the southern hemisphere***

3. layer file downloaded from ArcGIS Online saved with the extension .lyrx
    (2020_Median_Household_Income.lyrx)
4. excel file with the genetic clusters of each infestation. This file must only have 6 columns: first=ID, second through sixth=the proportion of that genetic cluster.
    (k_pops_test.xlsx)

    ***NOTE: if there are more or less than 5 clusters, the script will need to be modified to the correct number; this example uses 5***


.......Identify the variables.......
The beginning of the script calls all the file locations and names used throughout the script. Change these to suit the project name and file locations for the current project. NOTE: use double "\\" when using direct paths and "" when identifying files otherwise you will get an error.

1. arcpy.env.workspace= <the_path_to_the_current_geodatabase>
2. map_file= <the_path_to_the_shapefile>
3. filename= <the_path_to_the_text_file>
4. lyr_file= <the_path_to_the_layer_file>
5. file= <path_to_the_excel_file>

6.username= "ArcGIS Pro Online Username"
7.password= "ArcGIS Pro Online Password"


.......Run the script.......
Run this script either by importing the code into the python editor in ArcGIS Pro or copying and pasting it into the editor and hitting enter twice. Once the script is finished, edit the symbology of the points to be pies (See Point'n'click).


.......Point'n'click.......
Some features are not available in python yet, such as modifying the points to be pies. To do this, use the ArcGIS Pro GUI and:
1. right click the 'TestPoints_Mod' layer and select "Zoom to Layer" 
2. right click the 'TestPoints_Mod' layer and select "Symbology"
2. in the Symbology pane, click the drop down menu under "Primary Symbology" and select "Charts"
3. under chart type, select "Pie Chart"
4. in the fields menu, select each k cluster (titled a-e in this example)

The colors and sizes of the pies can be further modified using the "Appearance" and "Display" options in the Symbology pane.

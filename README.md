# plot_drifter_data_map
This is a part 2 to the output from the repository https://github.com/Tstolarz/clean_drifter_data to plot time interactive maps of the cleaned drifter track data using folium

This package is an automator application for Mac OS systems

This package takes the output cleaned csv's from the clean_drifter_data automator app and is able to instantly create time interactive track maps by drag and drop in the same fashion. 


Installation:

1. If python is not installed on the system yet, install it with miniforge using the corresponding operating system (https://github.com/conda-forge/miniforge). Open a terminal window and navigate to where the miniforge.sh was installed. Change the permissions on the file to all with the common chmod +rwx Miniforge.... If you hit tab after typing Mini it should auto complete. Then drag and drop the Miniforge.sh file onto the terminal window and complete the install process.
- If the installation process does not complete for whatever reason, then make sure to delete the Miniforge file before trying again

2. Change the permissions for the shell script to be able to execute code

3. In order to run this package you have to change the directories of the all the scripts to correspond to your system and installation of python directory.

- Edit the drifter_track_plot_app.sh file to copy over the directory of your python3 file (default install location is usually /Users/USER/miniforge3/bin/python3) and the drifter_track_plot_app.py script, replacing the paths already there.
-- If this is your first time installing python, upon completion open a terminal window and install the following packages: pandas, netcdf4 via the command "conda install pandas", "conda install netcdf4" (with no quotes).
-- If this is NOT your first time installing python, and you have virtual environments set up already, you can select the python3 in those environments which may or may not have pandas and netcdf4 and folium installed for your personal use.

- In the search bar in the top right, search for the Automator app and open it. Open the example_drifter_track_plot.app file with it by going to File>Open and navigating to the directory with the app. Copy the directory of the drifter_track_plot_app.sh and place into the automator script, replacing the text already there.

With these steps, the package SHOULD work. 


Use:

To use this application, drag and drop a CLEANED drifter.csv file onto the example_drifter_track_plot.app. This should create an interactive map for the drifter or drifters if multiple are selected.
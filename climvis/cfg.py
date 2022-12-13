"""This configuration module is a container for parameters and constants."""
import os
import pathlib

cru_dir = 'C:/Users/Surface Pro/OneDrive/Dokumente/Uni/Programmieren/project_data/'
cru_tmp_file = cru_dir + 'cru_ts4.03.1901.2018.tmp.dat.nc'
cru_pre_file = cru_dir + 'cru_ts4.03.1901.2018.pre.dat.nc'
cru_topo_file = cru_dir + 'cru_cl1_topography.nc'

# check if files are available with pathlib:
if pathlib.Path(cru_tmp_file).exists() & pathlib.Path(cru_pre_file).exists() & \
        pathlib.Path(cru_topo_file).exists():
    True
else:
    print('The CRU files are not available on this system. For cruvis (part'
          ' of the climvis package) to work properly, please create a file'
          ' called ".climvis" in your HOME directory, and indicate the path'
          ' to the CRU directory in it.')
    os.path.expanduser('~climvis')


bdir = os.path.dirname(__file__)
html_tpl = os.path.join(bdir, 'data', 'template.html')
world_cities = os.path.join(bdir, 'data', 'world_cities.csv')

default_zoom = 8

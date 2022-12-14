"""This configuration module is a container for parameters and constants."""
import os
import pathlib
import sys

def data_location():
    path_file = os.path.expanduser('~/.climvis')
    with open(path_file, 'r', encoding='utf-8') as f:
        path = f.read()
        return path


cru_dir = pathlib.Path(data_location())
cru_tmp_file = cru_dir / 'cru_ts4.03.1901.2018.tmp.dat.nc'
cru_pre_file = cru_dir / 'cru_ts4.03.1901.2018.pre.dat.nc'
cru_topo_file = cru_dir / 'cru_cl1_topography.nc'

files = [cru_tmp_file, cru_pre_file, cru_topo_file]


if all(map(os.path.exists, files)) is False:
    print('The CRU files are not available on this system. '
          'For cruvis (part of the climvis package) to work properly, '
          'please create a file called ".climvis" in your HOME directory, '
          'and indicate the path to the CRU directory in it.')
    sys.exit()
    
    
    
bdir = os.path.dirname(__file__)
html_tpl = os.path.join(bdir, 'data', 'template.html')
world_cities = os.path.join(bdir, 'data', 'world_cities.csv')

default_zoom = 8

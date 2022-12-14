"""This configuration module is a container for parameters and constants."""
import os
import pathlib
import sys

files = ['cru_ts4.03.1901.2018.tmp.dat.nc',
         'cru_ts4.03.1901.2018.pre.dat.nc',
         'cru_cl1_topography.nc']

path_file = os.path.expanduser('~/.climvis')

def data_location():
    with open(path_file, 'r', encoding='utf-8') as f:
        path = f.read()
        return path


def check_folder_files(path):
    if os.path.isdir(path) is False:
        print(f'The folder {str(path)} does not exist')
        sys.exit()
    else:
        paths = [pathlib.Path(path) / i for i in files]
        if all(map(os.path.exists, paths)) is False:
            print(f'The CRU files are not in this folder (or not all of them): {str(path)}')
            sys.exit()
    return path


def find_data():
    print('The CRU files are not available on this system. '
          'For cruvis (part of the climvis package) to work properly,'
          'you can specify the folder where the files are or '
          'create a file called ".climvis" in your HOME directory,'
          'and indicate the path to the CRU directory in it.')
    answer = input('Specify the data folder? y/n \n')
    if answer in ['y','Y','yes','Yes']:
        data_path = input('Enter the CRU files path \n')
        data_path = os.path.expanduser(f'~/{data_path}')
        climvis_file = os.path.expanduser('~/.climvis')
        with open(climvis_file,'w',encoding = 'utf-8') as f:
           f.write(str(check_folder_files(data_path)))
        print('Data: found. Now you can run the program!')
        sys.exit()
    else:
        sys.exit()
    

if os.path.exists(path_file) is False:
    find_data()
else:
    cru_dir = pathlib.Path(data_location())
    cru_tmp_file = cru_dir / files[0]
    cru_pre_file = cru_dir / files[1]
    cru_topo_file = cru_dir / files[2]

    files_path = [cru_tmp_file, cru_pre_file, cru_topo_file] 
    if all(map(os.path.exists, files_path)) is False:
        find_data()


    
bdir = os.path.dirname(__file__)
html_tpl = os.path.join(bdir, 'data', 'template.html')
world_cities = os.path.join(bdir, 'data', 'world_cities.csv')

default_zoom = 8

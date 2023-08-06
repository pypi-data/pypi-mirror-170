# -*- coding: utf-8 -*-
import os, glob, sys, math, string, time, json, logging, functools, random, yaml, operator, gc
import shutil, tarfile, zipfile
from typing import Optional, Union
import wget, yaml


from utilmy import to_file


#################################################################
from utilmy.utilmy_base import log, log2

def help():
    """function help
    """
    from utilmy import help_create
    ss = help_create(__file__)
    print(ss)


#####################################################################
def test_all():
    """
    """
    test1()





def test1():
    pass




##########################################################################################
def unzip(dirin, dirout):
    """function unzip.
    Doc::
            
            Args:
                dirin:   
                dirout:   
            Returns:
                
    """
    import  zipfile
    with zipfile.ZipFile(dirin, 'r') as zip_ref:
        zip_ref.extractall(dirout)


def zip(dirin:str="mypath", dirout:str="myfile.zip", format='zip'):
    """ zip a full dirin folder into dirout file
    Doc::
            
            https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
            Args:
                dirin:   
                dirout:   
            Returns:
                
    """
    import shutil
    shutil.make_archive(base_name=dirout,format=format,base_dir=dirin)



def gzip(dirin='/mydir', dirout="./"):
    """function gzip.
    Doc::
            
            Args:
                dirin:   
                dirout:   
            Returns:
                
    """
    #  python prepro.py gzip
    name = "_".join(dirin.split("/")[-2:])
    cmd  = f"tar -czf '{dirout}/{name}.tar.gz'   '{dirin}/'   "
    print(cmd)
    os.system(cmd)


def dir_size(dirin="mypath", dirout="./save.txt"):
    """function dir_size.
    Doc::
            
            Args:
                dirin:   
                dirout:   
            Returns:
                
    """
    os.system( f" du -h --max-depth  13   '{dirin}'  | sort -hr  > '{dirout}'  ")

    
def dataset_donwload(url, path_target):
    """Donwload on disk the tar.gz file.
    Doc::
            
            Args:
                url:
                path_target:
            Returns:
        
    """
    log(f"Donwloading mnist dataset in {path_target}")
    os.makedirs(path_target, exist_ok=True)
    wget.download(url, path_target)
    tar_name = url.split("/")[-1]
    os_extract_archive(path_target + "/" + tar_name, path_target)
    log2(path_target)
    return path_target + tar_name


def dataset_get_path(cfg: dict):
    """function dataset_get_path.
    Doc::
            
            Args:
                cfg (  dict ) :   
            Returns:
                
    """
    #### Donaload dataset
    # cfg = config_load()
    name = cfg.get("current_dataset", "mnist")
    cfgd = cfg["datasets"].get(name, {})
    url = cfgd.get("url", None)
    path = cfgd.get("path", None)
    path_default = os.path.expanduser("~").replace("\\", "/") + f"/.mygenerator/dataset/{name}/"

    if path is None or path == "default":
        path_target = path_default
    else:
        path_target = path

    #### Customize by Dataset   #################################
    if name == "mnist":
        ### TODO hardcoded per dataset source
        path_data = path_target + "/mnist_png/training/"
        fcheck = glob.glob(path_data + "/*/*")
        log2("n_file: ", len(fcheck))
        if len(fcheck) < 1:
            dataset_donwload(url, path_target)

        return path_data

    else:
        raise Exception("No dataset available")


def os_extract_archive(file_path, path=".", archive_format="auto"):
    """Extracts an archive if it matches tar, tar.gz, tar.bz, or zip formats..
    Doc::
            
            Args:
                file_path: path to the archive file
                path: path to extract the archive file
                archive_format: Archive format to try for extracting the file.
                    Options are 'auto', 'tar', 'zip', and None.
                    'tar' includes tar, tar.gz, and tar.bz files.
                    The default 'auto' is ['tar', 'zip'].
                    None or an empty list will return no matches found.
            Returns:
                True if a match was found and an archive extraction was completed,
                False otherwise.
    """
    if archive_format is None:
        return False
    if archive_format == "auto":
        archive_format = ["tar", "zip"]
    if isinstance(archive_format, str):
        archive_format = [archive_format]

    file_path = os.path.abspath(file_path)
    path = os.path.abspath(path)

    for archive_type in archive_format:
        if archive_type == "tar":
            open_fn = tarfile.open
            is_match_fn = tarfile.is_tarfile
        if archive_type == "zip":
            open_fn = zipfile.ZipFile
            is_match_fn = zipfile.is_zipfile

        if is_match_fn(file_path):
            with open_fn(file_path) as archive:
                try:
                    archive.extractall(path)
                except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
                    if os.path.exists(path):
                        if os.path.isfile(path):
                            os.remove(path)
                        else:
                            shutil.rmtree(path)
                    raise
            return True
    return False


        
        
        
        
        
        
        
##########################################################################################
################### Logs Wrapper #########################################################
"""
from loguru import logger

def log(*s):
    logger.info(",".join([str(t) for t in s]))


def log2(*s):
    logger.debug(",".join([str(t) for t in s]))


def logw(*s):
    logger.warning(",".join([str(t) for t in s]))


def loge(*s):
    logger.error(",".join([str(t) for t in s]))


def logger_setup():
    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "<level>{level: <8}</level>| <level>{message}</level>",
            }
        ]
    }
    logger.configure(**config)


logger_setup()

"""        

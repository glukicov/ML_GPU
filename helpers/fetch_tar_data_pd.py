#Download and unpack tar file from url 
#Author: Gleb Lukicov
# --fetch or --pd 
# run from JLab e.g. 
# %run helpers/fetch_tar_data_pd.py --fetch --url="https://raw.github..."s
import os, sys, argparse, tarfile, urllib
import pandas as pd

#globals 
last_percent_reported=-1 

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="full URL to file", type=str)
parser.add_argument("--local_path", help="local path to save tgz to", type=str, default=None)
parser.add_argument("--fetch", help="download and unpack", action="store_true")
args = parser.parse_args()

#Resolve system vars for local download path 
if(args.local_path == None):
    print("Assuming ENV path to the project", os.environ.get('ML_PATH'))
    local_path=os.path.join(os.environ.get('ML_PATH'), "DATA")

def main():

    if(args.fetch):
        print("Getting file", args.url)
        fetch_tar_data()


def fetch_tar_data(url=args.url):
    '''
    Download single tar file and unpack 
    ''' 
    tgz_file=os.path.join(local_path, url.split("/")[-1])

    print("Downloading", url)
    urllib.request.urlretrieve(url, tgz_file, reporthook=download_progress_hook)
    
    print("Extracting", tgz_file)
    housing_tgz = tarfile.open( tgz_file ) 
    housing_tgz.extractall(path=local_path)
       
    print("Removing .tgz file")
    housing_tgz.close()
    os.remove(tgz_file)

    print("ls in", local_path, ":", os.listdir(local_path))


def download_progress_hook(count, blockSize, totalSize, increment=10):
    '''
    Print progress every %increment
    '''
    global last_percent_reported
    percent = int(count * blockSize * 100 / totalSize)
    if last_percent_reported != percent:
        if percent % increment == 0: sys.stdout.write("%s%%" % percent); sys.stdout.flush();
        else: sys.stdout.write("."); sys.stdout.flush();
        last_percent_reported = percent
    if (percent % 100==0 and percent != 0): sys.stdout.write("\n");

if __name__=="__main__":
    main()
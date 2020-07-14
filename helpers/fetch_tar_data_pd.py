#Download and unpack tar file from url 
#Author: Gleb Lukicov
import os, argparse, tarfile, urllib
import pandas as pd

#Resolve system vars 
print("Assuming ENV path to project", os.environ.get('ML_PATH'))
local_path=os.environ.get('ML_PATH')+"/DATA/"

# --fetch or --pd 
# run from JLab e.g. run helpers/fetch_tar_data_pd.py --fetch 
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL base", type=str, 
                    default="https://raw.githubusercontent.com/ageron/handson-ml2/master/")
parser.add_argument("--path", help="path to file", type=str, default="datasets/housing/")
parser.add_argument("--file", help="file name", type=str, default="housing.tgz")
parser.add_argument("--fetch", help="download and unpack", action="store_true")
parser.add_argument("--pd", help="return PD", action="store_true")
args = parser.parse_args()

full_path = args.url + "/" + args.path + "/" + args.file

def main():

    if(args.fetch):
        print("Getting file...", full_path)
        fetch_tar_data()

    if(args.pd):
        print("Returning pandas DF from", full_path)
        return_pd()


def fetch_tar_data(housing_url=full_path, path=args.path, file=args.file):
    '''
    Download single tar file and unpack 
    ''' 
    tgz_path=local_path+"/"+path
    print("Creating new dir", tgz_path)
    os.makedirs(tgz_path, exist_ok=True) 
    print("Downloading", housing_url)
    urllib.request.urlretrieve(housing_url)
    # print("Opening", housing_url)
    # housing_tgz = tarfile.open(tgz_path+"/"+file) 
    # print("Extracting", housing_url)
    # housing_tgz.extractall(path=tgz_path) 
    # print("Done", housing_url)
    # housing_tgz.close()
    print(os.listdir(tgz_path))

def return_pd(path=args.path, file=args.file): 
    csv_path = os.path.join(path, file) 
    return pd.read_csv(csv_path)

if __name__=="__main__":
    main()
printf "\nSourcing ML PY env: ~/ML/ML_env/bin/activate\n"
# activate the gpu_ml environment
source ~/ML/ML_env/bin/activate
cd ~/ML/

# open Jupyter lab on specific port
alias jlab="jupyter lab --port=8899"
alias lr="ls -ltrh"

# usage cd.. 3 to pop 3 dirs up 
function cd_up() { cd $(printf "%0.s../" $(seq 1 $1 )) ;}
alias 'cd..'='cd_up'

# usage 'lg "My commit msg"' ; new files should be added manually 
function lg() { git add -u ; git commit -a -m "$1" ; git push ;}

function st { git status ;}
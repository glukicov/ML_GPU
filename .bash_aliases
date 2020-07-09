printf "\nSourcing ML PY env: ~/gpu_ml/bin/activate\n"

# activate the gpu_ml environment
source ~/gpu_ml/bin/activate
cd ~/gpu_ml/

# open Jupyter lab on specific port 
alias jlab="jupyter lab --port=8899"

alias lr="ls -ltrh"

# usage cd.. 3 to pop 3 dirs up
function cd_up() { cd $(printf "%0.s../" $(seq 1 $1 )) ;}
alias 'cd..'='cd_up'

# usage 'lg "My commit msg"' 
# new files should be added manually (e.g. git add FILE) 
function lg() { git add -u ; git commit -a -m "$1" ; git push ;}

function st { git status ;}
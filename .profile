# use ML as $ML in Linux (can use ip address instead of the DNS hostname) 
export ML=mlgpu.ddns.net

# just like below ;) for the magic packer command to wake-up a remote machine
alias wake_gml="wakeonlan -i $ML -p 22 b3:21:88:6k:17:24"

# open ssh tunnel from ML to the laptop in port 8899
alias sg="ssh -L 8899:localhost:8899 $ML"

# 'cd_ML' to quickly cd into the mounted directory 
alias cd_ML="cd /Users/user/Documents/Ubuntu_mount/"
#!/bin/bash

echo "SAVING FIRST FILE"
mkdir /home/codefiesta/Downloads/First
sudo cat > /home/codefiesta/Downloads/First/flag1.txt << "EOF"
CDAKJSHFNKJEL234GFLL9231BWFL1
EOF

echo "SAVING SECOND FILE:" 
mkdir /home/codefiesta/Music/Second
sudo cat > /home/codefiesta/Music/Second/flag2.txt << "EOF"
OIJONKJBHBHJBUGBSDWE123FL2
EOF

echo "SAVING THIRD FILE"
sudo mkdir /media/Third
sudo cat > /media/Third/flag3.txt << "EOF"
HGRV2FVUYV213Y4UBUAHJOIEJDFL3
EOF

echo "SAVING FOURTH FILE"
sudo mkdir /root/Fourth 
sudo cat > /root/Fourth/flag4.txt << "EOF"
BLIV3EREJH3B554CU7HWBMLPOFL4
EOF

echo "SAVING FIFTH FILE"
sudo mkdir /lib32/Fifth
sudo cat > /lib32/Fifth/flag5.txt << "EOF"
JDALSHFUIAHILEFBIASBCVAYUSBD
EOF

echo "SAVING SIXTH FILE" 
sudo mkdir /mnt/Sixth
sudo cat > /mnt/Sixth/flag6.txt << "EOF"
AWECBABVBAYWEBRUVBAUSBDHF23
EOF

echo "SAVING SEVENTH FILE"
sudo mkdir /tmp/Seventh
sudo cat > /tmp/Seventh/flag7.txt << "EOF"
NBNASD23BFUABUBAW5UBEBFUAWB
EOF

echo "RUNNING DEPENDENCY SCRIPT"

python3 hint2_dependency.py

echo "DONE"

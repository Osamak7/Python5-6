ls -l
mkdir $home/cercaStringa
cp "./myenv"  "./cerca.py" $home/cercaStringa
cd $home/cercaStringa
pip install virtualenv
virtualenv myenv
source myenv/bin/activate
pip install -r requirements.txt

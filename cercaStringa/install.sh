ls -l
mkdir $HOME/cercaStringa
cp "./myenv"  "./cerca.py" "./requirements.txt" "./uninstall.sh" $HOME/cercaStringa
cd $HOME/cercaStringa
pip install virtualenv
virtualenv myenv
source myenv/bin/activate
pip install -r requirements.txt

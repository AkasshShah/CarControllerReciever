MYDIR = "$(dirname "$(which "$0")")"
PATHTOSCRIPT = "${MYDIR}/main.py"
echo "$PATHTOSCRIPT"
while true ; do
    /usr/bin/python3 $PATHTOSCRIPT
done
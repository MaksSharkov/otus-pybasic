#! /usr/bin/env sh
echo "MaksSh prestart script is running..."
flask -A main:app db upgrade
echo "MaksSh prestart script is done..."
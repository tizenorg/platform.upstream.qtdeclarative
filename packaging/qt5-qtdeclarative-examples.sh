#!/bin/sh

ls /usr/share/qt5/qt5-qtdeclarative/examples/quick/demos/*/*.qml \
    | while read t ; do
    qmlscene "$t" ;
done

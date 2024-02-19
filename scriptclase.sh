#!/bin/bash
filenam='largetext.txt' 
prefix='output'
split -l 1000 $filenam $prefix
tar cvfz output.tar.gz $prefix*
origen='clasebatch'
destino='salidabatch'
rm -r $origen
mkdir $origen
rm $destino
mkdir $destino
mv output.tar.gz $destino/outpot2.tar.gz
cd $destino
tar xvfz outpot2.tar.gz
rm output2.tar.gz
cat 'prefix*'>texto.txt
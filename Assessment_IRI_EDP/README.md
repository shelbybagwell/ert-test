# Assessment: IRI EDP
This directory contains my work toward the IRI EDP assessment.

## How to run
Download the IRI source code at http://irimodel.org/IRI-2020/00_iri.zip and put it in this directory.
Download the IRI common files at http://irimodel.org/COMMON_FILES/00_ccir-ursi.zip and put it in this directory.
No need to unzip, the Makefile will handle that for you.
You will also need to download the data for this model.
It can be found at http://irimodel.org/incdices/ig_rz.dat and https://chain-new.chain-project.net/echaim_downloads/apf107.dat

To run this code, you need to have `gfortran` and `gnuplot` installed on your device.

Once the necessary files are downloaded and the dependencies are installed, run the following steps:

1. `make`
2. `gcc -o iri iri.c -L. -liri2020`
3. `./iri`
4. `gnuplot plot_iri.gp`

## Takeaways
This was a challenging excercise for me, but in a good way. I have never worked with Fortran code before, and it has been a while since I've been this hands-on with C. I definitely ran into some frustrating bugs, and some situations where having a senior developer I could ask for guidance would have been a big help, but overall once I got a grasp on the IRI documentation, it was straightforward.

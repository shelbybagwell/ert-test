set terminal pngcairo size 800,600 enhanced font 'Arial,12'
set output 'electron_density.png'

set logscale x
set ylabel "Altitude (km)"
set xlabel "Electron Density (m^{-3})"
set grid

set output 'edp_plot_2021-03-03.png'
set title "Electron Density vs Altitude \nIRI Model — 2021-03-03 at 11:00 UTC"
plot "edp_output_2021-03-03.dat" using 2:( $1 > 0 ? $1 : 1/0 ) with linespoints title "IRI Model"
unset output

set output 'edp_plot_2021-03-04.png'
set title "Electron Density vs Altitude \nIRI Model — 2021-03-04 at 23:00 UTC"
plot "edp_output_2021-03-04.dat" using 2:( $1 > 0 ? $1 : 1/0 ) with linespoints title "IRI Model"
unset output


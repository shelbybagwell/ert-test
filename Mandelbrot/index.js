#!/usr/bin/env node

const {Command} = require('commander');
const {math} = require('mathjs');

const program = new Command();

program
    .name('mandelbot')
    .description('solves the mandelbrot equation')
    .version('1.0.0');

// Define program options
program
    .option('-x, --center-x', 
        'x-coordinate of the center of the view')
    .option('-y, --center-y', 
        'y-coordinate of the center of the view')
    .option('-w, --width', 
        'width of the view')
    .option('-h, --height', 
        'height of the view')
    .option('-s, --step', 
        'resolution of the view (size of a pixel)')
    .option('-n, --max-iterations', 
        'maximum number of iterations to perform at each pixel', 
        100)
    .option('-b, --bound', 
        'divergence cutoff. If the abs(z) >= bound, the iterations stop.', 
        2)
    .option('-p, --power', 
        'exponent used in the mandelbrot equation', 
        2);

// Define program actions
program.action((options) => {
    let minX = options.center-x - options.width;
    let maxX = options.center-x + options.width;
    let minY = options.center-y - options.height;
    let maxY = options.center-y + options.height;

    // Create evenly spaced array
    let x_domain = linspace(minX, maxX, options.step);
    let y_domain = linspace(minY, maxY, options.step);

    let iterArr = [];

    for (let i=0; i<y_domain.length; i++) {
        let row = [];
        for (let j=0; j<x_domain.length; j++) {
            let z = 0;
            let p = options.power;
            let c = math.complex(x_domain[j], y_domain[i]);
            let invalid = false;
            for (let k=0; k<options.max-iterations; k++) {
                if (Math.abs(z) >= options.bound) {
                    row.push(k);
                    invalid = true;
                    break;
                } else {
                    try {
                        z = z**p + c;
                        row.push(0);
                    } catch (error) {
                        console.log("An error occurred", error)
                    }
                }
            }
            if (!invalid) {
                row.push(0);
            }
        }
        iterArr.push(row);
    }


})

/*
Creates an evenly spaced array given a starting value,
stopping value, and the number of elements desired.
*/
function linspace(start, stop, count) {
    const step = (stop - start) / (count - 1);
    let arr = [];
    for (let i = 0; i < count; i++) {
        arr.push(start + (step*i));
    }
}
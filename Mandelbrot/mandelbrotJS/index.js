#!/usr/bin/env node

const {Command} = require('commander');
const math = require('mathjs');

const program = new Command();

program
    .name('mandelbot')
    .description('solves the mandelbrot equation')
    .version('1.0.0');

// Define program action and options
program
    .command('mandelbrot')
    .argument('-x, --center-x', 
        'x-coordinate of the center of the view', parseFloat)
    .argument('-y, --center-y', 
        'y-coordinate of the center of the view', parseFloat)
    .argument('-w, --width', 
        'width of the view', parseFloat)
    .argument('-h, --height', 
        'height of the view', parseFloat)
    .argument('-s, --step', 
        'resolution of the view (size of a pixel)', parseFloat)
    .argument('-n, --max-iterations', 
        'maximum number of iterations to perform at each pixel', parseInt, 
        100)
    .argument('-b, --bound', 
        'divergence cutoff. If the abs(z) >= bound, the iterations stop.', parseFloat, 
        2)
    .argument('-p, --power', 
        'exponent used in the mandelbrot equation', parseFloat, 
        2)
    .action((centerX, centerY, width, height, step, maxIterations, bound, power, options) => {
        let minX = centerX - width;
        let maxX = centerX + width;
        let minY = centerY - height;
        let maxY = centerY + height;

        // Create evenly spaced array
        let x_domain = linspace(minX, maxX, step);
        let y_domain = linspace(minY, maxY, step);

        let iterArr = [];

        for (let y of y_domain) {
            let row = [];
            for (x of x_domain) {
                let z = math.complex(0,0);
                let p = options.power;
                let c = math.complex(x, y);
                let invalid = false;
                for (let iter=0; iter<maxIterations; iter++) {
                    if (Math.abs(z) >= bound) {
                        // Out of bounds, cannot be part of mandelbrot set
                        row.push(iter); // Return the index at which it converged
                        invalid = true;
                        break;
                    } else {
                        try {
                            z = math.add(math.pow(z, p), c);
                        } catch (error) {
                            console.log("An error occurred", error)
                        }
                    }
                }
                if (!invalid) {
                    // It is part of the mandelbrot set
                    row.push(0);
                }
            }
            iterArr.push(row);
        }

        // Output the data
        console.log(iterArr);
    })

program.parse(process.argv);

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
    return arr;
}
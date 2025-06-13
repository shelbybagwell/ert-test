#!/usr/bin/env node

const {Command} = require('commander');

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
})
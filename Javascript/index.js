$(function() {
    $("#myButton").on("click", function(event) {
        const canvas = document.getElementById("mycanvas");
        const ctx = canvas.getContext('2d');
        var rect = canvas.getBoundingClientRect();

        // draw the circle
        var radius = 100;
        ctx.beginPath();
        ctx.arc(radius, radius, radius, 0, 2 * Math.PI);
        ctx.fillStyle = 'red';
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.stroke();
        ctx.closePath();

        var radX = 20;
        var radY = 45;
        var centX = canvas.width - radX;
        var centY = canvas.width - radY;
        ctx.beginPath();
        ctx.ellipse(centX, centY, radX, radY, 0, 0, Math.PI*2);
        ctx.fillStyle = 'blue';
        ctx.fill();
        ctx.stroke();
        ctx.closePath();
    });
});
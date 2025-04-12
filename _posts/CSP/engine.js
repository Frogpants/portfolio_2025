
function intializeCanvas() {
    const canvas = document.getElementById("draw");
    const ctx = canvas.getContext("2d");
};

intializeCanvas();

// Camera Setup
const cam = {
    x: 0,
    y: 0,
    z: 0,
    rotx: 0,
    roty: 0,
    FOV: 90
};

var ray = {
    x: 0,
    y: 0,
    z: 0
};

function distance(x,y,z) {
    return Math.sqrt(x*x+y*y+z*z);
};
function normalize3D(x1,y1,z1) {
    mag = distance(x1,y1,z1);
    return {x:x1/mag,y:y1/mag,z:z1/mag};
};

function rotateRay() {
    ray.x = ray.x * Math.cos(Math.radians(cam.rotx)) - ray.z * Math.sin(Math.radians(cam.rotx));
    ray.z = ray.x * Math.sin(Math.radians(cam.rotx)) + ray.z * Math.cos(Math.radians(cam.rotx));

    ray.y = ray.y * Math.cos(Math.radians(cam.roty)) - ray.z * Math.sin(Math.radians(cam.roty));
    ray.z = ray.y * Math.sin(Math.radians(cam.roty)) + ray.z * Math.cos(Math.radians(cam.roty));
};

function pixel(u,v) {
    ray.x = u;
    ray.y = v;
    ray.z = cam.FOV;
    rotateRay();
    ray = normalize3D(...ray);
    
};

function lighting() {
    // ignore
};

function moveCam(speed) {
    cam.x += speed * Math.sin(cam.rotx);
    cam.z += speed * Math.cos(cam.rotx);
};

function controls(speed, keyPressed) {
    if (keyPressed === "ArrowRight") {
        cam.rotx += speed;
    } else if (keyPressed === "ArrowLeft") {
        cam.rotx -= speed;
    } else if (keyPressed === "ArrowUp") {
        cam.roty += speed;
    } else if (keyPressed === "ArrowDown") {
        cam.roty -= speed;
    }
    if (keyPressed === "w") {
        moveCam(speed);
    } else if (keyPressed === "s") {
        moveCam(-speed);
    }
    cam.rotx += 90;
    if (keyPressed === "d") {
        moveCam(speed);
    } else if (keyPressed === "a") {
        moveCam(-speed);
    }
    cam.rotx -= 90;
};

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    requestAnimationFrame(render);
};

render();

document.addEventListener('keydown', (event) => {
    controls(4,event.key);
});


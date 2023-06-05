function init_draw() {
    canvas = document.getElementById("webgl");
    if (canvas.getContext) {
        ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        ctx.fillStyle = "rgb(0,0,200,0.5)";
        ctx.fillRect(30,30,50,50);

        ctx.fillStyle = "rgb(200,0,0)";
        ctx.fillRect(10,10,50,50);
    } else {
        alert("해당 컨텐츠를 지원하지 않는 브라우저 입니다.")
    }
}

function clear_canvas() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
}
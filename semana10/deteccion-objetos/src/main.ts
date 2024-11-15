import "./style.css";

window.onload = () => {
  showVideo();
};

const video = document.getElementById("video") as HTMLVideoElement;
const canvas = document.getElementById("canvas") as HTMLCanvasElement;

const GREEN = {
  r: 0,
  g: 255,
  b: 0,
};

const processVideo = () => {
  const ctx = canvas.getContext("2d");

  if (ctx) {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const pixels = imageData.data;

    let shortestDistance = null;
    let moreGreenPixel = null;

    let sumX = 0;
    let sumY = 0;
    let count = 0;

    for (let i = 0; i < pixels.length; i += 4) {
      const color = {
        r: pixels[i],
        g: pixels[i + 1],
        b: pixels[i + 2],
        a: pixels[i + 3],
      };

      const distance = Math.sqrt(
        Math.pow(GREEN.r - color.r, 2) +
          Math.pow(GREEN.g - color.g, 2) +
          Math.pow(GREEN.b - color.b, 2)
      );

      if (distance < 200) {
        pixels[i] = 0;
        pixels[i + 1] = 0;
        pixels[i + 2] = 255;

        const y = Math.floor(i / canvas.width / 4);
        const x = (i / 4) % canvas.width;

        sumX += x;
        sumY += y;
        count++;
      }

      // if (shortestDistance === null || distance < shortestDistance) {
      //   shortestDistance = distance;
      //   const y = Math.floor(i / canvas.width / 4);
      //   const x = (i / 4) % canvas.width;

      //   moreGreenPixel = {
      //     x,
      //     y,
      //   };
      // }
    }

    ctx.putImageData(imageData, 0, 0);

    if (count > 0) {
      ctx.fillStyle = "#f00";
      ctx.beginPath();
      ctx.arc(sumX / count, sumY / count, 10, 0, 2 * Math.PI);
      ctx.fill();
    }

    // if (moreGreenPixel) {
    //   ctx.fillStyle = "#00f";
    //   ctx.beginPath();
    //   ctx.arc(moreGreenPixel.x, moreGreenPixel.y, 10, 0, 2 * Math.PI);
    //   ctx.fill();
    // }

    setTimeout(processVideo, 30);
  }
};

const showVideo = () => {
  const options = {
    audio: false,
    video: {
      width: 720,
      height: 720,
    },
  };

  if (navigator.mediaDevices.getUserMedia !== undefined) {
    navigator.mediaDevices.getUserMedia(options).then((stream) => {
      video.srcObject = stream;
      processVideo();
    });
  } else {
    alert("getUserMedia() no soportado");
  }
};

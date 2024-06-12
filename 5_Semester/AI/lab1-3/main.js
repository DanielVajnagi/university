

const fileInput = document.querySelector("#fileInput");
const addEtalonBtn = document.querySelector("#addEtalonBtn");
const recognizeBtn = document.querySelector(".recognizeBtn");
const recognizeOut = document.querySelector(".output");




let pixelColors;
let n;
const meshSize = 4; 


let fileName = "";
let clasters = {};
let vector;


function normVector(vector){
  return vector.map((num) => num / Math.max(...vector));
}
function getAvgVector(x1,x2){
    
  return x1.map((obj, index)=> (obj + x2[index])/2); 
}

function getDistance(x1, x2){

  let distance = 0;

  for(let i = 0; i < x1.length;i++){
      distance += Math.abs(x1[i] - Math.pow(x2[i], 2));  
  }

  return distance;
}

fileInput.addEventListener("change", async () => {

  
    let imageFile = fileInput.files[0];
    fileName = imageFile.name.split("_")[0];

    const reader = new FileReader();
    reader.onload = async () => {
      const imageBuffer = reader.result;

      const img = document.createElement('img');
      img.src = URL.createObjectURL(imageFile);

      img.onload = async () => {
        const canvas = document.querySelector('#canvas');
        const ctx = canvas.getContext('2d');

        canvas.width = img.width;
        canvas.height = img.height;

        n = img.width;

        ctx.drawImage(img, 0, 0, img.width, img.height);

        const imageData = ctx.getImageData(0, 0, img.width, img.height);

        pixelColors = imageData.data;
        console.log(pixelColors)
        vector = generateVector(pixelColors);
      };

      // Завантажте зображення
      img.src = URL.createObjectURL(imageFile);
    };

    reader.readAsArrayBuffer(imageFile);;
  
});


function generateVector(pixels) {

  let colorBits = [];
  let vector = [];

  for (let i = 0; i <= pixels.length - meshSize; i += meshSize) {
    colorBits.push(pixels[i] === 0 ? 1 : 0);
  }

  console.log("colorBits", colorBits, "Довжина", colorBits.length);

  for (let i = 0; i < n * n - n; i += n * 2) {
    for (let j = 0; j < n; j += Math.sqrt(meshSize)) {

      let count = 0;

      count += colorBits[i + j];
      count += colorBits[i + j + 1];
      count += colorBits[i + j + 12];
      count += colorBits[i + j + 13];

      vector.push(count);
      count = 0;

    }
  }

  vector = normVector(vector);
  console.log(vector)

  return vector;
}

addEtalonBtn.addEventListener("change", async () => {
  console.log(addEtalonBtn.files)
  for (let i = 0; i < addEtalonBtn.files.length; i++) {
    let imageFile = addEtalonBtn.files[i];

    const img = document.createElement('img');
    img.src = URL.createObjectURL(imageFile);


    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');

    img.onload = async () => {
      
      const ctx = canvas.getContext('2d');

      canvas.width = img.width;
      canvas.height = img.height;

      n = img.width;

      ctx.drawImage(img, 0, 0, img.width, img.height);

      const imageData = ctx.getImageData(0, 0, img.width, img.height);

      pixelColors = imageData.data;

      vector = generateVector(pixelColors);

      //console.log(vector)
      fileName = imageFile.name.split("_")[0];

      if (fileName in clasters)
        clasters[fileName] = getAvgVector(clasters[fileName], vector);
      else
        clasters[fileName] = vector;
      console.log(fileName);
      console.log(clasters);

      localStorage.setItem("clasters", JSON.stringify(clasters));
      
    };
  }
})


recognizeBtn.addEventListener("click", () => {
  if (!fileInput.files[0]) {
    recognizeOut.textContent = "Виберіть зображення";
    return;
  }

  clasters = JSON.parse(localStorage.getItem("clasters"));

  let recognizedNumber = recognize(vector);

  recognizeOut.textContent = "Відповідь: " + recognizedNumber;


})

function recognize(x2) {

  let minDistance = Infinity, distance;
  let number;

  console.log("!!!", clasters)
  for (let key in clasters) {

    distance = getDistance(clasters[key], x2);

    if (minDistance > distance) {
      number = key;
      minDistance = distance;
    }
  }

  console.log(distance);

  return number;
}



function doFactorial(){
    let x=document.querySelector("#task1 input").value;
    let factorial=1, double_factorial=1;
    let resultOut=document.querySelector("#result1");
    for(let i=1; i<=x;i++){
        factorial*=i;
    }
    for(let i=x; i>=1;i-=2){
        double_factorial*=i;
    }
    resultOut.innerHTML=`Factorial of number equals ${factorial}.<br>Double Factorial of number equals ${double_factorial}`
}
function doCount(){
    let input=document.querySelector("#task2 input").value;
    let arr=input.toString();
    arr=arr.split(" ")  
    let res=[];
    for (let i=0;i<arr.length;i++){
        rep=0
        for(let j=0;j<res.length;j++){
            if(arr[i]==res[j].text){
                res[j].reps++;
                rep=1;
            }
        }
        if(rep==0 && arr[i]!=""){
            res.push({text:arr[i], reps:1});
        }
    }
    document.getElementById("result2").innerHTML=""
    for(i=0;i<res.length;i++){
    document.getElementById("result2").innerHTML+="Fragment \""+res[i].text+"\" has "+res[i].reps+" reps.<br>";
    }
}
function removeSpaces(){
    let input=document.querySelector("#task3 input").value;
    let arr=input.toString();
    arr=arr.split(" ")  
    console.log(arr)
    res=arr.join(' ');
    document.getElementById("result3").textContent=res;
}
// НА3-головна, ЯРК3-допоміжна

let epsilon, h_0, h_optimal;
const x_0 = 1, y_0 = 1, t_0 = 0;
epsilon = 0.000001
h_0 = 0.1
h_optimal = find_h_optimal(h_0, epsilon)
console.log(h_optimal)

function f(x, y, t) {
    return t / y
}

function g(x, y, t) {
    return -t / x
}

function find_h_optimal(h_0, epsilon, x_1, y_1) {
    if (x_1 == null && y_1 == null) {
        x_1 = x_0 + h_0 * (f(x_0, y_0, t_0))
        y_1 = y_0 + h_0 * (g(x_0, y_0, t_0))
    }
    x_avg = x_0 + h_0 / 2 * (f(x_0, y_0, t_0))
    y_avg = y_0 + h_0 / 2 * (g(x_0, y_0, t_0))
    x_1_new = x_avg + h_0 / 2 * (f(x_avg, y_avg, t_0 + h_0 / 2))
    y_1_new = y_avg + h_0 / 2 * (g(x_avg, y_avg, t_0 + h_0 / 2))
    if (Math.abs(x_1 - x_1_new) + Math.abs(y_1 - y_1_new) > epsilon) {
        console.log("Not In range")
        h_optimal = find_h_optimal(h_0 / 2, epsilon, x_avg, y_avg);
        return h_optimal
    }
    else {
        console.log("In range")
        h_optimal = h_0 / 2
        return h_optimal;
    }
}
const arrayRange = (start, stop, step) =>
    Array.from(
        { length: (stop - start) / step + 1 },
        (value, index) => parseFloat((start + index * step).toFixed(5))
    );
t = arrayRange(0, 1, h_optimal)


//Вираховуєм точні значення

let x_accurate = calculate_x_accurate(t)
function calculate_x_accurate(t) {
    let x_accurate = []
    for (i in t) {
        x_accurate[i] = Math.exp(t[i] ** 2 / 2)
    }
    return x_accurate
}
let y_accurate = calculate_y_accurate(t)
function calculate_y_accurate(t) {
    let y_accurate = []
    for (i in t) {
        y_accurate[i] = Math.exp(-(t[i] ** 2 / 2))
    }
    return y_accurate
}


let x = [], y = [];
x[0] = x_0;
y[0] = y_0;


function RK3_x(t, x, y, n) {
    function K1(n) {
        return f(x[n], y[n], t[n])
    }
    function K2(n) {
        return f(x[n], y[n] + (h_optimal / 3) * K1(n), t[n] + h_optimal / 3)
    }
    function K3(n) {
        return f(x[n], y[n] + (h_optimal * 2 / 3) * K2(n), t[n] + h_optimal * 2 / 3)
    }
    return x[n - 1] + (h_optimal / 4) * (K1(n - 1) + 3 * K3(n - 1))
}

function RK3_y(t, x, y, n) {
    function K1(n) {
        return g(x[n], y[n], t[n])
    }
    function K2(n) {
        return g(x[n] + (h_optimal / 3) * K1(n), y[n], t[n] + h_optimal / 3)
    }
    function K3(n) {
        return g(x[n] + (h_optimal * 2 / 3) * K2(n), y[n], t[n] + h_optimal * 2 / 3)
    }
    return y[n - 1] + (h_optimal / 4) * (K1(n - 1) + 3 * K3(n - 1))
}
x[1] = RK3_x(t, x, y, 1)
y[1] = RK3_y(t, x, y, 1)
console.log(y[1])
function NA3_x(t, x, y, n) {
    x_n0=x[n-1]+f(x[n-1],y[n-1],t[n-1])
    y_n0=y[n-1]+g(x[n-1],y[n-1],t[n-1])

    do{
    x_n1=x[n - 1] + (h_optimal / 12) * (5 * f(x_n0, y_n0, t[n]) + 8 * f(x[n - 1], y[n - 1], t[n - 1]) - f(x[n - 2], y[n - 2], t[n - 2]))
    y_n1=y[n - 1] + (h_optimal / 12) * (5 * g(x_n0, y_n0, t[n]) + 8 * g(x[n - 1], y[n - 1], t[n - 1]) - g(x[n - 2], y[n - 2], t[n - 2]))
    if((Math.abs(x_n1-x_n0)+Math.abs(y_n1-y_n0))<epsilon){
       return [x_n1,y_n1]
    }
    else{
         x_n0=x_n1;
        y_n0=y_n1;
        console.log(n+'iter')
        
    }

    }
    while(true)
        
     
}
for(i=2;t[i]<=1;i++){
    xy_i=NA3_x(t,x,y,i);
    x[i]=xy_i[0];
    y[i]=xy_i[1];

}
console.log(x[640])
console.log(x_accurate[640])
console.log(y[640])
console.log(y_accurate[640 ])





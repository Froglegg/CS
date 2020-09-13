let num = 19;
let isNeg = false;
let result = "";

if (num < 0) {
  isNeg = true;
  num = Math.abs(num);
}

if (num === 0) {
  result = "0";
}
while (num > 0) {
  result += (num % 2).toString();
  num = Math.floor(num / 2);
}
if (isNeg) {
  result = `- ${result}`;
}

console.log(`${result} is ${num} in Binary`);

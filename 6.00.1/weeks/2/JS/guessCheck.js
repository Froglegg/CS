const x = 25;
const epsilon = 0.01;
const step = 0.1;
let guess = 0.0;

while (guess <= x) {
  if (Math.abs(Math.pow(guess, 2) - x) < epsilon) {
    break;
  } else {
    guess += step;
  }
}
if (Math.abs(Math.pow(guess, 2) - x) >= epsilon) {
  console.log("failed");
} else {
  console.log(`Succeded: sq root of ${x} is ${guess}`);
}

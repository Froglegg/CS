const x = 25;
const epsilon = 0.001;
let guesses = 0;
let low = 0.0;
let high = x;
let ans = high + low / 2;

while (Math.abs(Math.pow(ans, 2) - x) >= epsilon) {
  console.log(`Low: ${low} High: ${high} ANS:${ans}`);
  guesses += 1;
  if (Math.pow(ans, 2) < x) {
    low = ans;
  } else {
    high = ans;
  }
  ans = (high + low) / 2.0;
}
console.log(`NUmber of gueses ${guesses}`);
console.log(`${ans} is close to the sq root of ${x}`);
// while abs(ans**2 - x) >= epsilon:
//     print(f"Low: {low} High: {high} ANS:{ans}")
//     guesses += 1
//     if ans**2 < x:
//         low = ans
//     else:
//         high = ans
//     ans = (high + low) / 2.0
// print(f"num of guesses: {guesses}")
// print(f"{str(ans)} is close to the sq root of {x}")

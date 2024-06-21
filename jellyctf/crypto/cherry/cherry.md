# cherry
Point count: 871pts

Difficulty: hard

Provided files: cherry_dist.zip

Description:
>A Starknight hacked an old slot machine and turned it into something strange?! I heard that you win a secret message if you manage to get triple cherries, but...

URL: https://cherry.jellyc.tf/
# 

There are 32768 symbols, the first of which is the cherry.

According to `static/script.js`, the symbols in the slots are controlled by `slotIndices`
This means that we must get `slotIndices` to `[0, 0, 0]`.
slotIndices can have one of three start values.
```
function reset() {
  if (ciphertextIndex == 0)       slotIndices = [10992, 30978, 12520];
  else if (ciphertextIndex == 1)  slotIndices = [30983,  7390,   481];
  else if (ciphertextIndex == 2)  slotIndices = [25974, 26744,  9122];
  spinCounts = [0,0,0];
  updatePlaintextDisplay();
  doSpinCleanup();
}
```
These are looped through by the `change` function:
```
function change() {
  ciphertextIndex = (ciphertextIndex + 1) % 3;
  reset();
}
```
Each time we spin, we add a different amount to each index of slotIndices depending on `slotSpins`.
```
function spin() {
  const buttons = document.querySelectorAll('.button');
  buttons.forEach((b) => b.disabled = true);
  spinCounts[spinMode] += 1;
  updateModeDisplay();
  updatePlaintextDisplay();
  doSpinAnimation();
  for (let columnIndex = 0; columnIndex < 3; columnIndex++) {
    slotIndices[columnIndex] = (slotIndices[columnIndex] + slotSpins[columnIndex]) % m;
  }
  setTimeout(() => {
    doSpinCleanup();
    buttons.forEach((b) => b.disabled = false);
  }, 1800)
}
```
`slotSpins` can be set to 3 different presets by changing coins.
```
function playCoin(n){
  spinMode = n;
  if (n == 0)       slotSpins = [ 19,  22,  19];
  else if (n == 1)  slotSpins = [ 32,  27,  29];
  else if (n == 2)  slotSpins = [347, 349, 353];
  updateModeDisplay();
}
```
The number of spins of each coin is converted to a 9 character string with awascii.
```
let awascii32 = 'awjelyhosiumpcntbdfgr.,!{}_/;CTF';
...
function updatePlaintextDisplay() {
  let decToAwascii32 = (x) => {return awascii32.charAt(x % 32) + awascii32.charAt((x >> 5) % 32) + awascii32.charAt((x >> 10) % 32)};
  document.getElementById('spinCount0').innerHTML = decToAwascii32(spinCounts[0]);
  document.getElementById('spinCount1').innerHTML = decToAwascii32(spinCounts[1]);
  document.getElementById('spinCount2').innerHTML = decToAwascii32(spinCounts[2]);
}
```
Therefore we will obtain the flag by getting 3 cherries from each `slotIndices` starting value and concatenating each string.
The values of `slotIndices` are modulo `32768`, so this is a simple modular linear algebra problem with 3 systems of equations.

Each of the 3 systems has 3 variables, so we will have 9 nonnegative integers less than 32768 which we can convert to awascii to get the flag.

Script: `sol.py`

Flag: `jellyCTF{you_won_cherries!}`

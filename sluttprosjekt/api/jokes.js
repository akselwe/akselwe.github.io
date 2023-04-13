/* 
Aksel api læring javascript 
Dato: 27. jan 2022

toturial : https://www.youtube.com/watch?v=ki00QtsoiJU
*/

const jokeButtom = document.querySelector(".getJoke");
const jokeHolder = document.querySelector(".joke");

const buttomTekst = [
    "Ugh..", 
    "Wtf dad.", 
    "Are you serious?",
    "Please stop.",
    "You are embarrising",
    "Thats was your last.",
    "Jesus.",
];
async function fetchJoke(){
    const response = await fetch("https://icanhazdadjoke.com", {
        headers: {
            Accept: "application/json"
        },
    });
    const data = response.json();
        //console.log(data["joke"]) // data["joke"] er der vitsen ligger, key/value
        return data;
}
async function handleClick(){
    const { joke } = await fetchJoke();
    //console.log(joke);
    jokeHolder.textContent = joke;
    jokeButtom.textContent = randomFromArray(buttomTekst, jokeButtom.textContent);
}
function randomFromArray(arr, not) {
    const item = arr[Math.floor(Math.random() * arr.length)];
    if (item == not){
        console.log("Ah! We used that one last time, look again");
        return randomFromArray(arr, not);
    }
    return item;
}
jokeButtom.addEventListener("click", handleClick);


/* 
Aksel api læring start javascript
Dato: 27. jan 2022

toturial : https://www.youtube.com/watch?v=ki00QtsoiJU
*/

const jokeButtom = document.querySelector(".getJoke");
const jokeHolder = document.querySelector(".joke");

/* array for random tekst til knappen */
const buttomTekst = [
    "Ugh..", 
    "Wtf dad.", 
    "Are you serious?",
    "Please stop.",
    "You are embarrising",
    "Thats was your last.",
    "Jesus.",
];

/* her er funksjonen, men fent til den blir brukt */
async function fetchJoke(){
    /* fetch en repsons fra nettsiden, hent fra adresse Accept: */
    const response = await fetch("https://icanhazdadjoke.com", {
        headers: {
            Accept: "application/json"
        },
    });
    const data = response.json();
        //console.log(data["joke"]) // data["joke"] er der vitsen ligger, key/value
        return data;
}

/* funksjonen for å hente key/value av data som returneres fra fetchJoke() */
async function handleClick(){
    const { joke } = await fetchJoke();
    //console.log(joke);
    jokeHolder.textContent = joke;
    /* tekst til knappen */
    jokeButtom.textContent = randomFromArray(buttomTekst, jokeButtom.textContent);
}

/* tekst til knappen */
function randomFromArray(arr, not) {
    const item = arr[Math.floor(Math.random() * arr.length)];
    if (item == not){
        //console.log("Brukt, trykk på nytt.");
        return randomFromArray(arr, not);
    }
    return item;
}
jokeButtom.addEventListener("click", handleClick);

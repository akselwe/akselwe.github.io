/* isIntersecting er en api man kan bruke for å sjekke om noe på siden er på skjermen eller ikke */

//observerer er et objekt, som tar inn en callbackfunc i konstruktøren
const observerer = new IntersectionObserver((entries) => {
    // for each er en lettere metode å loope gjennom -- entry blir hvert 
    entries.forEach((entry)=>{
        if (entry.isIntersecting){
            entry.target.classList.add('show')
        }
        //else{entry.target.classList.remove('show')}
    })
});

let hiddenEl = document.querySelectorAll('.hidden');
hiddenEl.forEach((el) => observerer.observe(el));
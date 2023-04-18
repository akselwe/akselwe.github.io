let menuBtn = document.querySelector("#menu-btn")
let navbarEl = document.querySelector('.navbar')
let searchForm = document.querySelector(".search-form")
let seachBtn = document.querySelector("#search-btn")

/* nav slide til senere bruk, for å ha bare */
let navLinks = document.querySelectorAll('.link')
const navSlide = () => {
    //animasjon link
    navLinks.forEach((link, index) => {
        if(link.style.animation){
            link.style.animation = '';
        } else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
        }
    });
}

/* når meny trykkes, fjern de andre som er aktive */
menuBtn.onclick = () =>{
    navbarEl.classList.toggle('active')
    searchForm.classList.remove("active")
}

/* når search trykkes, fjern de andre som er aktive*/
seachBtn.onclick = () =>{
    searchForm.classList.toggle("active")
    navbarEl.classList.remove("active")
}

/* når vinduet scroller, fjern det som er aktivt */
window.onscroll = () => {
    navbarEl.classList.remove("active")
    searchForm.classList.remove("active")
}



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
/* liste med alle .hidden elementer */
let hiddenEl = document.querySelectorAll('.hidden');
hiddenEl.forEach((el) => observerer.observe(el));


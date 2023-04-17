let menuBtn = document.querySelector("#menu-btn")
let navLinks = document.querySelectorAll('.link')
let navbarEl = document.querySelector('.navbar')
let searchForm = document.querySelector(".search-form")

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


menuBtn.onclick = () =>{
    navbarEl.classList.toggle('active')
    searchForm.classList.remove("active")
    navSlide()
}


document.querySelector("#search-btn").onclick = () =>{
    searchForm.classList.toggle("active")
    navbarEl.classList.remove("active")
}

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

let hiddenEl = document.querySelectorAll('.hidden');
hiddenEl.forEach((el) => observerer.observe(el));
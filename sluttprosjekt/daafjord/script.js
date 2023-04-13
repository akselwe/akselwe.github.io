let menuBtn = document.querySelector("#menu-btn")
let navLinks = document.querySelectorAll('.link')
let navbarEl = document.querySelector('.navbar')

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

let searchForm = document.querySelector(".search-form")
document.querySelector("#search-btn").onclick = () =>{
    searchForm.classList.toggle("active")
    navbarEl.classList.remove("active")
}

window.onscroll = () => {
    navbarEl.classList.remove("active")
    searchForm.classList.remove("active")
}



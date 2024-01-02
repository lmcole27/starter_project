console.log("hello world")

/* */
const cContainer = document.querySelector(".container")



cContainer.addEventListener('mouseenter', () => {
    cContainer.classList.add('change')
})
cContainer.addEventListener('mouseleave', () => {
    cContainer.classList.remove('change')
})

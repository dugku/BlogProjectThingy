async function Likes(Likeys){
    let other = Likeys.getAttribute('data-id')

    await fetch(`http://127.0.0.1:8000/like/${other}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        }
    })

    var plusOne = Likeys.innerHTML
    plusOne = Number(plusOne) + 1
    Likeys.innerHTML = Number(plusOne)
}

async function Dislikes(Dislikesy){

    let other = Dislikesy.getAttribute('data-id')

    await fetch(`http://127.0.0.1:8000/dislike/${other}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        }
    })


    var plusOne = Dislikesy.innerHTML
    plusOne = Number(plusOne) + 1
    Dislikesy.innerHTML = Number(plusOne)
}

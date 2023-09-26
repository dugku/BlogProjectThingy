document.addEventListener("DOMContentLoaded", () => {

    var GetButton = document.getElementById("SubmitComment")
    var GetTextArea = document.getElementById("CommentArea")

    GetButton.addEventListener("click", () => {

        let CommentText = GetTextArea.value;
        
        const row = document.createElement("div")
        const col = document.createElement("div")
        const CommentTextPara = document.createElement("p")
        const likeButt = document.createElement("a")
        const DislikeButt = document.createElement("a")

        row.classList.add("row","d-flex")
        col.classList.add("col", "d-flex")

        CommentTextPara.classList.add("my-2")
        CommentTextPara.innerHTML = CommentText

        likeButt.classList.add("btn", "btn-primary", "mx-2")
        likeButt.addEventListener("click", () =>{
            console.log("Sweet")
        })

        DislikeButt.classList.add("btn", "btn-primary", "mx-2")
        DislikeButt.addEventListener("click", () => {
            console.log("Sweet")
        })

        const appendChildList = [
            CommentTextPara,
            likeButt,
            DislikeButt
        ]

        appendChildList.forEach((Dom) =>{
            col.appendChild(Dom)
        })

        const GetDiv = document.getElementById("Parnet");

        row.appendChild(col);
        GetDiv.appendChild(row);


    })

})
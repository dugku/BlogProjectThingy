var button = document.getElementById("GetThis");
var title = document.getElementById("title");
var author = document.getElementById("auth");
var postBody = document.getElementById("postBody");

button.addEventListener("click", async () => {
    sendPostInfo = {
        "Post": postBody.value,
        "Author": author.value,
        "Title": title.value
    }

    await fetch("http://127.0.0.1:8000/PostContent/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(sendPostInfo)
    })

    window.location.href = "http://127.0.0.1:8000/home/"
})


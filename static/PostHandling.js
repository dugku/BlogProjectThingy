document.addEventListener("DOMContentLoaded", () => {

   var button = document.getElementById("GetThis");
   var title = document.getElementById("title");
   var author = document.getElementById("auth");
   var postBody = document.getElementById("postBody");

    button.addEventListener("click", () => {
        sendPostInfo = {
            "title": title.value,
            "author": author.value,
            "post": postBody.value
        }

        console.log(sendPostInfo)
    })
})

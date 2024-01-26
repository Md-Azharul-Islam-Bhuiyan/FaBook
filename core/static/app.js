// let btn1 = document.querySelectorAll(".like-button");



// btn1.forEach(likeButton => {
//   likeButton.addEventListener('click', function () {
//     // console.log("toggled")
//     this.classList.toggle("active");
//   });
// });


// const commentFunc=(id)=>{
//     // console.log(id);
//     let element = document.getElementById(`comment_${id}`);
//     let comment_div = document.getElementById(`comment_div_${id}`)
//     // console.log(element);
//     // console.log(comment_div);
//     element.addEventListener('click',()=>{
//       comment_div.classList.remove("d-none")
//       comment_div.classList.add("d-block")
//     })
    
// }



// ********************News Feed********************


function togglePost(postId) {
    // Hide all posts
    var posts = document.querySelectorAll('.post');
    posts.forEach(function(post) {
        post.classList.remove('active');
    });

    // Show the clicked post
    var clickedPost = document.getElementById(postId);
    clickedPost.classList.add('active');
}


/************ toggle create post form************ */

document.addEventListener("DOMContentLoaded", function () {
    var formContainer = document.getElementById("postFormContainer");
    var toggleFormBtn = document.getElementById("toggleFormBtn");

    toggleFormBtn.addEventListener("click", function () {
        if (formContainer.style.display === "none" || formContainer.style.display === "") {
            formContainer.style.display = "block";
        } else {
            formContainer.style.display = "none";
        }
    });
});
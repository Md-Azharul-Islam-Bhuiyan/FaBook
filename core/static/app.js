let btn1 = document.querySelectorAll(".like-button");



btn1.forEach(likeButton => {
  likeButton.addEventListener('click', function () {
    // console.log("toggled")
    this.classList.toggle("active");
  });
});
// button.addEventListener("click", function(e) {
//   e.preventDefault();
//   this.classList.toggle("active");
//   this.classList.add("animated");
   
//   if (this.classList.contains("active")){
//     amount++;
//   }else{
//     amount--;
//   }
//   generateClones(this);
//   likes.innerHTML = amount
// });


// function generateClones(button) {
//   let clones = randomInt(2, 4);
//   for (let it = 1; it <= clones; it++) {
//     let clone = button.querySelector("svg").cloneNode(true),
//       size = randomInt(5, 16);
//     button.appendChild(clone);
//     clone.setAttribute("width", size);
//     clone.setAttribute("height", size);
//     clone.style.position = "absolute";
//     clone.style.transition =
//       "transform 0.5s cubic-bezier(0.12, 0.74, 0.58, 0.99) 0.3s, opacity 1s ease-out .5s";
//     let animTimeout = setTimeout(function() {
//       clearTimeout(animTimeout);
//       clone.style.transform =
//         "translate3d(" +
//         (plusOrMinus() * randomInt(10, 25)) +
//         "px," +
//         (plusOrMinus() * randomInt(10, 25)) +
//         "px,0)";
//       clone.style.opacity = 0;
//     }, 1);
//     let removeNodeTimeout = setTimeout(function() {
//       clone.parentNode.removeChild(clone);
//       clearTimeout(removeNodeTimeout);
//     }, 900);
//     let removeClassTimeout = setTimeout( function() {
//       button.classList.remove("animated")
//     }, 600);
//   }
// }


// function plusOrMinus() {
//   return Math.random() < 0.5 ? -1 : 1;
// }

// function randomInt(min, max) {
//   return Math.floor(Math.random() * (max - min + 1) + min);
// }


const commentFunc=(id)=>{
    // console.log(id);
    let element = document.getElementById(`comment_${id}`);
    let comment_div = document.getElementById(`comment_div_${id}`)
    // console.log(element);
    // console.log(comment_div);
    element.addEventListener('click',()=>{
      comment_div.classList.remove("d-none")
      comment_div.classList.add("d-block")
    })
    
}
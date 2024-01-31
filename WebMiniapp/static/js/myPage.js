const onDeleteButtonDown = (wishID) =>{
  const wish = document.querySelector("#" + wishID);
  let body = {
    id : wishID
  }
  fetch("http://127.0.0.1:8000/mypage/deleteWish", {
    method: "DELETE",
    headers:{
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body)
  })
  .then((res) =>{
    console.log(res)
    if(res.status == 200) wish.remove()
  })
}
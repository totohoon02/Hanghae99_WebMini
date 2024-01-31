const onBoardClick = (boardID) =>{
  console.log(boardID);
  fetch(`http://127.0.0.1:8000/mypage/${boardID}`, {
    method: "GET",
    headers:{
      "Content-Type": "application/json",
    },
  })
  .then((res) =>{
    if(res.status == 200)
      window.location.href = res.url
  })
}

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
    if(res.status == 200) wish.remove()
  })
}

const home = () => {window.location.href = "http://127.0.0.1:8000/"}
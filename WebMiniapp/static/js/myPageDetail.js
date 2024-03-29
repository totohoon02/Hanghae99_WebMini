const address = "http://sanghoonkang.pythonanywhere.com";
const home = () => {
  window.location.href = `${address}`;
};

$(document).ready(function () {
  // 모든 commentButton 요소에 클릭 이벤트 리스너 추가
  $(".commentButton").click(function () {
    let com = $("#com");

    if (com.val() != "") {
      // 클릭된 버튼의 데이터 가져오기
      var urlParts = window.location.href.split("/");
      var boardId = urlParts[urlParts.length - 1];
      var cookies = document.cookie;

      // 쿠키 문자열에서 ';'로 분리하여 배열로 만듦
      var cookieArray = cookies.split("; ");

      // user_id를 찾아서 처리
      var commentor = null;
      for (var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i];
        var [cookieKey, cookieValue] = cookie.split("=");
        if (cookieKey === "username") {
          commentor = cookieValue;
          break;
        }
      }

      // user_id가 없는 경우 또는 에러 처리
      if (commentor === null) {
        console.error("username 쿠키를 찾을 수 없습니다.");
        return;
      }

      // 입력 필드에서 코멘트 내용 가져오기
      var commentInput = $("#com").val();

      // 서버로 전송할 데이터 구성
      var data = {
        board_id: boardId,
        comment_id: commentor,
        comment_content: commentInput,
      };

      // Ajax를 사용하여 서버에 POST 요청 보내기
      $.ajax({
        url: "http://sanghoonkang.pythonanywhere.com/add_comment",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (response) {
          console.log("댓글 추가 성공");
          // 성공 시 적절한 처리 수행
          window.location.reload();
        },
        error: function (error) {
          console.error("댓글 추가 실패:", error);
        },
      });
    }
  });
});

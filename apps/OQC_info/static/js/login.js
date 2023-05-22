const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const firstForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container = document.querySelector(".container");

signInBtn.addEventListener("click", () => {
	container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
	container.classList.add("right-panel-active");
});

$(function () {
	// 页面框架加载完成之后代码自动执行
	firstFormEvent();
})

function firstFormEvent() {
	$("#btn_signin").click(function (){
		$.ajax({
			url: '/ajax/',
			type: 'post',
			data: $("#form1").serialize(),
			dataType: 'JSON',
			success: function (res){
				console.log(res);
				console.log(res.status);
				console.log(res.data);
			}
		})
	})
}

// firstForm.addEventListener("submit", function (e) {
// 	e.preventDefault();
//
// 	const form1_Data = new FormData(firstForm);
// 	// const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
//
// 	const xhr = new XMLHttpRequest();
// 	xhr.open("POST", "/login/");
// 	// xhr.setRequestHeader("X-CSRFToken", csrfToken)
//
// 	xhr.onload = function (){
// 		if (xhr.status === 200){
// 			const response = JSON.parse(xhr.responseText);
// 			if (response.success){
// 				window.location.href = "http://127.0.0.1:8000/home/";
// 			} else {
// 				alert(response.message);
// 			}
// 		}
// 	};
// 	xhr.send(form1_Data)
// });
//
// secondForm.addEventListener("submit", function (e) {
// 	e.preventDefault();
//
// 	const formData = new FormData(secondForm);
// 	// const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
//
// 	const xhr = new XMLHttpRequest();
// 	xhr.open("POST", "/register/");
// 	// xhr.setRequestHeader("X-CSRFToken", csrfToken)
//
// 	xhr.onload = function (){
// 		if (xhr.status === 200){
// 			const response = JSON.parse(xhr.responseText);
// 			if (response.success){
// 				alert(response.message);
// 				window.location.href = "http://127.0.0.1:8000/login/";
// 			} else {
// 				alert(response.message);
// 			}
// 		}
// 	};
// 	xhr.send(formData)
// });

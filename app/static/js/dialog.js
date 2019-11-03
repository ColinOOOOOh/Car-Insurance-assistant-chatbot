var object_content = document.getElementById("content");
var object_image = document.getElementById("Img");
var object_text = document.getElementById("txt");
var object_button = document.getElementById("btn");
var object_show_text = document.getElementById("showTxt");
var object_save = document.getElementById("save");

angular.module('dialog', [])
    .controller('dialog_controller', function ($scope, $http) {

    //Send message and get instant response.
    $scope.send_msg = function () {
        var new_li = document.createElement("li");
        var new_image = document.createElement('img');
        var request_data = $scope.requestMsg;
        var data = {
            "message": request_data
        };

        if(request_data != ""){
            new_li.innerHTML = request_data;
            new_li.className = 'showTxt right';
            object_save.appendChild(new_li);
            $scope.requestMsg = "";

            new_image.src = "picture/me.PNG";
            new_image.className = "showImg rightImg";
            new_li.appendChild(new_image);

            var div = document.createElement("div");
            div.style = 'clear:both';
            object_save.appendChild(div);

            $http({
                method: 'POST',
                url: 'https://fba5b7a2-2283-4909-a637-6facc546d041.mock.pstmn.io/send_msg',
                data: data
            }).then(function (response) {
                var res_data = response.data.response;
                response_by_chatbot(res_data);
            });
        }
    }
});

//Response by chatbot automatically.
function response_by_chatbot(message){
    var new_li = document.createElement("li");
    var new_image = document.createElement('img');

    new_li.innerHTML = message;
    new_li.className = 'showTxt left';
    object_save.appendChild(new_li);
    object_text.value = "";

    // new_image.src = object_image.src;
    new_image.src = "picture/chatbot.jpg";
    new_image.className = "showImg leftImg";
    new_li.appendChild(new_image);

    var div = document.createElement("div");
    div.style = 'clear:both';
    object_save.appendChild(div);
}
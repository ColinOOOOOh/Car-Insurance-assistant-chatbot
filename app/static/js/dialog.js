var object_text = document.getElementById("txt");
var object_save = document.getElementById("save");
var userid = document.getElementById("userid").value;

angular.module('dialog', [])
    .controller('dialog_controller', function ($scope, $http) {
    //Send message by press enter.
    $scope.send_msg_key = function(){
        $scope.send_msg();
    };

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

            new_image.src = "static/picture/zhihu.jpg";
            new_image.className = "showImg rightImg";
            new_li.appendChild(new_image);

            var div = document.createElement("div");
            div.style = 'clear:both';
            object_save.appendChild(div);
            document.getElementById('content').scrollTop = document.getElementById('content').scrollHeight;

            $http({
                method: 'POST',
                url: 'answer_question',
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

    new_li.innerHTML = enterMsg(message);
    new_li.className = 'showTxt left';
    object_save.appendChild(new_li);
    object_text.value = "";

    // new_image.src = object_image.src;
    new_image.src = "static/picture/chatbot.jpg";
    new_image.className = "showImg leftImg";
    new_li.appendChild(new_image);

    var div = document.createElement("div");
    div.style = 'clear:both';
    object_save.appendChild(div);
    document.getElementById('content').scrollTop = document.getElementById('content').scrollHeight;
}

function enterMsg(msg) {
    var new_msg = msg.replace(new RegExp(/\*/g), '</br>');
    return new_msg;
}
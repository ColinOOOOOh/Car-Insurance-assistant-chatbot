var flag1 = true;
var flag2 = true;

angular.module('profile', [])
    .controller('profile_controller', function ($scope, $http){
    $scope.change_icon = function () {
        document.getElementById('icon').style.display = "none";
        document.getElementById('make').style.display = "block";
        document.getElementById('icon_frame').style.display = "block";
    };

    //Change icon.
    $scope.change = function () {
        var icon = document.getElementById('icon');
        alert(document.getElementById('icon_frame').value);
        icon.src = document.getElementById('icon_frame').value;
        document.getElementById('icon').style.display = "block";
        document.getElementById('make').style.display = "none";
        document.getElementById('icon_frame').style.display = "none";

    };

    //Email format is valid or not.
    $scope.email_valid = function(){
        $http({
            method: 'GET',
            url: 'https://ac785e2a-c9be-488e-aee3-aa2cb088bf8a.mock.pstmn.io/email_valid'
        }).then(function (response) {
            var res_data = response.data.result;
            var email_check = document.getElementById('valid_email');
            if(res_data != 'yes'){
                email_check.style.display = "block";
                flag1 = false;
            }else{
                email_check.style.display = "none";
                flag1 = true;
            }
        })
    };

    //Mobile number is valid or not.
    $scope.mobilenumber_valid = function(){
        $http({
            method: 'GET',
            url: 'https://e9da2167-a5c2-4a83-9982-614edcd65d99.mock.pstmn.io/mobilenumber_valid'
        }).then(function (response) {
            var res_data = response.data.result;
            var mobilenumber_check = document.getElementById('valid_mobilenumber');
            if(res_data != 'yes'){
                mobilenumber_check.style.display = "block";
                flag2 = false;
            }else{
                mobilenumber_check.style.display = "none";
                flag2 = true;
            }
        });
    };
    
    //Reset function.
    $scope.reset = function () {
        $scope.email = "";
        $scope.mobilenumber = "";
        $scope.gender = "";
        $scope.birthday = "";
        $scope.username = "";
    }
    
    //Edit function.
    $scope.edit = function () {
        var edit_valid_block = document.getElementById('edit_valid_div');
        if(!flag1 || !flag2){
            edit_valid_block.style.display = "block";
            return;
        }else{
            edit_valid_block.style.display = "none";
        }
    };

    //Transfer to original page.
    $scope.transfer = function(){
        window.location.href = 'Management.html'
    }
});
var flag1 = true;
var flag2 = true;

angular.module('profile', [])
    .controller('profile_controller', function ($scope, $http, $window){

    //Initializing
    $window.onload = function(){
        $http({
            method: 'POST',
            url: 'profile'
        }).then(function (response) {
            $scope.username = response.data.username;
            $scope.email = response.data.email;
            var str = response.data.birthday.replace(/-/g, "/");
            var date = new Date(str)
            $scope.birthday = date;
            $scope.mobilenumber = response.data.telephone;
            var sex = response.data.gender;
            if(sex == "1"){
                $scope.gender = "1";
            }else{
                $scope.gender = "2"
            }
        });
     };

    //Email format is valid or not.
    $scope.email_valid = function(){
        $http({
            method: 'GET',
            url: 'email_exit?email='+email
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
            url: 'check_telephone_number?mobile_number='+mobilenumber
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
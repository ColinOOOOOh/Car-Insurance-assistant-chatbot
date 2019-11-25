var flag1 = true;
var flag2 = true;
var flag3 = true;
var flag4 = true;
//var age = 0;

angular.module('register', [])
    .controller('register_controller', function ($scope, $http) {
    //Username is valid or not.
    $scope.username_exist = function(){
        var username = $scope.username;
        $http({
            method: 'GET',
            url: 'username_exist?username=' +　username
        }).then(function (response) {
            var res_data = response.data.result;
            var username_check = document.getElementById('valid_username');
            if(res_data != 'yes'){
                username_check.style.display = "block";
                flag1 = false;
            }else{
                username_check.style.display = "none";
                flag1 = true;
            }
        });
    };

    //Email format is valid or not.
    $scope.email_valid = function(){
        var email = $scope.email;
        $http({
            method: 'GET',
            url: 'email_exit?email=' + email
        }).then(function (response) {
            var res_data = response.data.result;
            var email_check = document.getElementById('valid_email');
            if(res_data != 'yes'){
                email_check.style.display = "block";
                flag2 = false;
            }else{
                email_check.style.display = "none";
                flag2 = true;
            }
        });
    };

    //Mobile number is valid or not.
    $scope.mobilenumber_valid = function(){
        var mobilenumber = $scope.mobilenumber;
        $http({
            method: 'GET',
            url: 'check_telephone_number?mobile_number='+mobilenumber
        }).then(function (response) {
            var res_data = response.data.result;
            var mobilenumber_check = document.getElementById('valid_mobilenumber');
            if(res_data != 'yes'){
                mobilenumber_check.style.display = "block";
                flag3 = false;
            }else{
                mobilenumber_check.style.display = "none";
                flag3 = true;
            }
        });
    };

    //Confirm password is consistent with password or not.
    $scope.consistent = function(){
        var one_pass = $scope.password;
        var two_pass = $scope.confirm;
        var pass_block = document.getElementById('consistency');
        if(one_pass != null && one_pass != two_pass){
            pass_block.style.display = "block";
            flag4 = false;
        }else{
            pass_block.style.display = "none";
            flag4 = true;
        }
    };

    //Calculate Age.
    $scope.calculateAge = function(){
        var birth = $scope.birthday;
        var birthDayTime = new Date(birth).getTime();
        var nowTime = new Date().getTime();
        var age = Math.ceil((nowTime-birthDayTime)/31536000000);

        document.getElementsByName("age").val = age;

        $scope.age = age;
        document.getElementById("age").value = age;

    };

    //Register function
    $scope.register = function(){
        var gender = $scope.gender;
        var register_valid_block = document.getElementById('register_valid_div');
        if(!flag1 || !flag2 || !flag3 || !flag4){
            register_valid_block.style.display = "block";
            return;
        }else{
            register_valid_block.style.display = "none";
        }
    };

    //Reset all the properties.
    $scope.reset = function () {
      $scope.username = "";
      $scope.email = "";
      $scope.mobilenumber = "";
      $scope.role = "";
      $scope.gender = "";
      $scope.birthday = "";
      $scope.password = "";
      $scope.confirm = "";
      $scope.occupation = "";
      $scope.car_model = "";
      $scope.previous_accidents = "";
    };

    $scope.return = function () {
        window.location.href = 'Login.html'
    }
});
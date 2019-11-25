function jumpToRegister(){
    window.location.href = "Register.html";
}

//Jump to Register page
angular.module('loginApp', []).controller('login_controller', function ($scope, $location) {
    $scope.reset = function(){
        $scope.username = "";
        $scope.password = "";
    };
});
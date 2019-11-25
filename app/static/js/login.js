var app = angular.module('loginApp', []);

function jumpToRegister(){
    window.location.href = "Register.html";
}

//Jump to Register page
app.controller('login_controller', function ($scope, $location) {
    $scope.reset = function(){
        $scope.username = "";
        $scope.password = "";
    };
});
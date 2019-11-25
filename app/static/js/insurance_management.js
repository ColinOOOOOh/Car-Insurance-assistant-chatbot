var main = document.getElementById('popover');
var userid = document.getElementById('userid').value;

angular.module('insurance_management', [])
    .controller('insurance_management_controller', function ($scope, $http, $window) {
        //Insurance information
        $scope.insurance_info = [];

        //Onload function.
        $window.onload = function(){
            var data = {"userid": userid};
            $http({
                method: 'POST',
                url: 'insurance_m',
                data: data
            }).then(function (response) {
                $scope.insurance_info = response.data.result;
            });
        };

        //Transfer to chatbot.
        $scope.to_chatbot = function(){
            window.location = "Main.html";
        };
    });
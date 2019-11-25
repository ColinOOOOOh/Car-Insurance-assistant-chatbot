var app = angular.module('insurance', []);

app.controller('insurance_controller', function ($scope, $http) {
    $http({
        method: 'GET',
        url: 'get_insurance'
    }).then(function (response) {
        var res_data = response.data.insurance_type;
        $scope.insurnace_types = res_data;
    });
});
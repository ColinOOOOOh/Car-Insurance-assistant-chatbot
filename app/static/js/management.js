var popup = document.getElementById('popup');
var main = document.getElementById('popover');
var insurance_bar = document.getElementById('insurance_bar');
var edit_button = document.getElementById('multi_btn');
var userid = document.getElementById('userid').value;

function show() {
    popup.style.display = "block";
    document.body.style.backgroundColor = "silver";
    document.getElementById('multi_btn').type = "button";
    document.getElementById('edit_btn').style.display = "none";
    edit_button.style.display = "block";
    insurance_bar.innerText = "Add Insurance";
    edit_button.value = "Add";
}

function cancel() {
    popup.style.display = "none";
    document.body.style.backgroundColor = "white";
}

angular.module('management', [])
    .controller('management_controller', function ($scope, $http, $window){
        //Insurance information
        $scope.insurance_info = [];

        //Onload function.
        $window.onload = function(){
            var data = {"userid": userid};
            $http({
                method: 'POST',
                url: 'get_management_info',
                data: data
            }).then(function (response) {
                $scope.insurance_info = response.data.result;
            });
        };

        //Transfer to chatbot.
        $scope.to_chatbot = function(){
            window.location = "Main.html";
        };

        //Add information.
        $scope.add_info = function ($index) {
            var insurance_name = $scope.insurance_name;
            var company = $scope.company;
            var business_name = $scope.business_name;
            var insurance_description = $scope.insurance_description;
            var business_description = $scope.business_description;
            var value = document.getElementById('multi_btn').value;

            //Clear contents
            $scope.insurance_name = "";
            $scope.company = "";
            $scope.business_name = "";
            $scope.insurance_description = "";
            $scope.business_description = "";

            var data = {
                "insurance_name": insurance_name,
                "company": company,
                "business_name": business_name,
                "insurance_description": insurance_description,
                "business_description": business_description
            };

            $http({
                method: "POST",
                url: "https://85b9afbf-b08a-4417-9ea8-06bc7a4e157b.mock.pstmn.io/add_insurance",
                data: data
            }).then(function (response) {
                var res_data = response.data.result;
                if(res_data == 'yes'){
                    alert("Ok");
                    $scope.insurance_id = response.data.insurance_id;
                    data["insurance_id"] = $scope.insurance_id;
                    $scope.insurance_info.push(data);
                    cancel();
                }else{
                    alert("No");
                }
            });
        };

        //Edit page.
        $scope.edit = function($index){
            document.getElementById('edit_btn').style.display = "block";
            document.getElementById('multi_btn').type = "hidden";
            popup.style.display = "block";
            // edit_button.value = "Edit";
            insurance_bar.innerText = "Edit Insurance";

            //Retrieve the value.
            var value = $scope.insurance_info[$index];
            $scope.insurance_index = $index;
            $scope.insurance_id = value.insurance_id;
            $scope.insurance_name = value.insurance_name;
            $scope.company = value.company;
            $scope.business_name = value.business_name;
            $scope.insurance_description = value.insurance_description;
            $scope.business_description = value.business_description;
        };

        //Edit insurance information.
        $scope.edit_info = function () {
            var index = $scope.insurance_index;
            var insurance_id = $scope.insurance_id;
            var insurance_name = $scope.insurance_name;
            var company = $scope.company;
            var business_name = $scope.business_name;
            var insurance_description = $scope.insurance_description;
            var business_description = $scope.business_description;
            //var value = document.getElementById('multi_btn').value;

            //Clear contents
            $scope.insurance_name = "";
            $scope.company = "";
            $scope.business_name = "";
            $scope.insurance_description = "";
            $scope.business_description = "";

            var data = {
                "insurance_id": insurance_id,
                "insurance_name": insurance_name,
                "company": company,
                "business_name": business_name,
                "insurance_description": insurance_description,
                "business_description": business_description
            };

            $http({
                method: "POST",
                url: "https://6c2d41b5-6589-49f7-827b-ddab1702c2ca.mock.pstmn.io/edit_insurance",
                data: data
            }).then(function (response) {
                var res_data = response.data.result;
                if(res_data == 'yes'){
                    $scope.insurance_info[index] = data;
                    cancel();
                    alert("Ok");
                }else{
                    alert("No");
                }
            });
        };

        //Delete insurance information.
        $scope.delete = function($index){
            var insurance_id = $scope.insurance_info[$index].insurance_id;
            var data = {
                "insurance_id": insurance_id
            };
            $http({
                method: "DELETE",
                url: "https://320ace37-48b8-480a-aef2-0d1ea71f5f40.mock.pstmn.io/remove_insurance_info",
                data: data,
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function (response) {
                var res_data = response.data.result;
                if(res_data == 'yes'){
                    alert("Ok");
                    $scope.insurance_info.splice($index, 1);
                    cancel();
                }else{
                    alert("No");
                }
            });
        };
        
        //Transfer to profile page.
        $scope.to_profile = function () {
            window.location.href = 'Profile.html'
        };
        
        //Sign out.
        $scope.sign_out = function () {
            window.location.href = 'Login.html'
        }
});
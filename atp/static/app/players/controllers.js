(function () {
    'use strict';

    angular.module('atp')
        .controller('playersCtrl', PlayersCtrl);

    PlayersCtrl.$inject = ['$scope', '$http'];

    function PlayersCtrl($scope, $http) {
        $http.get('api/players')
            .success(function (data, status) {
                var response = angular.fromJson(data);
                $scope.players = response['objects'];
            })
            .error(function (data, status) {
            });
    }
})();

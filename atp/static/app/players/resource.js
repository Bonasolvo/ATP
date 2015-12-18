(function () {
    'use strict';

    angular.module('atp')
        .factory('Players', Players);

    Players.$inject = ['$resource'];

    function Players($resource) {
        return $resource('/api/players/:id', {id: '@id'}, {
            query: {
                method: 'GET',
                isArray: true,
                ignoreLoadingBar: true
            }
        });
    }
})();
(function () {
    'use strict';

    angular.module('atp', [
        'ui.router',
        'angular-loading-bar',
        'ngAnimate',


        //foundation
        'foundation',
        'foundation.modal',
        'foundation.dynamicRouting',
        'foundation.dynamicRouting.animations'
    ])
        .config(config)
        .run(run)
    ;

    config.$inject = ['$urlRouterProvider', '$locationProvider'];

    function config($urlProvider, $locationProvider) {
        $urlProvider.otherwise('/');

        $locationProvider.html5Mode({
            enabled: false,
            requireBase: false
        });

        $locationProvider.hashPrefix('!');
    }


    function run() {
        FastClick.attach(document.body);
    }

})();

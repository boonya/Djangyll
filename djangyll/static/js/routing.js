'use strict';

locoMoco.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.
            when('/apps/', {
                templateUrl: 'html/app/list.html',
                controller: 'ApplicationListController'
            }).
            when('/apps/:id', {
                templateUrl: 'html/app/view.html',
                controller: 'ApplicationController'
            }).
            when('/apps/:id/participants', {
                templateUrl: 'html/app/participants.html',
                controller: 'ApplicationParticipantsController'
            }).
            otherwise({
                redirectTo: '/apps/'
            });
    }
]);

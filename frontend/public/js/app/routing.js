'use strict';

Djangyll.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.
            when('/post-list/', {
                templateUrl: 'html/post/list.html',
                controller: 'PostListController'
            }).
            when('/post/:id', {
                templateUrl: 'html/post/edit.html',
                controller: 'PostEditController'
            }).
            otherwise({
                redirectTo: '/post-list/'
            });
    }
]);

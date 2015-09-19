'use strict';

Djangyll.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.
            when('/post-list/', {
                templateUrl: 'html/post/list.html',
                controller: 'PostListController'
            }).
            when('/post/:id', {
                templateUrl: 'html/post/view.html',
                controller: 'PostController'
            }).
            otherwise({
                redirectTo: '/post-list/'
            });
    }
]);

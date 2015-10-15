'use strict';

var appName = 'Djangyll';

var Controllers = angular.module(appName + '.controllers', []);
var Services = angular.module(appName + '.services', []);
var Directives = angular.module(appName + '.directives', []);
var Filters = angular.module(appName + '.filters', []);

// Declare app level module which depends on controllers, services and directives modules
var Djangyll = angular.module(appName,
    [
        appName + '.services',
        appName + '.directives',
        appName + '.controllers',
        appName + '.filters',
        'ngRoute',
        'ngCookies',
        'ngResource',
        'textAngular'
    ]
);

Djangyll.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

Djangyll.config(['$resourceProvider', function ($resourceProvider) {
    // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $resourceProvider.defaults.actions['update'] = {method: 'PUT'};
}]);

Djangyll.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
});

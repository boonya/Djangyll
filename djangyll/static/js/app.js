'use strict';

var appName = 'locoMoco';

var locoMocoControllers = angular.module(appName + '.controllers', []);
var locoMocoServices = angular.module(appName + '.services', []);
var locoMocoDirectives = angular.module(appName + '.directives', []);
var locoMocoFilters = angular.module(appName + '.filters', []);

// Declare app level module which depends on controllers, services and directives modules
var locoMoco = angular.module(appName,
    [
        appName + '.services',
        appName + '.directives',
        appName + '.controllers',
        appName + '.filters',
        'ngRoute',
        'ngCookies',
        'ngResource',
        'ngAnimate',
        'ui.bootstrap',
        'ui.select'
    ]
);

locoMoco.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

locoMoco.config(['$resourceProvider', function ($resourceProvider) {
    // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $resourceProvider.defaults.actions['update'] = {method: 'PUT'};
}]);

locoMoco.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

locoMoco.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
});

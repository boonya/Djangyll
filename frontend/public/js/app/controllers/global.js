'use strict';

var GlobalController = function ($scope, $rootScope) {
    $scope.globalPreloader = false;

    $rootScope.$on('globalPreloader:show', function () {
        $scope.globalPreloader = true;
    });

    $rootScope.$on('globalPreloader:hide', function () {
        $scope.globalPreloader = false;
    });
};

GlobalController.$inject = ['$scope', '$rootScope'];

Controllers.controller('GlobalController', GlobalController);

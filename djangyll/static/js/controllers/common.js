'use strict';

var CommonController = function ($scope, $rootScope) {
    $scope.globalPreloader = false;

    $rootScope.$on('globalPreloader:show', function () {
        $scope.globalPreloader = true;
    });

    $rootScope.$on('globalPreloader:hide', function () {
        $scope.globalPreloader = false;
    });
};

CommonController.$inject = ['$scope', '$rootScope'];

locoMocoControllers.controller('CommonController', CommonController);

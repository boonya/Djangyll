'use strict';

var ApplicationParticipantsController = function ($scope, $rootScope, $routeParams, ApiCore, Application) {

    $scope.appId = parseInt($routeParams.id, 10);

    $scope.application = {};

    $scope.participants = [];

    /**
     * Initialization of all needed data.
     */
    $scope.init = function () {
        $rootScope.$broadcast('globalPreloader:show');
        $scope.getApplication()
            .then(function () {
                $scope.getParticipants();
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $rootScope.$broadcast('globalPreloader:hide');
            });
    };

    /**
     * Get current application.
     *
     * @return  {promise}
     */
    $scope.getApplication = function () {
        return Application.get($scope.appId)
            .then(function (data) {
                $scope.application = data;
            })
            .catch(ApiCore.throwApiError);
    };

    /**
     * Get listing of application's participants.
     *
     * @returns {promise}
     */
    $scope.getParticipants = function () {
        return Application.participants($scope.application.id, $scope.application.participants)
            .then(function (data) {
                $scope.participants = data;
            })
            .catch(ApiCore.throwApiError);
    };

};

ApplicationParticipantsController.$inject = ['$scope', '$rootScope', '$routeParams', 'ApiCore', 'Application'];

locoMocoControllers.controller('ApplicationParticipantsController', ApplicationParticipantsController);

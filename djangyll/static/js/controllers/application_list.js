'use strict';

var ApplicationListController = function ($scope, $rootScope, ApiCore, Application, Language) {

    $scope.loaded = false;

    /**
     * List of all available applications.
     *
     * @type {Array}
     */
    $scope.applications = [];

    /**
     * Application's data which should be saved.
     *
     * @type {{}}
     */
    $scope.application = {};

    /**
     * List of all available localizations.
     *
     * @type {Array}
     */
    $scope.languages = [];

    /**
     * Creation form controller.
     *
     * @type {FormController}
     */
    $scope.createForm = {};

    /**
     * Whether to show the form for creating applications.
     *
     * @type {boolean}
     */
    $scope.showCreateForm = false;

    /**
     * Get list of all available applications.
     */
    $scope.list = function () {
        $scope.loaded = false;
        Application.list()
            .then(function (data) {
                $scope.applications = data;
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $scope.loaded = true;
            }
        );
    };

    /**
     * Try to create a new application.
     */
    $scope.create = function () {
        var languages = [];
        for (var i = 0; i < $scope.languages.length; i++) {
            if ($scope.languages[i].name != $scope.application.language) continue;
            languages.push($scope.languages[i].id);
            break;
        }
        Application.create($scope.application.name, languages)
            .then(function (data) {
                $scope.showCreateForm = false;
                $scope.applications.push(data);
            })
            .catch(ApiCore.throwApiError);
    };

    /**
     * Clears the creation form.
     */
    $scope.clearCreateForm = function () {
        $scope.application = {};
        $scope.createForm.$setPristine();
    };

    $scope.$watch('showCreateForm', function (value) {
        if (!value) $scope.clearCreateForm();
        if (!value || 0 < $scope.languages.length) return;
        Language.list()
            .then(function (data) {
                $scope.languages = data;
            }).catch(function (error) {
                ApiCore.throwApiError(error);
            }
        );
    });

    $scope.$watch('loaded', function (loaded) {
        if (!loaded) $rootScope.$broadcast('globalPreloader:show');
        else $rootScope.$broadcast('globalPreloader:hide');
    });
};

ApplicationListController.$inject = ['$scope', '$rootScope', 'ApiCore', 'Application', 'Language'];

locoMocoControllers.controller('ApplicationListController', ApplicationListController);

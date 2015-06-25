'use strict';

var SingleApplicationController = function ($scope, $routeParams, ApiCore, Application, Language, Text) {

    $scope.loaded = false;

    /**
     * Application's data which should be saved.
     *
     * @type {{}}
     */
    $scope.application = {};

    $scope.application_id = parseInt($routeParams.application_id, 10);
    $scope.language_id = null;

    /**
     * List of all available localizations.
     *
     * @type {Array}
     */
    $scope.localizations = [];

    /**
     * List of all available texts.
     *
     * @type {Array}
     */
    $scope.texts = [];

    /**
     * Get an application.
     *
     * @param {int} application_id
     */
    $scope.get = function (application_id) {
        $scope.loaded = false;
        Application.get(application_id)
            .then(function (data) {
                $scope.application = data;
            }).catch(function (error) {
                ApiCore.throwApiError(error);
            }).finally(function() {
                $scope.loaded = true;
            }
        );
    };

    /**
     * Get texts for application.
     */
    $scope.get_texts = function (application_id, language_id) {
        language_id = language_id || null;
        $scope.loaded = false;
        Text.list(application_id, language_id)
            .then(function (data) {
                $scope.texts = data;
            }).catch(function (error) {
                ApiCore.throwApiError(error);
            }).finally(function() {
                $scope.loaded = true;
            }
        );
    };

    /**
     * Create new texts for application.
     */
    $scope.create_texts = function (entries) {
        $scope.loaded = false;
        Text.create(entries)
            .then(function (data) {
                $scope.texts = [].concat($scope.texts, data.items);
            }).catch(function (error) {
                ApiCore.throwApiError(error);
            }).finally(function() {
                $scope.loaded = true;
            }
        );
    };

    /**
     * Update existing texts for application.
     */
    $scope.update_texts = function (entries) {
        $scope.loaded = false;
        Text.update(entries)
            .then(function (data) {
                // TODO: update existing entries
                console.log(data);
            }).catch(function (error) {
                ApiCore.throwApiError(error);
            }).finally(function() {
                $scope.loaded = true;
            }
        );
    };

    /**
     * Remove given texts from application.
     */
    $scope.remove_texts = function (entries) {
        $scope.loaded = false;
        Text.remove(entries)
            .then(function (data) {
                // TODO: remove deleted items from texts array.
            }).catch(function (error) {
                ApiCore.throwApiError(error);
            }).finally(function() {
                $scope.loaded = true;
            }
        );
    };

    /**
     * Init current view.
     * [DEMO]
     */
    $scope.get($scope.application_id);

    $scope.get_texts($scope.application_id, $scope.language_id);

    var new_texts = [
        {
            application: $scope.application_id,
            language: 1,
            key: 'key_tmp1',
            value: 'value_tmp1',
            comment: 'comment_tmp1'
        },
        {
            application: $scope.application_id,
            language: 1,
            key: 'key_tmp2',
            value: 'value_tmp2',
            comment: 'comment_tmp2'
        }
    ];
    $scope.create_texts(new_texts);

    var random_number = 42;
    var update_texts = [
        {
            id: 38,
            application: $scope.appId,
            language: 1,
            key: 'key_tmp1---v' + random_number,
            value: 'value_tmp1---v' + random_number,
            comment: 'comment_tmp1---v' + random_number
        },
        {
            id: 39,
            application: $scope.appId,
            language: 1,
            key: 'key_tmp2---v' + random_number,
            value: 'value_tmp2---v' + random_number,
            comment: 'comment_tmp2---v' + random_number
        }
    ];
    $scope.update_texts(update_texts);

    var remove_texts = [30, 31, 32];
    $scope.remove_texts(remove_texts);

};

SingleApplicationController.$inject = ['$scope', '$routeParams', 'ApiCore', 'Application', 'Language', 'Text'];

locoMocoControllers.controller('SingleApplicationController', SingleApplicationController);

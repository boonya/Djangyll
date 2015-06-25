'use strict';

var ApplicationController = function ($scope, $rootScope, $routeParams, ApiCore, Application, Language, Screen, Text) {

    $scope.loaded = false;

    $scope.appForm = null;

    $scope.appNameEditMode = false;

    $scope.appId = parseInt($routeParams.id, 10);

    $scope.application = {};

    $scope.languages = [];
    $scope.availableLanguages = [];

    $scope.texts = [];
    $scope.modifiedTexts = [];
    $scope.originalTexts = [];

    $scope.availableScreens = [];

    /**
     * Initialization of all needed data.
     */
    $scope.init = function () {
        $scope.loaded = false;
        $rootScope.$broadcast('globalPreloader:show');
        $scope.getApplication()
            .then(function () {
                $scope.getAvailableLanguages();
                $scope.getAvailableScreens();
                $scope.getLanguages();
                $scope.getTexts();
                $scope.loaded = true;
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
     * Get all available languages.
     *
     * @return  {promise}
     */
    $scope.getAvailableLanguages = function () {
        return Language.list()
            .then(function (data) {
                $scope.availableLanguages = data;
            })
            .catch(ApiCore.throwApiError);
    };

    /**
     * Get languages of application.
     *
     * @return  {promise}
     */
    $scope.getLanguages = function () {
        return Application.languages($scope.application.id, $scope.application.languages)
            .then(function (data) {
                $scope.languages = data;
            })
            .catch(ApiCore.throwApiError);
    };

    $scope.getAvailableScreens = function () {
        return Screen.list($scope.appId)
            .then(function (data) {
                $scope.availableScreens = data;
            })
            .catch(ApiCore.throwApiError);
    };

    /**
     * Get texts for application.
     *
     * @return  {promise}
     */
    $scope.getTexts = function () {
        return Text.list($scope.appId)
            .then(function (data) {
                $scope.modifiedTexts = [];
                $scope.originalTexts = data;
                $scope.texts = angular.copy($scope.originalTexts);
            })
            .catch(ApiCore.throwApiError);
    };

    /**
     * Create texts for application.
     *
     * @return  {promise}
     */
    $scope.createTexts = function () {
        // mock data
        var entries = [
            {
                key: 'view_profile',
                comment: 'Lorem Ipsum',
                values: {
                    'en_GB': 'view profile',
                    'fr_FR': 'voir le profil'
                }
            },
            {
                key: 'view_account',
                comment: 'Lorem Ipsum',
                values: {
                    'en_GB': 'view account',
                    'fr_FR': 'vue compte'
                }
            }
        ];

        return Text.create($scope.appId, entries)
            .then(function (data) {
                $scope.originalTexts = [].concat($scope.originalTexts, data.items);
                $scope.texts = angular.copy($scope.originalTexts);
            })
            .catch(ApiCore.throwApiError);
    };

    $scope.toggleAppNameEditMode = function () {
        $scope.appNameEditMode = ($scope.appNameEditMode) ? false : true;
        $scope.appForm.name.value = $scope.application.name;
    };

    $scope.saveName = function () {
        Application.update($scope.appId, {name: $scope.appForm.name.value})
            .then(function (data) {
                $scope.application = data;
                $scope.appNameEditMode = false;
            })
            .catch(ApiCore.throwApiError);
    };

    $scope.addLanguage = function (language) {
        var languages = [];
        for (var i = 0; i < $scope.languages.length; i++) {
            languages.push($scope.languages[i].id);
        }
        for (var i = 0; i < $scope.availableLanguages.length; i++) {
            if (language != $scope.availableLanguages[i].name) continue;
            languages.push($scope.availableLanguages[i].id);
            break;
        }
        $rootScope.$broadcast('globalPreloader:show');
        Application.update($scope.appId, {languages: languages})
            .then(function (data) {
                $scope.application = data;
                $scope.getLanguages();
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $rootScope.$broadcast('globalPreloader:hide');
            });
    };

    $scope.removeLanguage = function (language) {
        if (!confirm('Do you really want to delete this language?')) return;
        var languages = [];
        for (var i = 0; i < $scope.languages.length; i++) {
            if (language == $scope.languages[i].name) {
                var index = i;
                continue;
            }
            languages.push($scope.languages[i].id);
        }
        $rootScope.$broadcast('globalPreloader:show');
        Application.update($scope.appId, {languages: languages})
            .then(function (data) {
                $scope.application = data;
                $scope.getLanguages();
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $rootScope.$broadcast('globalPreloader:hide');
            });
    };

    $scope.setScreens = function (id, screens) {
        var length = $scope.modifiedTexts.length;
        for (var i = 0; i < length; i++) {
            if ($scope.modifiedTexts[i].id != id) continue;

            $scope.modifiedTexts[i]['screens'] = screens;

            break;
        }

        if (!length || i >= length) {
            $scope.modifiedTexts.push({
                id: id,
                screens: screens
            });
        }
    };

    /**
     * Set new value into modifiedTexts collection.
     *
     * @param id
     * @param language
     * @param text
     */
    $scope.setText = function (id, language, text) {
        var length = $scope.modifiedTexts.length;
        for (var i = 0; i < length; i++) {
            if ($scope.modifiedTexts[i].id != id) continue;

            $scope.modifiedTexts[i]['values'] = $scope.modifiedTexts[i]['values']
                ? $scope.modifiedTexts[i]['values']
                : {};
            $scope.modifiedTexts[i]['values'][language] = text;

            break;
        }

        if (!length || i >= length) {
            var data = {
                id: id,
                values: {}
            };
            data['values'][language] = text;
            $scope.modifiedTexts.push(data);
        }
    };

    /**
     * Rollback original value & remove it from modifiedTexts collection.
     *
     * @param id
     * @param language
     */
    $scope.rollbackText = function (id, language) {
        var length = $scope.modifiedTexts.length;
        for (var i = 0; i < length; i++) {
            if ($scope.modifiedTexts[i].id != id) continue;

            for (var j = 0; j < $scope.originalTexts.length; j++) {
                if (!$scope.originalTexts[j].id == id) continue;

                if (angular.isObject($scope.originalTexts[j]['values'])) {
                    delete $scope.modifiedTexts[i]['values'][language];
                    if (!Object.keys($scope.modifiedTexts[i]['values']).length) {
                        delete $scope.modifiedTexts[i]['values'];
                    }
                }

                return;
            }
        }
    };

    /**
     * Discard all changes which made with texts or screens.
     */
    $scope.resetTexts = function () {
        if (!confirm('Do you really want to delete all your modifications?')) return;
        $scope.modifiedTexts = [];
        $scope.texts = angular.copy($scope.originalTexts);
    };

    /**
     * Save all changes.
     */
    $scope.saveTexts = function () {
        if (!confirm('Do you really want to save all your modifications?')) return;
        $rootScope.$broadcast('globalPreloader:show');
        Text.update($scope.appId, $scope.modifiedTexts)
            .then(function () {
                $scope.getTexts();
            })
            .catch(ApiCore.throwApiError)
            .finally(function () {
                $rootScope.$broadcast('globalPreloader:hide');
            });
    };

    /**
     * Checks whether the text changes.
     *
     * @returns {boolean}
     */
    $scope.textsChanged = function () {
        var length = $scope.modifiedTexts.length;
        if (!length) return false;

        for (var i = 0; i < length; i++) {
            if (1 < Object.keys($scope.modifiedTexts[i]).length) return true;
        }

        $scope.modifiedTexts = [];
        return false;
    };

};

ApplicationController.$inject = ['$scope', '$rootScope', '$routeParams', 'ApiCore', 'Application',
    'Language', 'Screen', 'Text'];

locoMocoControllers.controller('ApplicationController', ApplicationController);

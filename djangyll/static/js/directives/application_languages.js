'use strict';

var ApplicationLanguagesDirective = function ($modal) {
    var _this = this;

    _this.restrict = 'EA';
    _this.templateUrl = 'html/directives/application_languages.html';
    _this.scope = {
        available: '=availableLanguages',
        used: '=appLanguages',
        filter: '=languagesFilter',
        addHandler: '=onAdd',
        removeHandler: '=onRemove'
    };

    _this.link = function ($scope) {

        $scope.toggle = function (name) {
            $scope.filter = [];
            angular.forEach($scope.used, function (language) {
                if (name == language.name) {
                    language['unchecked'] = (language['unchecked']) ? false : true;
                }
                if (!language['unchecked']) {
                    $scope.filter.push(language.name);
                }
            });
        };

        $scope.remove = function (name) {
            event.stopImmediatePropagation();
            $scope.removeHandler(name);
        };

        $scope.showModal = function () {
            $modal.open({
                templateUrl: 'html/app/add_language.html',
                controller: function ($scope, $modalInstance, available, used, addHandler) {
                    $scope.available = available;
                    $scope.used = used;
                    $scope.addHandler = addHandler;
                    $scope.selected = null;

                    $scope.cancel = function () {
                        $modalInstance.dismiss('canceled');
                    };

                    $scope.save = function () {
                        if (!angular.isString($scope.selected)) return;
                        $scope.addHandler($scope.selected);
                        $modalInstance.close('saved');
                    }
                },
                resolve: {
                    available: function () {
                        var available = [];
                        var usedIds = $scope.used.map(function(item) {
                            return item.id;
                        });
                        for (var i = 0; i < $scope.available.length; i++) {
                            if (-1 < usedIds.indexOf($scope.available[i].id)) continue;
                            available.push($scope.available[i]);
                        }
                        return available;
                    },
                    used: function () {
                        return $scope.used;
                    },
                    addHandler: function () {
                        return $scope.addHandler;
                    }
                }
            });
        };
    };
};

locoMoco.directive('applicationLanguages', ['$modal', function ($modal) {
    return new ApplicationLanguagesDirective($modal);
}]);

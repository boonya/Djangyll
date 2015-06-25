'use strict';

var EditableScreenTagsDirective = function () {
    var _this = this;

    _this.restrict = 'EA';
    _this.templateUrl = 'html/directives/editable_screen_tags.html';
    _this.scope = {
        id: '=id',
        screens: '=screens',
        original: '=original',
        available: '=available',
        setHandler: '=onSet'
    };

    _this.link = function ($scope) {
        $scope.editMode = false;

        $scope.toggleEditMode = function () {
            if (!$scope.setHandler) return;
            $scope.editMode = $scope.editMode ? false : true;
            $scope.previous = $scope.screens;
        };

        $scope.save = function () {
            $scope.setHandler($scope.id, $scope.screens);
            $scope.toggleEditMode();
        };

        $scope.reset = function () {
            $scope.screens = $scope.previous;
            $scope.toggleEditMode();
        };

        $scope.tagging = function (value) {
            return {name: value};
        };
    };
};

locoMoco.directive('editableScreenTags', [function () {
    return new EditableScreenTagsDirective();
}]);

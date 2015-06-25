'use strict';

var EditableTextDirective = function () {
    var _this = this;

    _this.restrict = 'EA';
    _this.templateUrl = 'html/directives/editable_text.html';
    _this.transclude = true;
    _this.scope = {
        id: '=id',
        language: '=language',
        text: '=text',
        setHandler: '=onSet',
        rollbackHandler: '=onRollback'
    };

    _this.link = function ($scope) {
        $scope.editMode = false;
        $scope.original = $scope.text;

        $scope.toggleEditMode = function () {
            if (!$scope.setHandler || !$scope.rollbackHandler) return;
            $scope.editMode = $scope.editMode ? false : true;
        };

        $scope.save = function () {
            $scope.setHandler($scope.id, $scope.language, $scope.text);
            $scope.toggleEditMode();
        };

        $scope.reset = function () {
            $scope.text = $scope.original;
            $scope.toggleEditMode();
        };

        $scope.rollback = function () {
            $scope.text = $scope.original;
            $scope.rollbackHandler($scope.id, $scope.language);
        };

        $scope.isChanged = function () {
            return $scope.text != $scope.original;
        };
    };
};

locoMoco.directive('editableText', [function () {
    return new EditableTextDirective();
}]);

'use strict';

var BreadcrumbsDirective = function () {
    var self = this;

    self.restrict = 'EA';
    self.templateUrl = 'html/directives/breadcrumbs.html';
    self.scope = {};

    self.link = function ($scope) {
    };
};

Djangyll.directive('breadcrumbs', [function () {
    return new BreadcrumbsDirective();
}]);

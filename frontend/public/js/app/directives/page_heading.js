'use strict';

var PageHeadingDirective = function () {
    var self = this;

    self.restrict = 'EA';
    self.templateUrl = 'html/directives/page_heading.html';
    self.scope = {};

    self.link = function ($scope) {
    };
};

Djangyll.directive('pageHeading', [function () {
    return new PageHeadingDirective();
}]);

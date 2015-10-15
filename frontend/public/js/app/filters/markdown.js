'use strict';

Djangyll.filter("markdown", ['$sce', function ($sce) {
    return function (markdownString) {
        var htmlCode = markdown.toHTML(markdownString);
        return $sce.trustAsHtml(htmlCode);
    }
}]);
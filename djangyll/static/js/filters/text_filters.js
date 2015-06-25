locoMoco.filter('texts_filter', function () {
    return function (input, query) {
        if (!angular.isArray(input) || !input.length) return [];
        if (!angular.isArray(query)) return input;
        if (!query.length) return [];

        var result = [];
        for (var i = 0; i < input.length; i++) {
            if (-1 < query.indexOf(input[i].name)) {
                result.push(input[i]);
            }
        }
        return result;
    };
});
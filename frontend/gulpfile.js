var gulp = require('gulp'),
    webserver = require('gulp-webserver'),
    concat = require('gulp-concat');

var jsFiles = cssFiles = [];

gulp.task('webserver', function () {
    gulp.src('public')
        .pipe(webserver({
            livereload: true,
            directoryListing: false,
            open: true
        }));
});

gulp.task('concat-css', function () {
    cssFiles = ['./node_modules/bootstrap/dist/css/bootstrap.min.css',
        './public/css/sb-admin.css',
        './public/css/preloader.css',
        './node_modules/textangular/dist/textAngular.css'];

    gulp.src(cssFiles)
        .pipe(concat('common.css'))
        .pipe(gulp.dest('./public/css/'));
});

gulp.task('concat-js', function () {
    var libs = ['./startbootstrap-sb-admin/js/jquery.js',
        './startbootstrap-sb-admin/js/bootstrap.min.js',
        './node_modules/angular/angular.min.js',
        './node_modules/angular-cookies/angular-cookies.min.js',
        './node_modules/angular-resource/angular-resource.min.js',
        './node_modules/angular-route/angular-route.min.js',
        './node_modules/markdown/lib/markdown.js',
        './node_modules/textangular/dist/textAngular-rangy.min.js',
        './node_modules/textangular/dist/textAngular-sanitize.min.js',
        './node_modules/textangular/dist/textAngular.min.js'];

    var core = ['./public/js/app/init.js',
        './public/js/app/api_core.js',
        './public/js/app/routing.js'];

    var directives = ['./public/js/app/directives/page_heading.js',
        './public/js/app/directives/breadcrumbs.js'];

    var filters = ['./public/js/app/filters/markdown.js'];

    var services = ['./public/js/app/services/post.js'];

    var controllers = ['./public/js/app/controllers/global.js',
        './public/js/app/controllers/post-list.js',
        './public/js/app/controllers/post.js'];

    jsFiles = [].concat(libs, core, directives, filters, services, controllers);

    gulp.src(jsFiles)
        .pipe(concat('common.js'))
        .pipe(gulp.dest('./public/js/'));
});

gulp.task('copy-fonts', function () {
    gulp.src('./startbootstrap-sb-admin/font-awesome/fonts/**/*.{ttf,woff,eof,svg}')
        .pipe(gulp.dest('./public/font-awesome/fonts'));

    gulp.src('./startbootstrap-sb-admin/font-awesome/css/**/*.min.css')
        .pipe(gulp.dest('./public/font-awesome/css'));
});

gulp.task('concat', function () {
    gulp.run('concat-js');
});

gulp.task('build', function () {
    gulp.run('copy-fonts');
    gulp.run('concat-css');
    gulp.run('concat-js');
});

gulp.task('watch', function () {
    gulp.run('build');

    var observable = [].concat(jsFiles, cssFiles);
    gulp.watch(observable, function() {
        gulp.run('build');
    });

    gulp.run('webserver');
});
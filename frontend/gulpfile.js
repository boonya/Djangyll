var gulp = require('gulp'),
    webserver = require('gulp-webserver');

gulp.task('webserver', function () {
    gulp.src('public')
        .pipe(webserver({
            livereload: true,
            directoryListing: false,
            open: true
        }));
});

gulp.task('copy-css', function () {
    gulp.src(['./startbootstrap-sb-admin/css/bootstrap.min.css',
        './startbootstrap-sb-admin/css/sb-admin.css'])
        .pipe(gulp.dest('./public/css'));
});

gulp.task('copy-js', function () {
    gulp.src(['./startbootstrap-sb-admin/js/jquery.js',
        './startbootstrap-sb-admin/js/bootstrap.min.js'])
        .pipe(gulp.dest('./public/js/lib'));

    gulp.src(['./node_modules/angular/angular.min.js',
        './node_modules/angular-cookies/angular-cookies.min.js',
        './node_modules/angular-resource/angular-resource.min.js',
        './node_modules/angular-route/angular-route.min.js'])
        .pipe(gulp.dest('./public/js/lib'));
});

gulp.task('copy-fonts', function () {
    gulp.src('./startbootstrap-sb-admin/font-awesome/fonts/**/*.{ttf,woff,eof,svg}')
        .pipe(gulp.dest('./public/font-awesome/fonts'));

    gulp.src('./startbootstrap-sb-admin/font-awesome/css/**/*.min.css')
        .pipe(gulp.dest('./public/font-awesome/css'));
});

gulp.task('build', function () {
    gulp.run('copy-fonts');
    gulp.run('copy-css');
    gulp.run('copy-js');
});

// Запуск сервера разработки gulp watch
gulp.task('watch', function () {
    gulp.run('build');
    gulp.run('webserver');
});
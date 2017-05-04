var gulp = require('gulp'),
	postcss = require('gulp-postcss'),
	autoprefixer = require('autoprefixer'),
	cssnext = require('cssnext'),
	precss = require('precss'),
	sass = require('gulp-sass'),
	cssnano = require('cssnano');

gulp.task('css', function () {
	var processors = [
		autoprefixer,
		cssnano(),
		precss
	];
	return gulp.src('./src/*.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(postcss(processors))
		.pipe(gulp.dest('./dest'));
});

gulp.task('watch', function() {
	gulp.watch('./src/*.scss', ['css']);
});

gulp.task('build', ['css']);

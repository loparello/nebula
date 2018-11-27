import Vue from 'vue';

import IntroJumbotron from './components/IntroJumbotron';

import '../sass/main.scss';

try {
    window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');

    require('bootstrap');
} catch (error) {
    console.error(error);
}

new Vue({
    el: '#app',
    components: { 
        'intro-jumbotron': IntroJumbotron 
    }
});


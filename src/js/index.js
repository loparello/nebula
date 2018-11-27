import Vue from 'vue';

import IntroJumbotron from './components/IntroJumbotron';

import '../sass/main.scss';

new Vue({
    el: '#app',
    components: { 
        'intro-jumbotron': IntroJumbotron 
    }
});


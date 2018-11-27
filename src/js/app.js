// Loads Vue for front-end interactivity. 
import Vue from 'vue';

import IntroJumbotron from './components/IntroJumbotron';

new Vue({
    el: '#app',
    components: { 
        'intro-jumbotron': IntroJumbotron 
    }
});
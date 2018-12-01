/* Loads istances of Vue for front-end interactivity. 
*  This file will get compiled into 'app.js' and loaded  
*  at the bottom of the template body.
*/  
import Vue from 'vue';

import HeroBody from './components/HeroBody';

new Vue({
    el: '#app',
    components: { 
        'hero-body': HeroBody 
    }
});
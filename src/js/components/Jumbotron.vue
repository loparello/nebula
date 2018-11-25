<template>
    <div class="intro-jumbotron jumbotron text-center">
        <h1 class="display-4">Welcome to Nebula</h1>
        <p class="lead">A simple Django Framework strater toolkit for apps, websites and blogs development, empowered with Vue.js on the front-end</p>
        <hr class="my-4 bg-light">
        <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
        <p class="lead">
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
        </p>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Jumbotron component mounted with Vue.js')
        }
    }
</script>
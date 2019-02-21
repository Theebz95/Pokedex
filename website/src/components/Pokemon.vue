<template>
<div class="container-pokedex">
<button v-on:click="showDetails()">
<h1>{{ pokemon.name }}</h1>
</button>
</div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Pokemon',
        props: ['pokemon', 'onclick'],
        methods: {
            showDetails: function(){
                axios.get(`http://127.0.0.1:5000/pokemons?pokemon=${this.pokemon.name}`)
                .then(response => {
                    const {id, abilities, moves, types, height, weight} = response.data;
                    console.log(id);
                    abilities.forEach(element => {
                        console.log(element.ability.name);
                    });
                    //console.log(response.data);
                })
                .catch(e => {
                    console.log(e);
                })
            }
        },
    };
</script>

<style>
    .container-pokedex button{
        border: none;
    }
</style>
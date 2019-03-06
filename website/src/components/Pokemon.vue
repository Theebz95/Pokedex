<template>
<div class="container-pokedex">
<button v-on:click="showDetails()">
<h1>{{ pokemon.name }}</h1>
</button>
<Pokeball v-if="visibility" :visible="visibility" />
<!-- <vodal :show="show" animation="rotate" @hide="show = visibility"></vodal> -->
</div>
</template>

<script>
    import axios from 'axios'
    import Vodal from 'vodal'
    import swal from 'sweetalert2'
    import Pokeball from './Pokeball.vue'

    export default {
        name: 'Pokemon',
        components: {
            Vodal,
            Pokeball,
        },
        props: ['pokemon', 'onclick'],
        data(){
            return{
                visibility : false,
            }
        },
        methods: {
            openPokemon: function() {
                this.visibility = true
            },
            openModel: function(params) {
                //console.log(params);
                let megaString = '<div class="height-weight-container"><div class="height-container"><h3>Height: </h3>' + params.height + ' inches</div>';
                megaString += '<div class="weight-container"><h3>Weight: </h3>' + params.weight + ' pounds</div></div>';
                megaString = megaString + '</div><br /><h3>Types:</h3>';
                params.types.forEach((element, index) => {
                    //console.log(element.type.name);
                    megaString += element.type.name;
                    if(params.types.length-1 !== index ){
                        megaString += ', ';
                    }
                });
                swal.fire({
                     title: params.name,
                     html: megaString,
                     confirmButtonText: 'Cool'
                })
            },
            showDetails: function(){
                axios.get(`http://127.0.0.1:5000/pokemons?pokemon=${this.pokemon.name}`)
                .then(response => {
                    const {id, name, abilities, moves, types, height, weight} = response.data;
                    // console.log(id);
                    // console.log(name);
                    // abilities.forEach(element => {
                    //     console.log(element.ability.name);
                    // });
                    // moves.forEach(element => {
                    //     console.log(element.move.name);
                    // });
                    // types.forEach(element => {
                    //     console.log(element.type.name);
                    // });
                    // console.log(height + " inches");
                    // console.log(weight + " pounds");
                    //this.openModel(response.data);
                    this.openPokemon();
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
    .height-container, .weight-container{
        width: 100%;
        display: flex;
        flex-flow: column nowrap;
        justify-content: space-evenly;
    }
    .height-weight-container{
        display: flex;
        flex-flow: row nowrap;
    }
    .moves-container{
        width:100%;
        display: flex;
        flex-flow: row wrap;
        justify-content: space-evenly;
    }
    .moves-container p{
        width: 33%;
        margin-bottom:-5%;
    }
    .swal2-show{
        width: 500px;
        height: 500px;
        border-radius: 50%;
        background-color: red;
    }
</style>
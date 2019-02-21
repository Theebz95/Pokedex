<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Pokemon"/>
    <Pokemon v-for='pokemon in pokemons' :key='pokemon.id' :pokemon='pokemon' />
    <div class="loading" v-if="loading">
      <img src="./assets/gifs/pokeball.gif" height="100px">
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import Pokemon from './components/Pokemon.vue';
import axios from 'axios';

export default {
  name: 'app',
  components: {
    HelloWorld,
    Pokemon,
  },
  data(){
    return {
      pokemons : [],
      nextLink : '',
      loading: false,
    }
  },
  beforeMount(){
    this.fetch();
  },
  created () {
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods:{
    fetch: function(){
      axios.get('http://127.0.0.1:5000/popo')
      .then(response => {
        console.table(response.data.results);
        console.log(response.data.next);
        this.pokemons = response.data.results
        this.nextLink = response.data.next
      })
      .catch(e => {
        console.log(e);
      })
    },
    handleScroll () {
      if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight){
        console.log("reach bottom, started from the bottom now we still here");
        this.loading = true
 
        axios.get(this.nextLink)
        .then(x => new Promise(resolve => setTimeout(() => resolve(x), 1500)))
        .then(response => {
          console.log(response.data.results);
          response.data.results.forEach(element => {
            this.pokemons.push(element)
          });
          this.nextLink = response.data.next
        })
        .catch(e => {
          console.log(e);
        })
        .finally(() => {
          this.loading = false;
        })
      }
    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.loading{
  display: flex;
  justify-content: center;
}
</style>

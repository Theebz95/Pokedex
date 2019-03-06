<template>
<div>
<div v-click-outside="hide" class="pokeball">
  <div class="top">
    <div class="middle_circle">
        <div class="white_in"></div>
    </div>
  </div>
  <div class="bottom"></div>
</div>
</div>
</template>

<script>
    import ClickOutside from 'vue-click-outside'

    export default {
        name: 'Pokeball',
        components: {
        },
        props: ['pokemon', 'onclick', 'visible'],
        data(){
            return{}
        },
        beforeMount(){
            console.log(this.visible);
            console.log("I dont know wat im doign");

        },
        methods: {
            hide(){
                this.visible = false
                console.log(this.visible);
            }
        },
        directives: {
            ClickOutside
        }
    };
</script>

<style>
@font-face {
  font-family: 'Spinnaker';
  font-style: normal;
  font-weight: 400;
  src: local('Spinnaker'), local('Spinnaker-Regular'), url(http://themes.googleusercontent.com/static/fonts/spinnaker/v5/WxzDAY6mC9v3znSJEtCoWz8E0i7KZn-EPnyo3HZu7kw.woff) format('woff');
}

body{
    overflow-y: hidden;
}


.pokeball{
  margin:50px auto;
  animation: spin 1.8s infinite linear;
  margin-bottom: 25%;
}

div {
  margin: 0 auto; padding: 0;
}

.top{
  background-color:#EB2224;
  height:110px;
  width:230px;
  border: solid black 0.5px;
  border-radius:195px 195px 0 0;
  border-bottom:6px solid #000000;
}

/*.middle{
  background-color:#000000;
  width:230px;
  height:1px;
  border:4px solid #000000;
}*/

.middle_circle{
  background-color:#FFFFFF;
  width:75px;
  height:75px;
  border-radius:50%;
  margin: 70px 65px;
  position:absolute;
  border:12px solid #000000;
}

.white_in{
  background-color:#FFFFFF;
  width:50px;
  height:50px;
  border-radius:50%;
  padding:4px 4px;
  margin:5px 6px;
  border:3px solid #000000;
  -webkit-animation:myfirst 5s; /* Chrome, Safari, Opera */
  animation:myfirst 4s infinite linear;
}

.bottom{
  background-color:#FFFFFF;
  height:110px;
  width:230px;
  border-radius:0 0 195px 195px;
  border-top:6px solid #000000;
  border-bottom: solid black 0.5px;
}

/* Animations */

@keyframes spin {
	0%  {transform: rotate(0deg);}
	50%{transform: rotate(40deg);}
   100%{transform: rotate(0deg);}
}

/* Chrome, Safari, Opera */
@-webkit-keyframes myfirst
{
0%   {background: white;}
25%   {background: #db9090;}
50%   {background: white;}
75%  {background: #db9090;}
}

/* Standard syntax */
@keyframes myfirst
{
0%   {background: white;}
25%   {background: #db9090;}
50%   {background: white;}
75%  {background: #db9090;}
}

</style>